package main

import (
	"fmt"
	"os"
	"os/signal"
	"syscall"

	"nerve"
)

func procesarMensaje(mensajeCrudo nerve.Message) {
	fmt.Printf(" ¡Mensaje recibido!: %+v\n", mensajeCrudo)

	payload, ok := mensajeCrudo.Payload.(map[string]interface{})
	if ok {
		if texto, ok := payload["texto"].(string); ok {
			fmt.Printf("Texto extraído: %s\n", texto)
		}
	}
}

func main() {
	fmt.Println("Iniciando receptor...")
	cliente := nerve.NewNexusClient()

	// Nos conectamos como "receptor_01"
	cliente.Connect("receptor_01")
	fmt.Println("✅ Receptor conectado. Esperando mensajes...")

	// Registramos la función que se llamará al recibir mensajes
	cliente.Listen(procesarMensaje)

	// Mantenemos el programa vivo para escuchar
	c := make(chan os.Signal, 1)
	signal.Notify(c, os.Interrupt, syscall.SIGTERM)
	<-c

	fmt.Println("\nSaliendo...")
	cliente.Disconnect()
}
