/**
 * Ejemplo: Concurrencia con Promise.all en JavaScript
 * 
 * Qué enseña este ejemplo:
 *   - Usar `Promise.all` para ejecutar múltiples promesas concurrentemente.
 *   - Medir el tiempo usando `performance.now()`.
 * 
 * Para tu reto (Probador de Carga Nerve):
 *   Reemplazarás `simularPeticion()` con llamadas al cliente Nerve
 *   (como publicar mensajes) para medir cuántas peticiones aguanta la red
 *   por segundo.
 */

// Función auxiliar para simular un retraso sin bloquear el hilo principal
const setTimeoutAsync = (ms) => new Promise(resolve => setTimeout(resolve, ms));

// 1. Definir una tarea asíncrona que simula trabajo
async function simularPeticion(idPeticion) {
    // Simulamos que enviar un mensaje tarda 100 milisegundos (0.1s)
    await setTimeoutAsync(100);
    // Retornamos true si fue exitoso (o podríamos hacer un try/catch)
    return true;
}

async function main() {
    const totalMensajes = 1000;
    console.log(`🚀 Iniciando prueba de carga: ${totalMensajes} peticiones...`);

    // Guardar el tiempo de inicio (más preciso que Date.now())
    const inicio = performance.now();

    // 2. Crear un arreglo (array) con todas las promesas (las peticiones ejecutándose)
    const promesas = [];
    for (let i = 0; i < totalMensajes; i++) {
        // Al llamar a la función sin `await`, comienza a ejecutarse
        // pero no esperamos a que termine, solo guardamos la promesa
        promesas.push(simularPeticion(i));
    }

    // 3. Promise.all espera a que TODAS las promesas terminen en paralelo
    const resultados = await Promise.all(promesas);

    // Calcular el tiempo total transcurrido
    const fin = performance.now();
    // Convertir de milisegundos a segundos
    const tiempoTotal = (fin - inicio) / 1000;

    // Contar cuántos retornaron `true`
    const exitosos = resultados.filter(r => r === true).length;
    
    // 4. Mostrar estadísticas
    console.log(`✅ Prueba finalizada en ${tiempoTotal.toFixed(2)} segundos.`);
    console.log(`📊 Mensajes exitosos: ${exitosos}/${totalMensajes}`);
    console.log(`⚡ Rendimiento: ${(totalMensajes / tiempoTotal).toFixed(2)} peticiones/segundo`);
}

main();
