/**
 * Ejemplo: Mini gestor de contactos con menú interactivo y persistencia JSON en Node.js
 * 
 * Qué enseña este ejemplo:
 *   - Cómo leer entrada del usuario en la terminal (readline)
 *   - Cómo leer y escribir archivos de forma síncrona (fs.readFileSync / fs.writeFileSync)
 *   - Cómo convertir JSON de texto a objetos y viceversa (JSON.parse / JSON.stringify)
 *   - Cómo manejar arrays y modificar sus elementos
 * 
 * Glosario de términos "raros":
 *   fs             — (File System) Módulo nativo de Node.js para trabajar con archivos.
 *   readline       — Módulo nativo para leer lo que el usuario escribe en la consola.
 *   JSON.parse     — Convierte un texto JSON en un objeto o array de JavaScript.
 *   JSON.stringify — Convierte un objeto o array de JavaScript a texto JSON.
 *   utf8           — Formato de texto estándar (soporta acentos, ñ, etc.).
 */

const fs = require('fs');
const readline = require('readline');

const ARCHIVO = 'contactos.json';

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

// En Node.js clásico, preguntar algo por consola es asíncrono con callbacks o promesas.
// Usaremos una pequeña función de ayuda para usar promesas y async/await:
function preguntar(texto) {
    return new Promise((resolve) => {
        rl.question(texto, resolve);
    });
}

function cargarContactos() {
    if (!fs.existsSync(ARCHIVO)) {
        return [];
    }
    const data = fs.readFileSync(ARCHIVO, 'utf8');
    return JSON.parse(data);
}

function guardarContactos(contactos) {
    // stringify(obj, null, 4) formatea el JSON con 4 espacios
    fs.writeFileSync(ARCHIVO, JSON.stringify(contactos, null, 4), 'utf8');
}

function mostrarContactos(contactos) {
    if (contactos.length === 0) {
        console.log("No hay contactos guardados todavía.");
        return;
    }
    console.log("\n--- Tus contactos ---");
    contactos.forEach((contacto, index) => {
        console.log(`  ${index + 1}. ${contacto.nombre} — ${contacto.telefono}`);
    });
}

async function agregarContacto(contactos) {
    const nombre = (await preguntar("Nombre: ")).trim();
    const telefono = (await preguntar("Teléfono: ")).trim();
    
    if (nombre) {
        contactos.push({ nombre, telefono });
        guardarContactos(contactos);
        console.log(`✓ Contacto '${nombre}' guardado.`);
    } else {
        console.log("El nombre no puede estar vacío.");
    }
}

async function actualizarContacto(contactos) {
    mostrarContactos(contactos);
    if (contactos.length === 0) return;

    const idxStr = await preguntar("\nNúmero del contacto a actualizar: ");
    const idx = parseInt(idxStr) - 1;

    if (idx >= 0 && idx < contactos.length) {
        const nuevoTel = (await preguntar("Nuevo teléfono: ")).trim();
        contactos[idx].telefono = nuevoTel;
        guardarContactos(contactos);
        console.log("✓ Contacto actualizado.");
    } else {
        console.log("Número inválido.");
    }
}

async function eliminarContacto(contactos) {
    mostrarContactos(contactos);
    if (contactos.length === 0) return;

    const idxStr = await preguntar("\nNúmero del contacto a eliminar: ");
    const idx = parseInt(idxStr) - 1;

    if (idx >= 0 && idx < contactos.length) {
        const eliminado = contactos.splice(idx, 1)[0];
        guardarContactos(contactos);
        console.log(`✓ Contacto '${eliminado.nombre}' eliminado.`);
    } else {
        console.log("Número inválido.");
    }
}

async function main() {
    let contactos = cargarContactos();

    while (true) {
        console.log("\n=== Gestor de Contactos ===");
        console.log("1. Ver contactos");
        console.log("2. Agregar contacto");
        console.log("3. Actualizar teléfono");
        console.log("4. Eliminar contacto");
        console.log("5. Salir");

        const opcion = (await preguntar("\nElige una opción (1-5): ")).trim();

        if (opcion === "1") {
            mostrarContactos(contactos);
        } else if (opcion === "2") {
            await agregarContacto(contactos);
        } else if (opcion === "3") {
            await actualizarContacto(contactos);
        } else if (opcion === "4") {
            await eliminarContacto(contactos);
        } else if (opcion === "5") {
            console.log("¡Hasta luego!");
            break;
        } else {
            console.log("Opción no reconocida, intenta de nuevo.");
        }
    }
    rl.close();
}

main();
