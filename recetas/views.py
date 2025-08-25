from django.shortcuts import render, get_object_or_404, redirect
from .models import Receta
from django.contrib.auth.decorators import login_required
from .forms import RecetaForm, PerfilForm
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Vista de inicio
def inicio(request):
    recetas_recientes = Receta.objects.order_by('-creado')[:6]
    return render(request, 'recetas/inicio.html', {'recetas_recientes': recetas_recientes})

# Vista About
def acerca_de_mi(request):
    return render(request, 'recetas/about.html')

# Vista de todas las recetas
class ListaRecetasView(ListView):
    model = Receta
    template_name = 'recetas/lista_recetas.html'
    context_object_name = 'recetas'
    
    def get_queryset(self):
        queryset = super().get_queryset().order_by('-creado')
        consulta = self.request.GET.get('q')
        categoria = self.request.GET.get('categoria')
        dificultad = self.request.GET.get('dificultad')

        if consulta:
            queryset = queryset.filter(titulo__icontains=consulta)
        if categoria:
            queryset = queryset.filter(categorias__icontains=categoria)
        if dificultad:
            queryset = queryset.filter(dificultad=dificultad)

        return queryset

# Vista de detalle de receta
class DetalleRecetaView(DetailView):
    model = Receta
    template_name = 'recetas/detalle_receta.html'
    context_object_name = 'receta'

# Vista de creación de receta
class CrearRecetaView(LoginRequiredMixin, CreateView):
    model = Receta
    form_class = RecetaForm
    template_name = 'recetas/crear_receta.html'
    success_url = '/recetas/'

    def post(self, request, *args, **kwargs):
        receta = Receta()
        receta.autor = request.user
        receta.titulo = request.POST.get('titulo')
        receta.descripcion = request.POST.get('descripcion')
        receta.dificultad = request.POST.get('dificultad')
        receta.tiempo = request.POST.get('tiempo')
        receta.porciones = request.POST.get('porciones')
        receta.categorias = request.POST.get('categorias', '')
        receta.alergias = request.POST.get('alergias', '')

        if 'imagen' in request.FILES:
            receta.imagen = request.FILES['imagen']

        # Ingredientes dinámicos
        nombres = request.POST.getlist('ingredientes[nombre][]')
        cantidades = request.POST.getlist('ingredientes[cantidad][]')
        unidades = request.POST.getlist('ingredientes[unidad][]')
        receta.ingredientes = [
            {"nombre": n, "cantidad": c, "unidad": u}
            for n, c, u in zip(nombres, cantidades, unidades)
            if n or c
        ]

        # Instrucciones dinámicas
        receta.instrucciones = request.POST.getlist('instrucciones[]')

        receta.save()
        return redirect('lista_recetas')

# Vista para editar receta
@login_required
def editar_receta(request, pk):
    receta = get_object_or_404(Receta, pk=pk, autor=request.user)
    categorias_default = ["Desayunos", "Almuerzos", "Cenas", "Postres", "Bebidas", "Vegetariano", "Vegano"]
    alergias_default = ["Leche", "Huevo", "Maní", "Frutos secos", "Soja", "Gluten", "Pescado", "Marisco"]

    if request.method == 'POST':
        # Campos simples
        receta.titulo = request.POST.get('titulo')
        receta.descripcion = request.POST.get('descripcion')
        receta.dificultad = request.POST.get('dificultad')
        receta.tiempo = request.POST.get('tiempo')
        receta.porciones = request.POST.get('porciones')
        receta.categorias = request.POST.get('categorias', '')
        receta.alergias = request.POST.get('alergias', '')

        # Imagen principal
        if 'imagen' in request.FILES:
            receta.imagen = request.FILES['imagen']

        # Más fotos (si manejas campo en el modelo)
        if 'fotos_extra' in request.FILES:
            receta.fotos_extra = request.FILES.getlist('fotos_extra')

        # Ingredientes dinámicos
        nombres = request.POST.getlist('ingredientes[nombre][]')
        cantidades = request.POST.getlist('ingredientes[cantidad][]')
        unidades = request.POST.getlist('ingredientes[unidad][]')
        receta.ingredientes = [
            {"nombre": n, "cantidad": c, "unidad": u}
            for n, c, u in zip(nombres, cantidades, unidades)
            if n or c
        ]

        # Instrucciones dinámicas
        receta.instrucciones = request.POST.getlist('instrucciones[]')

        # Guardar cambios
        receta.save()
        return redirect('mis_recetas')

    return render(request, 'recetas/editar_receta.html', {
        'receta': receta,
        'categorias_default': categorias_default,
        'alergias_default': alergias_default,
    })

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
    recetas_usuario = Receta.objects.filter(autor=request.user).order_by('-creado')
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
