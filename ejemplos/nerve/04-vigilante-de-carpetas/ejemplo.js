/**
 * Ejemplo: Monitoreo de carpeta con fs.watch en Node.js
 * 
 * Qué enseña este ejemplo:
 *   - Cómo usar el módulo nativo `fs` para vigilar cambios (fs.watch).
 *   - Cómo manejar eventos asíncronos y callbacks en Node.js.
 * 
 * Para tu reto (Vigilante de carpetas con Nerve):
 *   Aplica esta misma estructura. En vez de solo hacer `console.log`, cuando se
 *   detecte un cambio, usarás tu cliente de Nerve para notificar a otros nodos.
 * 
 * Glosario de funciones:
 *   fs.mkdirSync  — Crea una carpeta de forma síncrona (bloqueando la ejecución hasta que termine).
 *   recursive     — Opción para que mkdirSync cree también carpetas intermedias si no existen.
 *   fs.watch      — Inicia la vigilancia sobre un directorio o archivo. Retorna un objeto "watcher".
 *   eventType     — El tipo de evento detectado por fs.watch (generalmente 'rename' o 'change').
 *                   'rename' ocurre al crear o eliminar, 'change' al modificar.
 */

const fs = require('fs');
const path = require('path');

const carpetaAVigilar = path.join(__dirname, 'carpeta_prueba');

// Creamos la carpeta si no existe
if (!fs.existsSync(carpetaAVigilar)) {
    fs.mkdirSync(carpetaAVigilar, { recursive: true });
    console.log(`Carpeta creada: ${carpetaAVigilar}`);
}

console.log(`👀 Vigilando la carpeta '${carpetaAVigilar}'...`);
console.log("Crea, modifica o elimina archivos ahí para ver los eventos. Presiona Ctrl+C para salir.");

// fs.watch es nativo de Node.js. No requiere instalar nada extra.
// Le pasamos la ruta de la carpeta, y un callback que se ejecutará cada vez que haya un evento.
const watcher = fs.watch(carpetaAVigilar, (eventType, filename) => {
    if (filename) {
        // En Node.js nativo, 'rename' suele significar creación o eliminación.
        // 'change' suele significar modificación del contenido.
        if (eventType === 'rename') {
            console.log(`📁 [CREADO/ELIMINADO] Archivo afectado: ${filename}`);
        } else if (eventType === 'change') {
            console.log(`✏️  [MODIFICADO] Archivo afectado: ${filename}`);
        }
    } else {
        console.log('filename no proporcionado');
    }
});

// Manejo de errores
watcher.on('error', (error) => {
    console.error('❌ Error en el observador:', error);
});
