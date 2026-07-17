/*
Ejemplo: Construir un PIN bancario seguro con generadores de números aleatorios
 
Qué enseña este ejemplo:
  - Cómo usar el crate 'rand' para generar aleatoriedad criptográficamente segura (rand usa el OS RNG por defecto en thread_rng())
  - Cómo estructurar strings de constantes y mezclarlas
  - Cómo garantizar que el resultado incluya al menos un carácter de cada tipo
 
Para tu reto (generador de contraseñas):
  Aplica el mismo patrón: construye el pool de caracteres según los
  parámetros del usuario (longitud, símbolos sí/no, mayúsculas sí/no),
  y usa el RNG para construir la contraseña.
 
Glosario:
  rand::thread_rng() — obtiene el generador de números aleatorios seguro local
  slice::choose()    — selecciona un elemento aleatorio de una lista
  slice::shuffle()   — mezcla los elementos de una lista
*/

use rand::seq::SliceRandom;

const DIGITOS: &[u8] = b"0123456789";
const MAYUSCULAS: &[u8] = b"ABCDEFGHIJKLMNOPQRSTUVWXYZ";
const SIMBOLOS: &[u8] = b"!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~";

fn generar_pin(longitud: usize, solo_numeros: bool) -> String {
    let mut rng = rand::thread_rng();
    
    let mut pool = Vec::new();
    if solo_numeros {
        pool.extend_from_slice(DIGITOS);
    } else {
        pool.extend_from_slice(MAYUSCULAS);
        pool.extend_from_slice(DIGITOS);
    }

    let mut pin = String::with_capacity(longitud);
    for _ in 0..longitud {
        let ch = pool.choose(&mut rng).unwrap();
        pin.push(*ch as char);
    }
    pin
}

fn generar_pin_garantizado(longitud: usize) -> String {
    if longitud < 3 {
        panic!("La longitud mínima para un PIN garantizado es 3.");
    }

    let mut rng = rand::thread_rng();
    
    let mut pool_completo = Vec::new();
    pool_completo.extend_from_slice(MAYUSCULAS);
    pool_completo.extend_from_slice(DIGITOS);
    pool_completo.extend_from_slice(SIMBOLOS);

    let mut caracteres = Vec::new();
    
    // 1. Garantizar
    caracteres.push(*MAYUSCULAS.choose(&mut rng).unwrap());
    caracteres.push(*DIGITOS.choose(&mut rng).unwrap());
    caracteres.push(*SIMBOLOS.choose(&mut rng).unwrap());

    // 2. Rellenar
    for _ in 3..longitud {
        caracteres.push(*pool_completo.choose(&mut rng).unwrap());
    }

    // 3. Mezclar
    caracteres.shuffle(&mut rng);

    // Convertir de bytes a String
    caracteres.iter().map(|&b| *b as char).collect()
}

fn main() {
    println!("=== Generador de PINs seguros ===\n");

    println!("PINs numéricos (6 dígitos):");
    for _ in 0..3 {
        println!("  {}", generar_pin(6, true));
    }

    println!("\nPINs alfanuméricos (8 caracteres):");
    for _ in 0..3 {
        println!("  {}", generar_pin(8, false));
    }

    println!("\nPINs con garantía (letra + dígito + símbolo, 10 chars):");
    for _ in 0..3 {
        println!("  {}", generar_pin_garantizado(10));
    }
}
