/**
 * Ejemplo: Dibujar una barra de progreso con Jimp (Node.js)
 * 
 * Qué enseña este ejemplo:
 *   - Cómo crear una imagen nueva programáticamente sin usar canvas nativo.
 *   - Cómo manipular píxeles directamente o usar plugins de Jimp.
 *   - Cómo guardar una imagen asíncronamente.
 * 
 * Para tu reto (Puente de progreso GIF con Nerve):
 *   En lugar de un porcentaje fijo, tu receptor de Nerve recibirá actualizaciones
 *   (ej. 10%, 20%), y con cada actualización dibujarás la barra correspondiente 
 *   y guardarás la imagen.
 * 
 * Glosario:
 *   new Jimp(ancho, alto, color) — Instancia una imagen nueva con fondo sólido.
 *   image.scan()                 — Recorre los píxeles de un área para modificarlos.
 *   image.writeAsync()           — Guarda la imagen generada (devuelve una promesa).
 */

const Jimp = require('jimp');

async function generarBarraProgreso(porcentaje, rutaSalida) {
    const ancho = 400;
    const alto = 50;

    // Aseguramos que el porcentaje esté entre 0 y 100
    const p = Math.max(0, Math.min(100, porcentaje));
    
    // Calculamos el ancho de la barra verde
    const anchoProgreso = Math.floor((p / 100) * ancho);

    // 1. Creamos el lienzo base (fondo gris claro en Hexadecimal)
    // 0xDDDDDDFF = R: 221, G: 221, B: 221, Alpha: 255 (sólido)
    const imagen = new Jimp(ancho, alto, 0xddddddff);

    // 2. Coloreamos la porción correspondiente a la barra de progreso
    // Jimp no tiene una función nativa de dibujar rectángulos sin plugins,
    // pero podemos hacerlo fácilmente modificando los píxeles del área deseada.
    // El color verde lima es 0x32CD32FF
    const colorVerde = 0x32cd32ff;

    imagen.scan(0, 0, anchoProgreso, alto, function (x, y, idx) {
        // En lugar de acceder a los bytes, escribimos el color hexadecimal completo
        this.setPixelColor(colorVerde, x, y);
    });

    // 3. Guardamos la imagen (es una operación asíncrona)
    try {
        await imagen.writeAsync(rutaSalida);
        console.log(`✅ Imagen guardada en: ${rutaSalida} con un progreso de ${p}%`);
    } catch (error) {
        console.error("Error al guardar la imagen:", error);
    }
}

async function main() {
    console.log("Generando ejemplos de barras de progreso...\n");
    
    await generarBarraProgreso(25, "progreso_25.png");
    await generarBarraProgreso(75, "progreso_75.png");
    await generarBarraProgreso(100, "progreso_100.png");
    
    console.log("\nRevisa tu carpeta, deberías ver tres archivos .png nuevos.");
}

main();
