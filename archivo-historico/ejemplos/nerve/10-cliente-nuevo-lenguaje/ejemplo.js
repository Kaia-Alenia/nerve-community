/**
 * Ejemplo: Cliente de Socket TCP en Node.js (net)
 * 
 * Qué enseña este ejemplo:
 *   - Conectarse a un servidor usando el módulo `net` de Node.js.
 *   - Manejar eventos (connect, data, error, close).
 *   - Enviar y recibir strings JSON (Node.js maneja la codificación a Buffer por ti).
 * 
 * Para tu reto (Nuevo Cliente Nerve):
 *   La naturaleza orientada a eventos de Node.js (client.on) es perfecta para
 *   Nerve, ya que puedes escuchar 'data' de forma permanente y emitir eventos
 *   propios (usando EventEmitter) cuando lleguen mensajes de otros clientes.
 */

const net = require('net');

function main() {
    const host = '127.0.0.1';
    const puerto = 5000;

    console.log(`🔄 Conectando a ${host}:${puerto}...`);

    // 1. Crear la conexión TCP
    const client = new net.Socket();

    // 2. Intentar conectar
    client.connect(puerto, host, () => {
        console.log('✅ Conectado exitosamente');

        // 3. Preparar el payload
        const payload = {
            tipo: "publicar",
            canal: "test",
            contenido: "Hola desde el nuevo cliente JS!"
        };

        // 4. Enviar los datos convertidos a JSON String + salto de línea
        const datosStr = JSON.stringify(payload) + "\n";
        client.write(datosStr);
        console.log(`⬆️ Enviado: ${datosStr.trim()}`);
    });

    // 5. Escuchar el evento 'data' para recibir las respuestas del servidor
    client.on('data', (data) => {
        // data es un Buffer, al llamar .toString() lo convertimos a String
        const respuesta = data.toString().trim();
        console.log(`⬇️ Recibido: ${respuesta}`);
        
        // En este ejemplo simple, cerramos la conexión luego de recibir respuesta.
        // ¡En tu cliente Nerve querrás mantenerla abierta!
        client.destroy(); 
    });

    // Manejar errores (como si el servidor no está encendido)
    client.on('error', (err) => {
        if (err.code === 'ECONNREFUSED') {
            console.log('❌ No se pudo conectar. ¿Está el servidor encendido?');
        } else {
            console.log(`❌ Error: ${err.message}`);
        }
    });

    // Saber cuándo se cerró la conexión
    client.on('close', () => {
        console.log('🔌 Conexión cerrada');
    });
}

main();
