/**
 * Ejemplo: Servidor HTTP con Express
 * 
 * Qué enseña este ejemplo:
 *   - Crear una aplicación básica de Express.
 *   - Configurar `express.json()` para parsear el cuerpo de las peticiones.
 *   - Crear un endpoint (ruta) POST que lea esos datos.
 * 
 * Para tu reto (Puente HTTP para Nerve):
 *   Cuando el endpoint reciba los datos, deberás usar el cliente Nerve 
 *   para retransmitir la información hacia el hub de Nerve.
 */

const express = require('express');

// 1. Inicializar la aplicación
const app = express();
const puerto = 3000;

// 2. Middleware para poder leer JSON en el cuerpo (body) del POST
app.use(express.json());

// 3. Ruta GET básica
app.get('/', (req, res) => {
    res.json({ status: "Servidor funcionando" });
});

// 4. Ruta POST que será nuestro "puente"
app.post('/enviar', (req, res) => {
    // req.body contendrá el JSON que nos envíen (ej. {"mensaje": "Hola"})
    const mensaje = req.body.mensaje;

    if (!mensaje) {
        return res.status(400).json({ error: "Falta el campo 'mensaje' en el JSON" });
    }

    // En la terminal veremos lo que llegó
    console.log(`📩 Recibido por HTTP: ${mensaje}`);

    // ¡Aquí es donde integrarías Nerve! 
    // Ejemplo: clienteNerve.publicar("canal_http", mensaje);

    // Responder a quien hizo la petición HTTP que todo salió bien
    res.json({ status: "ok", recibido: mensaje });
});

// 5. Encender el servidor
app.listen(puerto, () => {
    console.log(`Servidor Express escuchando en http://localhost:${puerto}`);
});
