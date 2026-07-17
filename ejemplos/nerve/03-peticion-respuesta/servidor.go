package main

import (
	"fmt"
	"os"
	"os/signal"
	"syscall"

	"nerve"
)

type ServidorCalculadora struct {
	cliente *nerve.NexusClient
}

func (s *ServidorCalculadora) atenderPeticion(mensajeCrudo nerve.Message) {
	remitente := mensajeCrudo.From
	payload, ok := mensajeCrudo.Payload.(map[string]interface{})
	if !ok {
		return
	}

	accion, ok := payload["accion"].(string)
	if ok && accion == "sumar" {
		a, _ := payload["a"].(float64)
		b, _ := payload["b"].(float64)
		resultado := a + b

		fmt.Printf(" Solicitud de suma recibida de '%s': %v + %v = %v\n", remitente, a, b, resultado)

		respuesta := map[string]interface{}{
			"accion":    "respuesta_operacion",
			"resultado": resultado,
		}

		fmt.Printf("Enviando resultado a '%s'...\n", remitente)
		s.cliente.Send(remitente, respuesta)
	}
}

func (s *ServidorCalculadora) iniciar() {
	s.cliente.Connect("servidor_calculadora")
	fmt.Println("✅ Servidor Calculadora en línea y esperando peticiones...")

	s.cliente.Listen(s.atenderPeticion)

	c := make(chan os.Signal, 1)
	signal.Notify(c, os.Interrupt, syscall.SIGTERM)
	<-c

	fmt.Println("\nApagando servidor...")
	s.cliente.Disconnect()
}

func main() {
	app := &ServidorCalculadora{
		cliente: nerve.NewNexusClient(),
	}
	app.iniciar()
}
