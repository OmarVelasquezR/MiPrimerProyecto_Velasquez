from .forms import RegistroUsuarioForm, LoginForm

def forms_globales(request):
    return {
        "login_form": LoginForm(request=request),
        "registro_form": RegistroUsuarioForm(),
    }
