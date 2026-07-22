const { NexusClient } = require('nerve');

function procesarMensaje(mensajeCrudo) {
    // El servidor nos entrega el mensaje completo. Lo extraemos.
    console.log(` ¡Mensaje recibido!: ${JSON.stringify(mensajeCrudo)}`);

    // Podemos extraer el payload original si queremos
    const payload = mensajeCrudo.payload || {};
    if (payload.texto) {
        console.log(`Texto extraído: ${payload.texto}`);
    }
}

async function main() {
    console.log("Iniciando receptor...");
    const cliente = new NexusClient();

    // Nos conectamos como "receptor_01"
    await cliente.connect("receptor_01");
    console.log("✅ Receptor conectado. Esperando mensajes...");

    // Registramos la función que se llamará al recibir mensajes
    cliente.listen(procesarMensaje);

    // Mantenemos el programa vivo para escuchar
    process.on('SIGINT', () => {
        console.log("\nSaliendo...");
        cliente.disconnect();
        process.exit();
    });
}

if (require.main === module) {
    main();
}
