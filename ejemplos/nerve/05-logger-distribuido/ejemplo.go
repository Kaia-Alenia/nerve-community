/*
 * Ejemplo: Escritura de Logs en Go
 * 
 * Qué enseña este ejemplo:
 *   - Cómo obtener la fecha y hora actual usando `time.Now()`.
 *   - Cómo formatear una fecha en Go usando su sistema de fechas de referencia.
 *   - Cómo abrir un archivo en modo Append usando `os.OpenFile` y los flags correctos.
 * 
 * Para tu reto (Logger Distribuido con Nerve):
 *   En vez de llamar a `escribirLog` con datos estáticos, tu receptor de Nerve
 *   escuchará mensajes de otros nodos y llamará a tu función de log para 
 *   registrarlos en un archivo central.
 * 
 * Glosario:
 *   time.Now()          — Obtiene la fecha y hora actual.
 *   Format("2006-01-02 15:04:05") — Formatea la fecha. OJO: Go usa una fecha de referencia exacta
 *                         (2 de enero de 2006 a las 15:04:05) para definir formatos, NO usa %Y-%m-%d.
 *   os.OpenFile         — Abre un archivo con opciones avanzadas.
 *   os.O_APPEND         — Flag: si escribes, hazlo al final del archivo.
 *   os.O_CREATE         — Flag: si el archivo no existe, créalo.
 *   os.O_WRONLY         — Flag: abre el archivo solo para escritura.
 *   f.WriteString       — Escribe un string en el archivo abierto.
 */

package main

import (
	"fmt"
	"log"
	"os"
	"time"
)

const ArchivoLog = "sistema.log"

func escribirLog(nivel string, mensaje string) {
	// 1. Obtenemos el timestamp actual y lo formateamos
	// Recordatorio: "2006-01-02 15:04:05" es la forma de Go para decir "YYYY-MM-DD HH:MM:SS"
	ahora := time.Now()
	timestampFormateado := ahora.Format("2006-01-02 15:04:05")

	// 2. Construimos la línea de log final
	// Ejemplo: [2026-07-17 15:30:05] [INFO] El servidor ha iniciado correctamente
	lineaLog := fmt.Sprintf("[%s] [%s] %s\n", timestampFormateado, nivel, mensaje)

	// 3. Imprimimos en consola (opcional, para verlo en vivo)
	fmt.Print(lineaLog)

	// 4. Abrimos el archivo en modo "Append" (añadir al final)
	// Si no existe (O_CREATE), lo crea. Solo escritura (O_WRONLY).
	// Permisos 0644 (lectura y escritura para el dueño, solo lectura para otros).
	f, err := os.OpenFile(ArchivoLog, os.O_APPEND|os.O_CREATE|os.O_WRONLY, 0644)
	if err != nil {
		log.Printf("Error abriendo el archivo de log: %v", err)
		return
	}
	defer f.Close()

	// 5. Escribimos la línea en el archivo
	if _, err := f.WriteString(lineaLog); err != nil {
		log.Printf("Error escribiendo en el archivo de log: %v", err)
	}
}

func main() {
	fmt.Printf("Escribiendo logs en '%s'...\n\n", ArchivoLog)

	escribirLog("INFO", "Sistema iniciado.")
	escribirLog("DEBUG", "Conexión a la base de datos establecida en 14ms.")
	escribirLog("WARNING", "Poco espacio en disco (15% restante).")
	escribirLog("ERROR", "Fallo al procesar el archivo 'datos.csv': Archivo no encontrado.")
	escribirLog("INFO", "Apagando sistema de forma segura.")

	fmt.Printf("\nRevisa el archivo '%s' para ver los resultados guardados.\n", ArchivoLog)
}
