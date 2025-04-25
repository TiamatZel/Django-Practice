from django.shortcuts import render, get_object_or_404, redirect
from .models import Libro
from .forms import ResenaForm

def lista_libros(request):
    libros = Libro.objects.all()
    return render(request, 'biblioteca/lista_libros.html', {'libros': libros})

def detalle_libro(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    reseñas = libro.resena_set.all()

    if request.method == 'POST':
        form = ResenaForm(request.POST)
        if form.is_valid():
            nueva_resena = form.save(commit=False)
            nueva_resena.libro = libro
            nueva_resena.save()
            return redirect('detalle_libro', pk=libro.pk)
    else:
        form = ResenaForm()

    return render(request, 'biblioteca/detalle_libro.html', {
        'libro': libro,
        'reseñas': reseñas,
        'form': form
    })

