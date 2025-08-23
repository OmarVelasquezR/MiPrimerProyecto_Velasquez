from django.shortcuts import render, redirect
from .forms import RegistroUsuarioForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login as auth_login

# Vista de registro de usuario
def registro(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            # Guardar y loguear automáticamente
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = form.save()
            user = authenticate(request, username=username, password=raw_password)
            if user is not None:
                auth_login(request, user)
                return redirect('inicio')
            return redirect('login')
    else:
        form = RegistroUsuarioForm()
    # Fallback si alguien entra por URL directa
    return render(request, 'cuentas/registro.html', {'form': form})

# Vista de cierre de sesión
def cerrar_sesion(request):
    logout(request)
    return redirect('inicio')

# Vista para cambiar la contraseña
class CambiarContrasenaView(LoginRequiredMixin, PasswordChangeView):
    template_name = 'cuentas/cambiar_contrasena.html'
    success_url = reverse_lazy('perfil')