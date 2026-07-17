package main

import (
	"fmt"
	"os"
	"os/signal"
	"syscall"

	"nerve"
)

var nombreNodo string

func alRecibirNoticia(mensajeCrudo nerve.Message) {
	payload, ok := mensajeCrudo.Payload.(map[string]interface{})
	if !ok {
		return
	}

	if canal, ok := payload["canal"].(string); ok && canal == "noticias_tech" {
		titular, ok := payload["titular"].(string)
		if !ok {
			titular = "Sin titular"
		}
		fmt.Printf("[%s]  Nueva noticia interceptada: %s\n", nombreNodo, titular)
	}
}

func main() {
	if len(os.Args) > 1 {
		nombreNodo = os.Args[1]
	} else {
		nombreNodo = "suscriptor_default"
	}

	fmt.Printf("Iniciando %s...\n", nombreNodo)
	cliente := nerve.NewNexusClient()
	cliente.Connect(nombreNodo)
	fmt.Printf("✅ %s conectado. Escuchando el canal 'noticias_tech'...\n", nombreNodo)

	cliente.Listen(alRecibirNoticia)

	c := make(chan os.Signal, 1)
	signal.Notify(c, os.Interrupt, syscall.SIGTERM)
	<-c

	fmt.Printf("\nApagando %s...\n", nombreNodo)
	cliente.Disconnect()
}
