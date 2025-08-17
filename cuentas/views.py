from django.shortcuts import render, redirect
from .forms import RegistroUsuarioForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

def registro(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistroUsuarioForm()
    return render(request, 'cuentas/registro.html', {'form': form})

def cerrar_sesion(request):
    logout(request)
    return redirect('inicio')
