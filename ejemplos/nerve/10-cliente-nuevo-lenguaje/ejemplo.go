/**
 * Ejemplo: Cliente de Socket TCP en Go
 * 
 * Qué enseña este ejemplo:
 *   - Conectarse a un servidor TCP con el paquete `net`.
 *   - Escribir en la conexión usando `fmt.Fprintf` o `conn.Write`.
 *   - Leer la respuesta del servidor usando `bufio.NewReader`.
 * 
 * Para tu reto (Nuevo Cliente Nerve):
 *   Go es fenomenal para clientes de red. Podrás lanzar una goroutine que se 
 *   quede bloqueada leyendo `bufio.ReadString('\n')` para recibir mensajes,
 *   mientras tu programa principal puede seguir llamando a `Publicar()`.
 */

package main

import (
	"bufio"
	"encoding/json"
	"fmt"
	"net"
	"strings"
)

func main() {
	host := "127.0.0.1"
	puerto := "5000"
	direccion := host + ":" + puerto

	fmt.Printf("🔄 Conectando a %s...\n", direccion)

	// 1. Intentar conectar (net.Dial funciona para TCP, UDP, etc.)
	conn, err := net.Dial("tcp", direccion)
	if err != nil {
		fmt.Println("❌ No se pudo conectar. ¿Está el servidor encendido?")
		fmt.Println("Error:", err)
		return
	}
	// Asegurar que cerraremos la conexión al terminar la función
	defer conn.Close()
	fmt.Println("✅ Conectado exitosamente")

	// 2. Preparar los datos
	// Usamos un mapa como ejemplo rápido, en código real deberías usar un struct
	payload := map[string]string{
		"tipo":      "publicar",
		"canal":     "test",
		"contenido": "Hola desde el nuevo cliente Go!",
	}

	// 3. Convertir el mapa a JSON Bytes
	datosBytes, err := json.Marshal(payload)
	if err != nil {
		fmt.Println("Error creando JSON:", err)
		return
	}

	// 4. Enviar los datos (añadiendo el salto de línea al final)
	datosStr := string(datosBytes) + "\n"
	fmt.Fprintf(conn, "%s", datosStr)
	fmt.Printf("⬆️ Enviado: %s\n", strings.TrimSpace(datosStr))

	// 5. Esperar la respuesta (leyendo hasta encontrar un salto de línea \n)
	respuesta, err := bufio.NewReader(conn).ReadString('\n')
	if err != nil {
		fmt.Println("⚠️ El servidor cerró la conexión o hubo un error al leer.")
		return
	}

	// Mostrar la respuesta
	fmt.Printf("⬇️ Recibido: %s\n", strings.TrimSpace(respuesta))
}
