from django.shortcuts import render, redirect
from .models import Producto, Reseña

def index(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        calificacion = request.POST.get('calificacion')
        comentario = request.POST.get('comentario')
        if nombre and calificacion and comentario:
            Reseña.objects.create(
                nombre_cliente=nombre,
                calificacion=calificacion,
                comentario=comentario
            )
            return redirect('index')

    productos = Producto.objects.all()
    reseñas = Reseña.objects.all().order_by('-fecha')
    return render(request, 'index.html', {'productos': productos, 'reseñas': reseñas})