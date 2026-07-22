/**
 * Ejemplo: Concurrencia con Goroutines y WaitGroups en Go
 * 
 * Qué enseña este ejemplo:
 *   - Lanzar "goroutines" (hilos ligeros) usando la palabra clave `go`.
 *   - Sincronizar las goroutines usando un `sync.WaitGroup` para esperar a que todas terminen.
 *   - Medir el tiempo transcurrido usando `time.Since`.
 * 
 * Para tu reto (Probador de Carga Nerve):
 *   Reemplazarás `simularPeticion()` con un envío al servidor usando 
 *   tu cliente Nerve para ver cuánto tráfico puede aguantar tu red.
 */

package main

import (
	"fmt"
	"sync"
	"time"
)

// 1. Tarea que se ejecutará de forma concurrente
// Recibe un puntero al WaitGroup para avisar cuando termine
func simularPeticion(idPeticion int, wg *sync.WaitGroup) {
	// Importante: al terminar la función, avisa al WaitGroup
	defer wg.Done()

	// Simulamos que enviar un mensaje tarda 100 milisegundos (0.1s)
	time.Sleep(100 * time.Millisecond)

	// Aquí iría tu cliente Nerve: clienteNerve.Publicar(...)
}

func main() {
	totalMensajes := 1000
	fmt.Printf("🚀 Iniciando prueba de carga: %d peticiones...\n", totalMensajes)

	// Guardar el tiempo de inicio
	inicio := time.Now()

	// 2. Crear un WaitGroup para esperar a que todas las goroutines terminen
	var wg sync.WaitGroup

	// Decirle al WaitGroup cuántas tareas vamos a lanzar
	wg.Add(totalMensajes)

	// 3. Lanzar todas las tareas concurrentemente
	for i := 0; i < totalMensajes; i++ {
		// La palabra `go` lanza la función en un hilo ligero (goroutine)
		// y el bucle for sigue inmediatamente a la siguiente iteración
		go simularPeticion(i, &wg)
	}

	// 4. Pausar la ejecución principal hasta que el contador del WaitGroup llegue a cero
	wg.Wait()

	// Calcular el tiempo transcurrido
	tiempoTotal := time.Since(inicio).Seconds()

	// En este ejemplo simple asumimos que todas fueron exitosas
	// Para contar éxitos de forma segura en concurrencia necesitarías canales (channels) o sync.Mutex
	exitosos := totalMensajes

	// 5. Mostrar estadísticas
	fmt.Printf("✅ Prueba finalizada en %.2f segundos.\n", tiempoTotal)
	fmt.Printf("📊 Mensajes exitosos: %d/%d\n", exitosos, totalMensajes)
	fmt.Printf("⚡ Rendimiento: %.2f peticiones/segundo\n", float64(totalMensajes)/tiempoTotal)
}
