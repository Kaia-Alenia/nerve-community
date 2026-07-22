/**
 * Ejemplo: Escritura de Logs en Node.js
 * 
 * Qué enseña este ejemplo:
 *   - Cómo obtener la fecha y hora actual usando el objeto nativo `Date`.
 *   - Cómo formatear una fecha al estilo ISO o local.
 *   - Cómo añadir texto al final de un archivo usando `fs.appendFileSync` (modo append).
 * 
 * Para tu reto (Logger Distribuido con Nerve):
 *   En vez de llamar a `escribirLog` con datos estáticos, tu receptor de Nerve
 *   escuchará mensajes de otros nodos y llamará a tu función de log para 
 *   registrarlos en un archivo central.
 * 
 * Glosario:
 *   new Date()         — Crea un nuevo objeto de fecha con la fecha y hora actual.
 *   toISOString()      — Formatea la fecha al estándar ISO (ej: 2026-07-17T15:30:05.123Z).
 *   fs.appendFileSync  — Escribe en un archivo síncronamente agregando el texto al final. 
 *                        Si el archivo no existe, lo crea.
 */

const fs = require('fs');
const path = require('path');

// El archivo donde guardaremos los logs
const ARCHIVO_LOG = path.join(__dirname, 'sistema.log');

function escribirLog(nivel, mensaje) {
    // 1. Obtenemos el timestamp actual y lo formateamos
    // toISOString da un formato como "2026-07-17T15:30:05.123Z"
    // Reemplazamos la "T" por un espacio y quitamos los milisegundos y la Z final para que luzca mejor.
    const ahora = new Date();
    const timestampFormateado = ahora.toISOString().replace('T', ' ').substring(0, 19);

    // 2. Construimos la línea de log final
    // Ejemplo: [2026-07-17 15:30:05] [INFO] El servidor ha iniciado correctamente
    const lineaLog = `[${timestampFormateado}] [${nivel}] ${mensaje}\n`;

    // 3. Imprimimos en consola (opcional, para verlo en vivo)
    // Usamos process.stdout.write para evitar el salto de línea extra que pone console.log
    process.stdout.write(lineaLog);

    // 4. Escribimos en el archivo agregando al final (append)
    try {
        fs.appendFileSync(ARCHIVO_LOG, lineaLog, 'utf8');
    } catch (error) {
        console.error('Error al escribir en el archivo de log:', error);
    }
}

function main() {
    console.log(`Escribiendo logs en '${ARCHIVO_LOG}'...\n`);

    escribirLog("INFO", "Sistema iniciado.");
    escribirLog("DEBUG", "Conexión a la base de datos establecida en 14ms.");
    escribirLog("WARNING", "Poco espacio en disco (15% restante).");
    escribirLog("ERROR", "Fallo al procesar el archivo 'datos.csv': Archivo no encontrado.");
    escribirLog("INFO", "Apagando sistema de forma segura.");

    console.log(`\nRevisa el archivo '${ARCHIVO_LOG}' para ver los resultados guardados.`);
}

main();
