from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import RegistroUsuarioForm, LoginForm
from recetas.models import Receta

# Contexto base para la portada
def _inicio_contexto_base():
    recetas_recientes = Receta.objects.order_by("-id")[:9]
    return {
        "recetas_recientes": recetas_recientes,
    }

# Vista para la portada con formularios de login y registro en modales
def _render_inicio_con_form(request, *, login_form=None, registro_form=None, open_modal=None, status=200):
    ctx = _inicio_contexto_base()
    ctx.setdefault("login_form", login_form if login_form is not None else LoginForm(request=request))
    ctx.setdefault("registro_form", registro_form if registro_form is not None else RegistroUsuarioForm())
    ctx["open_modal"] = open_modal
    return render(request, "recetas/inicio.html", ctx, status=status)

# Vista para el modal de login
@require_POST
def login_modal(request):
    form = LoginForm(request=request, data=request.POST)
    if form.is_valid():
        user = form.get_user()
        auth_login(request, user)
        return redirect("inicio")
    
    return _render_inicio_con_form(
        request,
        login_form=form,
        registro_form=RegistroUsuarioForm(),
        open_modal="login",
        status=400,
    )

# Vista para el modal de registro
@require_POST
def registro_modal(request):
    form = RegistroUsuarioForm(request.POST)
    if form.is_valid():
        user = form.save()
        username = form.cleaned_data.get("username")
        raw_password = form.cleaned_data.get("password1")
        user = authenticate(request, username=username, password=raw_password)
        if user is not None:
            auth_login(request, user)
        return redirect("inicio")

    return _render_inicio_con_form(
        request,
        login_form=LoginForm(request=request),
        registro_form=form,
        open_modal="registro",
        status=400,
    )

# Vista para cerrar sesión
def cerrar_sesion(request):
    logout(request)
    return redirect("inicio")

# Vista para cambiar la contraseña
class CambiarContrasenaView(LoginRequiredMixin, PasswordChangeView):
    template_name = "cuentas/cambiar_contrasena.html"
    success_url = reverse_lazy("perfil")
