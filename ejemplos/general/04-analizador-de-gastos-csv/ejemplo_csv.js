/**
 * Ejemplo: Leer un CSV real desde disco, filtrar y calcular sumas
 * 
 * Qué enseña este ejemplo:
 *   - Cómo abrir y leer un archivo CSV con el módulo fs de Node.js
 *   - Cómo procesar líneas de texto y dividirlas en columnas
 *   - Cómo convertir strings a números para operar con ellos
 *   - Cómo agrupar filas y calcular sumas / promedios
 * 
 * Para tu reto (analizador de gastos):
 *   Aplica el mismo patrón para leer tu CSV de gastos
 *   (fecha, categoría, monto) y calcular totales por categoría.
 * 
 * Glosario:
 *   fs.readFileSync(ruta) — Lee todo el contenido de un archivo a la memoria.
 *   "utf-8"               — Asegura que los caracteres especiales se decodifiquen como texto y no como un buffer binario.
 *   .split('\n')          — Divide un texto largo en una lista de líneas.
 *   .split(',')           — Divide una línea en columnas separadas por comas.
 *   parseFloat(valor)     — Convierte un texto como "1234.50" a un número decimal.
 */

const fs = require('fs');

function leerEmpleados(rutaCsv) {
    if (!fs.existsSync(rutaCsv)) {
        console.log(`Archivo no encontrado: ${rutaCsv}`);
        return [];
    }

    const contenido = fs.readFileSync(rutaCsv, 'utf-8');
    const lineas = contenido.trim().split('\n');
    
    // La primera línea son las cabeceras
    const empleados = [];
    
    for (let i = 1; i < lineas.length; i++) {
        const linea = lineas[i].trim();
        if (!linea) continue;
        
        const [nombre, departamento, salarioStr] = linea.split(',');
        
        empleados.push({
            nombre: nombre,
            departamento: departamento,
            salario: parseFloat(salarioStr)
        });
    }

    return empleados;
}

function reportePorDepartamento(empleados) {
    const totales = {};

    for (const emp of empleados) {
        const dept = emp.departamento;
        if (!totales[dept]) {
            totales[dept] = { suma: 0, cantidad: 0 };
        }
        totales[dept].suma += emp.salario;
        totales[dept].cantidad += 1;
    }

    console.log("\n--- Reporte por departamento ---");
    for (const [dept, datos] of Object.entries(totales)) {
        const promedio = datos.suma / datos.cantidad;
        console.log(`  ${dept}: total=$${datos.suma.toLocaleString()} | promedio=$${promedio.toLocaleString()} | empleados=${datos.cantidad}`);
    }
}

// Crear archivo de ejemplo si no existe
const archivo = "empleados.csv";
if (!fs.existsSync(archivo)) {
    const datos = [
        "nombre,departamento,salario",
        "Ana García,Ingeniería,35000",
        "Luis Martínez,Marketing,28000",
        "Carmen López,Ingeniería,42000",
        "Pedro Sánchez,Marketing,31000",
        "Sofía Ramírez,Ingeniería,39000"
    ];
    fs.writeFileSync(archivo, datos.join("\n"), "utf-8");
    console.log(`Archivo '${archivo}' creado de ejemplo.`);
}

const empleados = leerEmpleados(archivo);
console.log(`\nSe leyeron ${empleados.length} empleados.`);
reportePorDepartamento(empleados);
