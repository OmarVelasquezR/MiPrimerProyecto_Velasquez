from .forms import RegistroUsuarioForm, LoginForm

# Contexto para formularios de autenticación
def forms_globales(request):
    return {
        "login_form": LoginForm(request=request),
        "registro_form": RegistroUsuarioForm(),
    }
