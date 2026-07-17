/**
 * Ejemplo: Extraer múltiples elementos de una página web en Node.js
 * 
 * Qué enseña este ejemplo:
 *   - Cómo hacer una petición HTTP GET con fetch nativo de Node.js
 *   - Cómo usar cheerio (el jQuery para Node) para analizar HTML
 *   - Cómo buscar elementos y extraer su texto
 *   - Cómo manejar errores de red con try/catch
 * 
 * Para tu reto (web scraper):
 *   Aplica este patrón pero apuntando a books.toscrape.com
 *   Instala dependencias con: npm install cheerio
 * 
 * Glosario de términos "raros":
 *   fetch    — Función nativa para hacer peticiones web.
 *   cheerio  — Librería que permite manipular HTML en Node.js de forma muy rápida usando selectores CSS.
 *   $        — Símbolo tradicional para instanciar cheerio (convención heredada de jQuery).
 *   .each()  — Método de cheerio para iterar sobre todos los elementos encontrados.
 *   .text()  — Extrae solo el contenido de texto (limpio de etiquetas HTML).
 */

const fs = require('fs');
const cheerio = require('cheerio'); // Requiere: npm install cheerio

const URL = "https://quotes.toscrape.com/";

async function obtenerFrases() {
    try {
        // 1. Hacer la petición GET a la página
        const respuesta = await fetch(URL);
        
        // 2. Verificar si la respuesta fue exitosa (código 200)
        if (!respuesta.ok) {
            throw new Error(`HTTP Error: ${respuesta.status}`);
        }

        // 3. Obtener el HTML como texto plano
        const html = await respuesta.text();

        // 4. Crear el objeto cheerio para navegar el HTML
        const $ = cheerio.load(html);

        // 5. Buscar TODOS los elementos con class="quote"
        const elementos = $(".quote");
        console.log(`Se encontraron ${elementos.length} frases en la página.\n`);

        const datosExtraidos = [];

        // .each() itera sobre cada elemento encontrado
        elementos.each((index, elemento) => {
            // Buscamos dentro de cada bloque individual
            const texto = $(elemento).find(".text").text();
            const autor = $(elemento).find(".author").text();
            
            datosExtraidos.push({ texto, autor });
            console.log(`"${texto}"`);
            console.log(`  — ${autor}\n`);
        });

        // 6. Guardar los datos en un archivo CSV simple
        let csvContent = "texto,autor\n"; // Cabeceras
        for (const dato of datosExtraidos) {
            // Limpiamos comas para no romper el CSV simple
            const textoLimpio = dato.texto.replace(/,/g, '');
            const autorLimpio = dato.autor.replace(/,/g, '');
            csvContent += `${textoLimpio},${autorLimpio}\n`;
        }
        
        fs.writeFileSync("frases.csv", csvContent, "utf8");
        console.log("✓ Datos guardados exitosamente en 'frases.csv'");

    } catch (error) {
        console.error("Error al obtener la página:", error.message);
    }
}

obtenerFrases();
