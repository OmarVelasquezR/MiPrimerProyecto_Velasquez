from .forms import RegistroUsuarioForm, LoginForm

def forms_globales(request):
    
    return {
        'registro_form': RegistroUsuarioForm(),
        'login_form': LoginForm(request=request),
    }
