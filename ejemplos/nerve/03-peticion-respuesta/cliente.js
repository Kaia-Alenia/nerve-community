const { NexusClient } = require('nerve');

class ClientePeticion {
    constructor() {
        this.cliente = new NexusClient();
        this.respuestaRecibida = null;
    }

    manejarRespuesta = (mensajeCrudo) => {
        const payload = mensajeCrudo.payload || {};
        const accion = payload.accion;

        if (accion === "respuesta_operacion") {
            this.respuestaRecibida = payload.resultado;
            console.log(`✅ ¡El servidor respondió! El resultado es: ${this.respuestaRecibida}`);
        }
    }

    async iniciar() {
        await this.cliente.connect("cliente_calculadora");
        this.cliente.listen(this.manejarRespuesta);

        console.log("Enviando petición de suma al servidor (5 + 7)...");
        const peticion = { accion: "sumar", a: 5, b: 7 };
        this.cliente.send("servidor_calculadora", peticion);

        let tiempoEspera = 0;
        while (this.respuestaRecibida === null && tiempoEspera < 5) {
            console.log("⏳ Esperando respuesta...");
            await new Promise(r => setTimeout(r, 1000));
            tiempoEspera++;
        }

        if (this.respuestaRecibida === null) {
            console.log("❌ Tiempo de espera agotado. El servidor no contestó.");
        }

        this.cliente.disconnect();
    }
}

if (require.main === module) {
    const app = new ClientePeticion();
    app.iniciar();
}
