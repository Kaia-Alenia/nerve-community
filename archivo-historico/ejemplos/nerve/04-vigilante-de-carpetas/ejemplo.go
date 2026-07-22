/*
 * Ejemplo: Monitoreo de carpeta con fsnotify en Go
 * 
 * Qué enseña este ejemplo:
 *   - Cómo usar un módulo externo de Go (github.com/fsnotify/fsnotify).
 *   - Cómo usar goroutines (go func) para ejecutar tareas en segundo plano.
 *   - Cómo usar un bucle for-select para leer eventos desde canales (channels).
 * 
 * Para tu reto (Vigilante de carpetas con Nerve):
 *   Aplica esta misma estructura. En vez de solo hacer `log.Println`, cuando se
 *   detecte un evento (ej. Create o Write), usarás el cliente de Nerve para 
 *   notificar a otros nodos.
 * 
 * Glosario de funciones/conceptos:
 *   fsnotify.NewWatcher()  — Crea un nuevo observador del sistema de archivos.
 *   defer watcher.Close()  — Asegura que el observador se cierre al terminar la función (limpieza).
 *   watcher.Add(path)      — Añade una ruta (archivo o carpeta) a la lista de vigilancia.
 *   <-watcher.Events       — Lee (recibe) datos del canal de eventos del observador. Bloquea hasta que haya uno.
 *   select                 — Permite a una goroutine esperar múltiples operaciones de comunicación (canales).
 */

package main

import (
	"log"
	"os"

	"github.com/fsnotify/fsnotify"
)

func main() {
	carpetaAVigilar := "./carpeta_prueba"

	// Creamos la carpeta si no existe (0755 son los permisos estándar de lectura/escritura/ejecución)
	if _, err := os.Stat(carpetaAVigilar); os.IsNotExist(err) {
		err = os.Mkdir(carpetaAVigilar, 0755)
		if err != nil {
			log.Fatal("Error al crear carpeta:", err)
		}
		log.Printf("Carpeta creada: %s\n", carpetaAVigilar)
	}

	// 1. Creamos un nuevo observador (watcher)
	watcher, err := fsnotify.NewWatcher()
	if err != nil {
		log.Fatal(err)
	}
	// defer asegura que los recursos se liberen al terminar main()
	defer watcher.Close()

	// 2. Iniciamos una goroutine (un hilo ligero en segundo plano)
	// que estará escuchando constantemente por eventos o errores.
	go func() {
		for {
			select {
			case event, ok := <-watcher.Events:
				if !ok {
					return
				}
				// Verificamos qué tipo de operación fue (Create, Write, Remove, Rename, Chmod)
				if event.Has(fsnotify.Create) {
					log.Printf("📁 [CREADO] Archivo: %s\n", event.Name)
				}
				if event.Has(fsnotify.Write) {
					log.Printf("✏️  [MODIFICADO] Archivo: %s\n", event.Name)
				}
				if event.Has(fsnotify.Remove) {
					log.Printf("🗑️  [ELIMINADO] Archivo: %s\n", event.Name)
				}
				if event.Has(fsnotify.Rename) {
					log.Printf("🔄 [RENOMBRADO] Archivo: %s\n", event.Name)
				}

			case err, ok := <-watcher.Errors:
				if !ok {
					return
				}
				log.Println("❌ Error:", err)
			}
		}
	}()

	// 3. Añadimos la carpeta que queremos vigilar al watcher
	err = watcher.Add(carpetaAVigilar)
	if err != nil {
		log.Fatal(err)
	}

	log.Printf("👀 Vigilando la carpeta '%s'...", carpetaAVigilar)
	log.Println("Crea, modifica o elimina archivos ahí para ver los eventos. Presiona Ctrl+C para salir.")

	// Bloqueamos el hilo principal para que el programa no termine inmediatamente.
	// <-make(chan struct{}) se queda esperando infinitamente (hasta que lo mates con Ctrl+C).
	<-make(chan struct{})
}
