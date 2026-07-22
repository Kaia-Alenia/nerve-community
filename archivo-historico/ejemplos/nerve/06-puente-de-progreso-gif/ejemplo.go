/*
 * Ejemplo: Dibujar una barra de progreso nativa en Go
 * 
 * Qué enseña este ejemplo:
 *   - Cómo usar la librería nativa de Go `image` y `image/draw`.
 *   - Cómo dibujar rectángulos en un lienzo RGBA.
 *   - Cómo codificar y guardar una imagen en formato PNG (image/png).
 * 
 * Para tu reto (Puente de progreso GIF con Nerve):
 *   En lugar de un porcentaje fijo, tu receptor de Nerve recibirá actualizaciones
 *   (ej. 10%, 20%), y con cada actualización dibujarás la barra correspondiente 
 *   y guardarás la imagen.
 * 
 * Glosario:
 *   image.NewRGBA()       — Crea una nueva imagen de un tamaño específico que soporta color.
 *   color.RGBA{}          — Define un color usando rojo, verde, azul y alpha (transparencia).
 *   draw.Draw()           — Copia una imagen/color sobre otra en un área específica.
 *   png.Encode()          — Escribe los datos de la imagen en formato PNG a un archivo.
 */

package main

import (
	"fmt"
	"image"
	"image/color"
	"image/draw"
	"image/png"
	"log"
	"os"
)

func generarBarraProgreso(porcentaje int, rutaSalida string) {
	ancho := 400
	alto := 50

	// Aseguramos que el porcentaje esté entre 0 y 100
	if porcentaje < 0 {
		porcentaje = 0
	} else if porcentaje > 100 {
		porcentaje = 100
	}

	// Calculamos el ancho de la barra
	anchoProgreso := int((float64(porcentaje) / 100.0) * float64(ancho))

	// 1. Definimos los colores
	colorFondo := color.RGBA{220, 220, 220, 255} // Gris claro
	colorBarra := color.RGBA{50, 205, 50, 255}   // Verde lima

	// 2. Creamos el lienzo (la imagen base)
	// image.Rect(x0, y0, x1, y1) define los límites
	lienzo := image.NewRGBA(image.Rect(0, 0, ancho, alto))

	// 3. Llenamos todo el lienzo con el color de fondo
	// draw.Src significa que reemplazará el pixel completamente
	draw.Draw(lienzo, lienzo.Bounds(), &image.Uniform{colorFondo}, image.Point{}, draw.Src)

	// 4. Dibujamos el rectángulo de progreso
	// Creamos un rectángulo que va desde (0,0) hasta (anchoProgreso, alto)
	rectProgreso := image.Rect(0, 0, anchoProgreso, alto)
	draw.Draw(lienzo, rectProgreso, &image.Uniform{colorBarra}, image.Point{}, draw.Src)

	// 5. Guardamos la imagen en un archivo
	archivo, err := os.Create(rutaSalida)
	if err != nil {
		log.Printf("Error al crear el archivo %s: %v", rutaSalida, err)
		return
	}
	defer archivo.Close()

	if err := png.Encode(archivo, lienzo); err != nil {
		log.Printf("Error al codificar PNG: %v", err)
		return
	}

	fmt.Printf("✅ Imagen guardada en: %s con un progreso de %d%%\n", rutaSalida, porcentaje)
}

func main() {
	fmt.Println("Generando ejemplos de barras de progreso...\n")

	generarBarraProgreso(25, "progreso_25.png")
	generarBarraProgreso(75, "progreso_75.png")
	generarBarraProgreso(100, "progreso_100.png")

	fmt.Println("\nRevisa tu carpeta, deberías ver tres archivos .png nuevos.")
}
