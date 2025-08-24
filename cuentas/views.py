from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import RegistroUsuarioForm, LoginForm
from recetas.models import Receta

def _inicio_contexto_base():
    """Contexto mínimo que tu portada usa (ajústalo si necesitas más)."""
    recetas_recientes = Receta.objects.order_by("-id")[:9]
    return {
        "recetas_recientes": recetas_recientes,
    }

def _render_inicio_con_form(request, *, login_form=None, registro_form=None, open_modal=None, status=200):
    """
    Renderiza la portada con los formularios y una bandera para abrir el modal correspondiente.
    """
    ctx = _inicio_contexto_base()
    ctx.setdefault("login_form", login_form if login_form is not None else LoginForm(request=request))
    ctx.setdefault("registro_form", registro_form if registro_form is not None else RegistroUsuarioForm())
    ctx["open_modal"] = open_modal  # 'login' | 'registro' | None
    return render(request, "recetas/inicio.html", ctx, status=status)

@require_POST
def login_modal(request):
    form = LoginForm(request=request, data=request.POST)
    if form.is_valid():
        user = form.get_user()
        auth_login(request, user)
        return redirect("inicio")
    # Volvemos a la portada con el modal de login abierto y errores en el form
    return _render_inicio_con_form(
        request,
        login_form=form,
        registro_form=RegistroUsuarioForm(),
        open_modal="login",
        status=400,
    )

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
    # Volvemos a la portada con el modal de registro abierto y errores en el form
    return _render_inicio_con_form(
        request,
        login_form=LoginForm(request=request),
        registro_form=form,
        open_modal="registro",
        status=400,
    )

def cerrar_sesion(request):
    logout(request)
    return redirect("inicio")

class CambiarContrasenaView(LoginRequiredMixin, PasswordChangeView):
    template_name = "cuentas/cambiar_contrasena.html"
    success_url = reverse_lazy("perfil")
