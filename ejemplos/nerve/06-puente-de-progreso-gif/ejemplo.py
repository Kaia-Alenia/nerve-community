"""
Ejemplo: Dibujar una barra de progreso con Pillow (Python)

Qué enseña este ejemplo:
  - Cómo crear una imagen desde cero.
  - Cómo dibujar formas geométricas (rectángulos) sobre la imagen.
  - Cómo guardar la imagen generada en el disco.

Para tu reto (Puente de progreso GIF con Nerve):
  En lugar de un porcentaje fijo, tu receptor de Nerve recibirá actualizaciones
  (ej. 10%, 20%), y con cada actualización dibujarás la barra correspondiente 
  y guardarás la imagen para que una página web u otro cliente pueda verla.

Glosario:
  Image.new()      — Crea un lienzo en blanco. Pide el modo ("RGB"), tamaño (ancho, alto) y color de fondo.
  ImageDraw.Draw() — Crea un objeto que permite dibujar sobre la imagen.
  draw.rectangle() — Dibuja un rectángulo dadas las coordenadas [x0, y0, x1, y1] y un color.
"""

from PIL import Image, ImageDraw

def generar_barra_progreso(porcentaje: int, ruta_salida: str):
    """
    Crea una imagen con una barra de progreso que representa el porcentaje dado.
    """
    # 1. Definimos dimensiones de la imagen
    ancho = 400
    alto = 50

    # 2. Creamos una nueva imagen con fondo gris claro
    color_fondo = (220, 220, 220)  # RGB
    imagen = Image.new("RGB", (ancho, alto), color_fondo)

    # 3. Preparamos el objeto para dibujar
    draw = ImageDraw.Draw(imagen)

    # 4. Calculamos el ancho de la barra verde (progreso)
    # Si porcentaje es 50, el ancho será el 50% de 400 = 200.
    porcentaje = max(0, min(100, porcentaje)) # Aseguramos que esté entre 0 y 100
    ancho_progreso = int((porcentaje / 100) * ancho)

    # 5. Dibujamos el rectángulo verde
    # Las coordenadas son [x_inicial, y_inicial, x_final, y_final]
    # Empieza en (0,0) y termina en (ancho_progreso, alto)
    color_barra = (50, 205, 50)  # Verde lima
    draw.rectangle([0, 0, ancho_progreso, alto], fill=color_barra)

    # 6. Guardamos la imagen
    imagen.save(ruta_salida)
    print(f"✅ Imagen guardada en: {ruta_salida} con un progreso de {porcentaje}%")

def main():
    print("Generando ejemplos de barras de progreso...\n")
    
    # Generamos tres imágenes distintas
    generar_barra_progreso(25, "progreso_25.png")
    generar_barra_progreso(75, "progreso_75.png")
    generar_barra_progreso(100, "progreso_100.png")
    
    print("\nRevisa tu carpeta, deberías ver tres archivos .png nuevos.")

if __name__ == "__main__":
    main()
