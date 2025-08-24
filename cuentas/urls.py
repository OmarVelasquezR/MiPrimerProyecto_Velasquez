from django.urls import path
from . import views
from .views import CambiarContrasenaView

urlpatterns = [
    path("login/", views.login_modal, name="login"),
    path("registro/", views.registro_modal, name="registro"),
    path("logout/", views.cerrar_sesion, name="logout"),
    path("cambiar-contrasena/", CambiarContrasenaView.as_view(), name="cambiar_contrasena"),
]
