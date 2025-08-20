from django.shortcuts import render, redirect
from .forms import RegistroUsuarioForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Vista de registro
def registro(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistroUsuarioForm()
    return render(request, 'cuentas/registro.html', {'form': form})

# Vista de cierre de sesión
def cerrar_sesion(request):
    logout(request)
    return redirect('inicio')

# Vista para cambiar la contraseña
class CambiarContrasenaView(LoginRequiredMixin, PasswordChangeView):
    template_name = 'cuentas/cambiar_contrasena.html'
    success_url = reverse_lazy('perfil')