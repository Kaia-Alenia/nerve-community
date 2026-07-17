/**
 * Ejemplo: Mini juego "adivina el color" con Math.random, bucle y conteo de intentos
 * 
 * Qué enseña este ejemplo:
 *   - Cómo usar Math.random() para seleccionar un elemento al azar de un array
 *   - Cómo estructurar el bucle de intentos con while + contador
 *   - Cómo dar pistas simples (mayor/menor en números, aquí: letra inicial)
 *   - Cómo manejar input no válido con validación condicional
 * 
 * Para tu reto (adivina el número):
 *   Aplica el mismo patrón de bucle + contador + pistas,
 *   pero usa Math.floor(Math.random() * 100) + 1 para generar un número
 *   y compara si el intento es mayor o menor al número secreto.
 * 
 * Glosario:
 *   Math.random()             — Genera un número decimal entre 0 (incluido) y 1 (excluido)
 *   Math.floor()              — Redondea hacia abajo al entero más cercano
 *   .toLowerCase()            — Convierte un string a minúsculas (útil para comparar)
 *   .trim()                   — Elimina espacios al inicio y final del string
 *   readline                  — Módulo de Node.js para leer entrada desde la terminal
 */

const readline = require('readline');

const COLORES = ["rojo", "azul", "verde", "amarillo", "morado", "naranja"];
const MAX_INTENTOS = 4;

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

// prompt que devuelve una promesa para facilitar el uso asíncrono
const input = (pregunta) => new Promise(resolve => rl.question(pregunta, resolve));

async function jugar() {
    // Math.random() junto con Math.floor() para elegir un índice al azar
    const indiceAleatorio = Math.floor(Math.random() * COLORES.length);
    const colorSecreto = COLORES[indiceAleatorio];
    let intentos = 0;

    console.log("=== Adivina el color ===");
    console.log(`Tengo un color en mente. Tienes ${MAX_INTENTOS} intentos.`);
    console.log(`Opciones posibles: ${COLORES.join(', ')}\n`);

    while (intentos < MAX_INTENTOS) {
        const respuesta = await input(`Intento ${intentos + 1}/${MAX_INTENTOS}: `);
        const intento = respuesta.trim().toLowerCase();

        // Validar que el input sea uno de los colores válidos
        if (!COLORES.includes(intento)) {
            console.log(`'${intento}' no es un color válido. Elige de la lista.\n`);
            continue; // No contamos este como un intento fallido
        }

        intentos++;

        if (intento === colorSecreto) {
            console.log(`\n¡Correcto! Era '${colorSecreto}'. Lo lograste en ${intentos} intento(s).`);
            rl.close();
            return;
        }

        // Pista: comparar letra inicial (equivalente a mayor/menor en números)
        if (intento[0] < colorSecreto[0]) {
            console.log(`No es '${intento}'. El color secreto va después alfabéticamente.`);
        } else {
            console.log(`No es '${intento}'. El color secreto va antes alfabéticamente.`);
        }
        console.log();
    }

    console.log(`\nSe acabaron los intentos. El color era '${colorSecreto}'.`);
    rl.close();
}

if (require.main === module) {
    jugar();
}
