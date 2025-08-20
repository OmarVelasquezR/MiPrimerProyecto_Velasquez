from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import ListaRecetasView, DetalleRecetaView

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('about/', views.acerca_de_mi, name='acerca_de_mi'),
    path('recetas/', ListaRecetasView.as_view(), name='lista_recetas'),
    path('recetas/<int:pk>/', DetalleRecetaView.as_view(), name='detalle_receta'),
    path('crear/', views.CrearRecetaView.as_view(), name='crear_receta'),
    path('recetas/<int:pk>/editar/', views.editar_receta, name='editar_receta'),
    path('recetas/<int:pk>/eliminar/', views.eliminar_receta, name='eliminar_receta'),
    path('login/', auth_views.LoginView.as_view(template_name='cuentas/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='inicio'), name='logout'),
    path('perfil/', views.perfil_usuario, name='perfil'),
    path('mis-recetas/', views.mis_recetas, name='mis_recetas'),
    path('editar-perfil/', views.editar_perfil, name='editar_perfil'),
]

