const { NexusClient } = require('nerve');

const nombreNodo = process.argv[2] || "suscriptor_default";

function alRecibirNoticia(mensajeCrudo) {
    const payload = mensajeCrudo.payload || {};

    if (payload.canal === "noticias_tech") {
        const titular = payload.titular || "Sin titular";
        console.log(`[${nombreNodo}]  Nueva noticia interceptada: ${titular}`);
    }
}

async function main() {
    console.log(`Iniciando ${nombreNodo}...`);
    const cliente = new NexusClient();
    
    await cliente.connect(nombreNodo);
    console.log(`✅ ${nombreNodo} conectado. Escuchando el canal 'noticias_tech'...`);

    cliente.listen(alRecibirNoticia);

    process.on('SIGINT', () => {
        console.log(`\nApagando ${nombreNodo}...`);
        cliente.disconnect();
        process.exit();
    });
}

if (require.main === module) {
    main();
}
