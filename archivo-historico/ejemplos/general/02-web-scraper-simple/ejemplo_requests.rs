// Ejemplo: Extraer múltiples elementos de una página web en Rust con reqwest + scraper
//
// Qué enseña este ejemplo:
//   - Cómo hacer una petición HTTP GET asíncrona con reqwest
//   - Cómo extraer datos del HTML usando la librería scraper
//   - Cómo escribir datos estructurados en un archivo CSV
//
// Para tu reto (web scraper):
//   Dependencias necesarias en Cargo.toml:
//   reqwest = { version = "0.11", features = ["blocking"] }
//   scraper = "0.18"
//   csv = "1.3"
//
// Glosario de términos "raros":
//   reqwest::blocking::get — Hace la petición web en modo "bloqueante" (espera a que termine).
//   scraper::Html::parse_document — Convierte el texto HTML a una estructura navegable.
//   scraper::Selector::parse — Prepara una regla CSS (ej: ".quote") para buscar elementos.
//   unwrap() — Atajo en Rust para "si hay error, explota el programa". Útil en scripts rápidos.
//   csv::Writer — Crea un escritor que se encarga de formatear correctamente las comas y comillas en el CSV.

use scraper::{Html, Selector};
use csv::Writer;
use std::error::Error;

const URL: &str = "https://quotes.toscrape.com/";

fn main() -> Result<(), Box<dyn Error>> {
    // 1. Hacer la petición GET (bloqueante)
    let respuesta = reqwest::blocking::get(URL)?;
    
    // 2. Verificar que la respuesta sea OK y extraer el HTML como texto
    let html = respuesta.error_for_status()?.text()?;

    // 3. Crear el objeto Html navegable
    let documento = Html::parse_document(&html);

    // 4. Preparar los selectores CSS
    // Selector::parse compila la regla. El unwrap() asume que escribiste bien la regla CSS.
    let selector_quote = Selector::parse(".quote").unwrap();
    let selector_text = Selector::parse(".text").unwrap();
    let selector_author = Selector::parse(".author").unwrap();

    let elementos = documento.select(&selector_quote).collect::<Vec<_>>();
    println!("Se encontraron {} frases en la página.\n", elementos.len());

    // 5. Preparar el escritor CSV
    let mut escritor = Writer::from_path("frases.csv")?;
    escritor.write_record(&["texto", "autor"])?; // Cabeceras

    // 6. Iterar sobre cada frase y extraer datos
    for elemento in elementos {
        // Encontramos el primer .text dentro del bloque
        let texto = elemento.select(&selector_text)
            .next()
            .map(|t| t.text().collect::<String>())
            .unwrap_or_default();
            
        // Encontramos el primer .author dentro del bloque
        let autor = elemento.select(&selector_author)
            .next()
            .map(|a| a.text().collect::<String>())
            .unwrap_or_default();

        println!("\"{}\"", texto);
        println!("  — {}\n", autor);

        // Guardamos la fila en el CSV (la librería csv maneja las comas internas automáticamente)
        escritor.write_record(&[&texto, &autor])?;
    }

    escritor.flush()?; // Asegurar que todo se escriba al disco
    println!("✓ Datos guardados exitosamente en 'frases.csv'");

    Ok(())
}
