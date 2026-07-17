/*
 * Ejemplo: Dibujar una barra de progreso en Rust con el crate `image`
 * 
 * Qué enseña este ejemplo:
 *   - Cómo usar el crate externo `image` para crear un lienzo.
 *   - Cómo manipular los píxeles de una imagen usando bucles `for`.
 *   - Cómo guardar una imagen en disco.
 * 
 * Para tu reto (Puente de progreso GIF con Nerve):
 *   En lugar de un porcentaje fijo, tu receptor de Nerve recibirá actualizaciones
 *   (ej. 10%, 20%), y con cada actualización dibujarás la barra correspondiente 
 *   y guardarás la imagen.
 * 
 * Glosario:
 *   RgbImage::new(w, h) — Crea un nuevo búfer de imagen RGB de ancho `w` y alto `h`.
 *   Rgb([r, g, b])      — Define un píxel con colores Rojo, Verde y Azul (0-255).
 *   put_pixel(x, y, c)  — Pinta el píxel en las coordenadas (x, y) con el color `c`.
 *   save(ruta)          — Guarda la imagen inferiendo el formato (ej. PNG) a partir de la extensión.
 */

use image::{Rgb, RgbImage};
use std::cmp;

fn generar_barra_progreso(porcentaje: i32, ruta_salida: &str) {
    let ancho = 400;
    let alto = 50;

    // Aseguramos que el porcentaje esté entre 0 y 100
    let p = cmp::max(0, cmp::min(100, porcentaje));
    
    // Calculamos el ancho de la barra
    let ancho_progreso = ((p as f32 / 100.0) * (ancho as f32)) as u32;

    // 1. Creamos la imagen base (RgbImage)
    let mut imagen = RgbImage::new(ancho, alto);

    let color_fondo = Rgb([220, 220, 220]); // Gris claro
    let color_barra = Rgb([50, 205, 50]);   // Verde lima

    // 2. Coloreamos la imagen iterando por los píxeles (x, y)
    for y in 0..alto {
        for x in 0..ancho {
            if x < ancho_progreso {
                // Si el píxel está dentro de la barra de progreso, lo pintamos verde
                imagen.put_pixel(x, y, color_barra);
            } else {
                // Si no, lo pintamos del color de fondo
                imagen.put_pixel(x, y, color_fondo);
            }
        }
    }

    // 3. Guardamos la imagen
    match imagen.save(ruta_salida) {
        Ok(_) => println!("✅ Imagen guardada en: {} con un progreso de {}%", ruta_salida, p),
        Err(e) => eprintln!("Error al guardar {}: {}", ruta_salida, e),
    }
}

fn main() {
    println!("Generando ejemplos de barras de progreso...\n");

    generar_barra_progreso(25, "progreso_25.png");
    generar_barra_progreso(75, "progreso_75.png");
    generar_barra_progreso(100, "progreso_100.png");

    println!("\nRevisa tu carpeta, deberías ver tres archivos .png nuevos.");
}
