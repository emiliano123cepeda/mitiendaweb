from django.contrib import admin
from .models import Producto, Reseña

admin.site.register(Producto)

@admin.register(Reseña)
class ReseñaAdmin(admin.ModelAdmin):
    list_display = ('nombre_cliente', 'calificacion', 'fecha')
    list_filter = ('calificacion', 'fecha')