const { NexusClient } = require('nerve');

async function main() {
    console.log("Iniciando emisor...");
    // 1. Crear el cliente de Nerve
    const cliente = new NexusClient();

    // 2. Conectarse al Hub con un identificador único
    await cliente.connect("emisor_01");
    console.log("✅ Emisor conectado al Nerve Hub.");

    // Esperamos un momento para asegurar que el receptor esté listo
    await new Promise(r => setTimeout(r, 1000));

    // 3. Preparar el mensaje (payload) y enviarlo al receptor
    const mensaje = { texto: "¡Hola, Nerve!", timestamp: Date.now() };

    console.log("Enviando mensaje a 'receptor_01'...");
    cliente.send("receptor_01", mensaje);

    console.log("Mensaje enviado. Terminando emisor...");
    // Desconectamos el cliente para liberar recursos
    cliente.disconnect();
}

if (require.main === module) {
    main();
}
