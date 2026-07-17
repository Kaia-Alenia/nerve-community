/**
 * Ejemplo: Construir un PIN bancario seguro con criptografía
 * 
 * Qué enseña este ejemplo:
 *   - Cuándo usar crypto.randomInt en lugar de Math.random (y por qué importa)
 *   - Cómo definir listas de caracteres (alfabeto, números, símbolos)
 *   - Cómo garantizar que el resultado incluya al menos un carácter de cada tipo
 * 
 * Para tu reto (generador de contraseñas):
 *   Aplica el mismo patrón: construye el pool de caracteres según los
 *   parámetros del usuario (longitud, símbolos sí/no, mayúsculas sí/no),
 *   y usa selección criptográfica para construir la contraseña.
 * 
 * Glosario:
 *   crypto.randomInt(max) — Devuelve un entero aleatorio criptográficamente seguro entre 0 y max-1.
 *   Math.random()         — NO usar para contraseñas, es predecible.
 *   arreglo.push(item)    — Añade un elemento al final de un arreglo.
 *   arreglo.join('')      — Une los elementos de un arreglo en un solo texto.
 */

const crypto = require('crypto');

const DIGITOS = "0123456789";
const MAYUSCULAS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
const SIMBOLOS = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~";

// Función de ayuda para elegir un caracter seguro al azar
function choice(pool) {
    const indice = crypto.randomInt(pool.length);
    return pool[indice];
}

// Función de ayuda para mezclar un arreglo (Fisher-Yates con crypto)
function shuffle(arreglo) {
    for (let i = arreglo.length - 1; i > 0; i--) {
        const j = crypto.randomInt(i + 1);
        [arreglo[i], arreglo[j]] = [arreglo[j], arreglo[i]];
    }
}

function generarPin(longitud = 6, soloNumeros = true) {
    let pool;
    if (soloNumeros) {
        pool = DIGITOS;
    } else {
        pool = MAYUSCULAS + DIGITOS;
    }

    let pin = "";
    for (let i = 0; i < longitud; i++) {
        pin += choice(pool);
    }
    return pin;
}

function generarPinGarantizado(longitud = 8) {
    if (longitud < 3) {
        throw new Error("La longitud mínima para un PIN garantizado es 3.");
    }

    const poolCompleto = MAYUSCULAS + DIGITOS + SIMBOLOS;

    // 1. Garantizar al menos uno de cada tipo requerido
    const obligatorios = [
        choice(MAYUSCULAS),
        choice(DIGITOS),
        choice(SIMBOLOS)
    ];

    // 2. Rellenar el resto con caracteres aleatorios del pool completo
    const relleno = [];
    for (let i = 0; i < longitud - 3; i++) {
        relleno.push(choice(poolCompleto));
    }

    // 3. Unir todo y mezclar
    const caracteres = obligatorios.concat(relleno);
    shuffle(caracteres);

    return caracteres.join("");
}

if (require.main === module) {
    console.log("=== Generador de PINs seguros ===\n");

    console.log("PINs numéricos (6 dígitos):");
    for (let i = 0; i < 3; i++) {
        console.log(`  ${generarPin(6, true)}`);
    }

    console.log("\nPINs alfanuméricos (8 caracteres):");
    for (let i = 0; i < 3; i++) {
        console.log(`  ${generarPin(8, false)}`);
    }

    console.log("\nPINs con garantía (letra + dígito + símbolo, 10 chars):");
    for (let i = 0; i < 3; i++) {
        console.log(`  ${generarPinGarantizado(10)}`);
    }
}
