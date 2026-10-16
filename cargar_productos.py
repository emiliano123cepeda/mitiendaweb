import os
import django

# Configurar el entorno de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mitienda.settings')
django.setup()

from catalogo.models import Producto

# Lista de productos extraídos de tu catálogo
productos_catalogo = [
    # Cejas
    {"nombre": "Gel de Cejas Brow Harmony - Rare Beauty", "descripcion": "Gel de cejas transparente, ligero, fija y da forma con fijación flexible todo el día.", "precio": 15.00, "categoria": "Cejas"},
    
    # Pestañas y Rímeles
    {"nombre": "Removedor de Pestañas Sheglam", "descripcion": "Ideal para remover máscara a prueba de agua sin irritar.", "precio": 8.50, "categoria": "Pestañas"},
    {"nombre": "Máscara de Pestañas Prosa Profesional", "descripcion": "Cepillo de silicón, fórmula contra agua, máximo alargamiento y volumen.", "precio": 6.00, "categoria": "Pestañas"},
    {"nombre": "Sheglam All-in-One Volume & Length", "descripcion": "Máscara de pestañas todo en uno color negro intenso.", "precio": 10.00, "categoria": "Pestañas"},
    
    # Iluminadores
    {"nombre": "Dior Backstage Glow Maximizer Palette", "descripcion": "Paleta de iluminadores rostro y cuerpo.", "precio": 45.00, "categoria": "Iluminadores"},
    {"nombre": "Charlotte Tilbury Beauty Light Wand", "descripcion": "Iluminador en barra con aplicador en cojín tono Pillow Talk.", "precio": 38.00, "categoria": "Iluminadores"},
    {"nombre": "Iluminador Líquido Positive Light - Rare Beauty", "descripcion": "Iluminador líquido luminoso y duradero.", "precio": 28.00, "categoria": "Iluminadores"},
    
    # Rubores
    {"nombre": "Sheglam Jelly-Licious Hydrating Lip & Blush", "descripcion": "Tinta hidratante en gel para labios y mejillas.", "precio": 9.00, "categoria": "Rubores"},
    {"nombre": "Elf Camo Liquid Blush", "descripcion": "Rubor líquido de alta pigmentación y acabado suave.", "precio": 7.00, "categoria": "Rubores"},
    {"nombre": "Rubor Líquido Soft Pinch - Rare Beauty", "descripcion": "Rubor líquido de larga duración acabado mate y luminoso.", "precio": 26.00, "categoria": "Rubores"},
    
    # Labiales y Gloss
    {"nombre": "Rhode Peptide Lip Tint", "descripcion": "Tratamiento y bálsamo labial con color e infusión de péptidos.", "precio": 22.00, "categoria": "Labiales"},
    {"nombre": "Gisou Honey Infused Lip Oil", "descripcion": "Aceite labial hidratante con infusión de miel.", "precio": 30.00, "categoria": "Labiales"},
    {"nombre": "Dior Addict Lip Maximizer", "descripcion": "Brillo labial efecto volumen hidratante.", "precio": 40.00, "categoria": "Labiales"},
    
    # Cuidado Facial y Protectores Solares
    {"nombre": "Beauty of Joseon Ginseng Moist Sun Serum", "descripcion": "Protector solar en suero con extracto de ginseng SPF50+ PA++++.", "precio": 24.00, "categoria": "Cuidado Facial"},
    {"nombre": "Tocobo Bio Watery Sun Cream", "descripcion": "Protector solar hidratante con extracto de judía mungo.", "precio": 23.00, "categoria": "Cuidado Facial"},
    
    # Cuerpo y Perfumes
    {"nombre": "Crema Corporal Victoria's Secret Coconut Passion", "descripcion": "Crema hidratante corporal perfumada.", "precio": 18.00, "categoria": "Cuerpo"},
    {"nombre": "Spray Sol de Janeiro Cheirosa 68", "descripcion": "Mist perfumado para cuerpo y cabello.", "precio": 35.00, "categoria": "Cuerpo"},
]

# Guardar en la base de datos
for item in productos_catalogo:
    Producto.objects.get_or_create(
        nombre=item["nombre"],
        defaults={
            "descripcion": item["descripcion"],
            "precio": item["precio"],
            "categoria": item["categoria"]
        }
    )

print("¡Catálogo de maquillaje cargado con éxito en la base de datos!")