from django.contrib import admin
from .models import Producto, Reseña

admin.site.register(Producto)

@admin.register(Reseña)
class ReseñaAdmin(admin.ModelAdmin):
    list_display = ('nombre_cliente', 'calificacion', 'fecha')
    list_filter = ('calificacion', 'fecha')

from .models import Producto, Reseña, Cupon

@admin.register(Cupon)
class CuponAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'descuento_porcentaje', 'activo')
    list_filter = ('activo',)