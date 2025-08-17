from django.shortcuts import render, get_object_or_404, redirect
from .models import Receta
from django.contrib.auth.decorators import login_required
from .forms import RecetaForm
from django.shortcuts import render

# Vista de inicio
def inicio(request):
    return render(request, 'recetas/inicio.html')

# Vista "Acerca de mí"
def acerca_de_mi(request):
    return render(request, 'recetas/about.html')

# Vista de listado de recetas
def lista_recetas(request):
    recetas = Receta.objects.all().order_by('-fecha_creacion')
    return render(request, 'recetas/lista_recetas.html', {'recetas': recetas})

# Vista de detalle de receta
def detalle_receta(request, pk):
    receta = get_object_or_404(Receta, pk=pk)
    return render(request, 'recetas/detalle_receta.html', {'receta': receta})

# Vista de creación de receta
@login_required
def crear_receta(request):
    if request.method == 'POST':
        form = RecetaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_recetas')
    else:
        form = RecetaForm()
    return render(request, 'recetas/crear_receta.html', {'form': form})

# Vista para editar
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

# Vista para eliminar
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
    return render(request, 'recetas/mis_recetas.html')

