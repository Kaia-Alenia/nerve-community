package main

import (
	"fmt"
	"time"

	"nerve"
)

func main() {
	fmt.Println("Iniciando emisor...")
	// 1. Crear el cliente de Nerve
	cliente := nerve.NewNexusClient()

	// 2. Conectarse al Hub con un identificador único
	cliente.Connect("emisor_01")
	fmt.Println("✅ Emisor conectado al Nerve Hub.")

	// Esperamos un momento para asegurar que el receptor esté listo
	time.Sleep(1 * time.Second)

	// 3. Preparar el mensaje (payload) y enviarlo al receptor
	mensaje := map[string]interface{}{
		"texto":     "¡Hola, Nerve!",
		"timestamp": time.Now().Unix(),
	}

	fmt.Println("Enviando mensaje a 'receptor_01'...")
	cliente.Send("receptor_01", mensaje)

	fmt.Println("Mensaje enviado. Terminando emisor...")
	// Desconectamos el cliente para liberar recursos
	cliente.Disconnect()
}
