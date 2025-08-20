from django.shortcuts import render, get_object_or_404, redirect
from .models import Receta
from django.contrib.auth.decorators import login_required
from .forms import RecetaForm, PerfilForm
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Vista de inicio
def inicio(request):
    return render(request, 'recetas/inicio.html')

# Vista "Acerca de mí"
def acerca_de_mi(request):
    return render(request, 'recetas/about.html')

# Vista de listado de recetas
class ListaRecetasView(ListView):
    model = Receta
    template_name = 'recetas/lista_recetas.html'
    context_object_name = 'recetas'
    ordering = ['-id']

# Vista de detalle de receta
class DetalleRecetaView(DetailView):
    model = Receta
    template_name = 'recetas/detalle_receta.html'
    context_object_name = 'receta'

# Vista de creación de receta
class CrearRecetaView(LoginRequiredMixin, CreateView):
    model = Receta
    fields = ['titulo', 'descripcion', 'imagen', 'ingredientes', 'instrucciones']
    template_name = 'recetas/crear_receta.html'
    success_url = '/recetas/'

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

# Vista para editar receta
@login_required
def editar_receta(request, pk):
    receta = get_object_or_404(Receta, pk=pk)
    if request.method == 'POST':
        form = RecetaForm(request.POST, request.FILES, instance=receta)
        if form.is_valid():
            form.save()
            return redirect('lista_recetas')
    else:
        form = RecetaForm(instance=receta)
    return render(request, 'recetas/editar_receta.html', {'form': form, 'receta': receta})

# Vista para eliminar receta
@login_required
def eliminar_receta(request, pk):
    receta = get_object_or_404(Receta, pk=pk)
    if request.method == 'POST':
        receta.delete()
        return redirect('lista_recetas')
    return render(request, 'recetas/eliminar_receta.html', {'receta': receta})

# Vista de perfil de usuario
@login_required
def perfil_usuario(request):
    return render(request, 'recetas/perfil.html')

# Vista de mis recetas
@login_required
def mis_recetas(request):
    recetas_usuario = Receta.objects.filter(autor=request.user).order_by('-fecha_creacion')
    return render(request, 'recetas/mis_recetas.html', {'recetas': recetas_usuario})

# Vista para editar perfil de usuario
@login_required
def editar_perfil(request):
    perfil = request.user.perfil

    if request.method == 'POST':
        form = PerfilForm(request.POST, request.FILES, instance=perfil)
        if form.is_valid():
            form.save()
            return redirect('perfil')
    else:
        form = PerfilForm(instance=perfil)

    return render(request, 'recetas/editar_perfil.html', {'form': form})