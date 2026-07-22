const { NexusClient } = require('nerve');

async function main() {
    console.log("Iniciando publicador (estación de radio)...");
    const cliente = new NexusClient();
    await cliente.connect("publicador_noticias");
    console.log("✅ Publicador conectado al Hub.");

    let contador = 1;
    
    // Función para transmitir continuamente
    const intervalId = setInterval(() => {
        const noticia = {
            canal: "noticias_tech",
            titular: `Noticia #${contador}: Nerve Hub funciona genial`,
            timestamp: Date.now()
        };

        console.log(` Transmitiendo (broadcast): ${noticia.titular}`);
        cliente.broadcast(noticia);
        
        contador++;
    }, 3000);

    process.on('SIGINT', () => {
        console.log("\nApagando publicador...");
        clearInterval(intervalId);
        cliente.disconnect();
        process.exit();
    });
}

if (require.main === module) {
    main();
}
