from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)

    def __str__(self):
        return self.nombre

class Reseña(models.Model):
    nombre_cliente = models.CharField(max_length=100, verbose_name="Nombre de la Clienta")
    calificacion = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)], verbose_name="Calificación (Estrellas)")
    comentario = models.TextField(verbose_name="Comentario")
    fecha = models.DateTimeField(auto_now_add=True, verbose_name="Fecha")

    def __str__(self):
        return f"{self.nombre_cliente} - {self.calificacion} Estrellas"

class Cupon(models.Model):
    codigo = models.CharField(max_length=50, unique=True, verbose_name="Código de Cupón")
    descuento_porcentaje = models.IntegerField(verbose_name="Descuento en % (Ej: 10 para 10%)")
    activo = models.BooleanField(default=True, verbose_name="¿Está activo?")

    def __str__(self):
        return f"{self.codigo} ({self.descuento_porcentaje}%)"
