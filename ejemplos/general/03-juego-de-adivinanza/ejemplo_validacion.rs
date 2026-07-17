/*
Ejemplo: Mini juego "adivina el color" con rand, bucle y conteo de intentos

Qué enseña este ejemplo:
  - Cómo usar el crate rand (y slice::choose) para elegir un elemento al azar
  - Cómo estructurar el bucle de intentos con loop + contador
  - Cómo dar pistas simples (mayor/menor en números, aquí: letra inicial)
  - Cómo manejar input no válido con validación condicional

Para tu reto (adivina el número):
  Aplica el mismo patrón de bucle + contador + pistas,
  pero usa rand::thread_rng().gen_range(1..=100) para generar un número
  y compara si el intento es mayor o menor al número secreto.

Glosario:
  rand::thread_rng()    — obtiene el generador de números aleatorios local
  slice.choose(...)     — elige un elemento al azar de un arreglo o vector
  .trim()               — elimina espacios al inicio y final del string
  .to_lowercase()       — convierte un string a minúsculas
  std::io::stdin()      — la manera estándar de leer entrada en la consola
*/

use rand::seq::SliceRandom;
use std::io::{self, Write};

fn main() {
    let colores = ["rojo", "azul", "verde", "amarillo", "morado", "naranja"];
    let max_intentos = 4;

    // Obtener RNG (Random Number Generator)
    let mut rng = rand::thread_rng();
    
    // choose devuelve un Option, hacemos unwrap porque sabemos que el arreglo no está vacío
    let color_secreto = colores.choose(&mut rng).unwrap();
    let mut intentos = 0;

    println!("=== Adivina el color ===");
    println!("Tengo un color en mente. Tienes {} intentos.", max_intentos);
    println!("Opciones posibles: {}\n", colores.join(", "));

    while intentos < max_intentos {
        print!("Intento {}/{}: ", intentos + 1, max_intentos);
        io::stdout().flush().unwrap(); // Para que el print anterior se muestre antes del input

        let mut input = String::new();
        io::stdin()
            .read_line(&mut input)
            .expect("Error al leer la entrada");

        let intento = input.trim().to_lowercase();

        // Validar
        if !colores.contains(&intento.as_str()) {
            println!("'{}' no es un color válido. Elige de la lista.\n", intento);
            continue;
        }

        intentos += 1;

        if intento == *color_secreto {
            println!("\n¡Correcto! Era '{}'. Lo lograste en {} intento(s).", color_secreto, intentos);
            return;
        }

        // Pista: obtenemos el primer char
        let char_intento = intento.chars().next().unwrap();
        let char_secreto = color_secreto.chars().next().unwrap();

        if char_intento < char_secreto {
            println!("No es '{}'. El color secreto va después alfabéticamente.", intento);
        } else {
            println!("No es '{}'. El color secreto va antes alfabéticamente.", intento);
        }
        println!();
    }

    println!("\nSe acabaron los intentos. El color era '{}'.", color_secreto);
}
