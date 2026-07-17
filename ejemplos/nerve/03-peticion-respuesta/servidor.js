const { NexusClient } = require('nerve');

class ServidorCalculadora {
    constructor() {
        this.cliente = new NexusClient();
    }

    atenderPeticion = (mensajeCrudo) => {
        const remitente = mensajeCrudo.from;
        const payload = mensajeCrudo.payload || {};
        const accion = payload.accion;

        if (accion === "sumar") {
            const a = payload.a || 0;
            const b = payload.b || 0;
            const resultado = a + b;

            console.log(` Solicitud de suma recibida de '${remitente}': ${a} + ${b} = ${resultado}`);

            const respuesta = { accion: "respuesta_operacion", resultado: resultado };
            console.log(`Enviando resultado a '${remitente}'...`);
            this.cliente.send(remitente, respuesta);
        }
    }

    async iniciar() {
        await this.cliente.connect("servidor_calculadora");
        console.log("✅ Servidor Calculadora en línea y esperando peticiones...");

        this.cliente.listen(this.atenderPeticion);

        process.on('SIGINT', () => {
            console.log("\nApagando servidor...");
            this.cliente.disconnect();
            process.exit();
        });
    }
}

if (require.main === module) {
    const app = new ServidorCalculadora();
    app.iniciar();
}
