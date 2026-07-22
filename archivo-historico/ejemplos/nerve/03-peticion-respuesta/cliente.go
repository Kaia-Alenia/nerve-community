package main

import (
	"fmt"
	"time"

	"nerve"
)

type ClientePeticion struct {
	cliente           *nerve.NexusClient
	respuestaRecibida *float64
}

func (c *ClientePeticion) manejarRespuesta(mensajeCrudo nerve.Message) {
	payload, ok := mensajeCrudo.Payload.(map[string]interface{})
	if !ok {
		return
	}

	accion, ok := payload["accion"].(string)
	if ok && accion == "respuesta_operacion" {
		if resultado, ok := payload["resultado"].(float64); ok {
			c.respuestaRecibida = &resultado
			fmt.Printf("✅ ¡El servidor respondió! El resultado es: %v\n", resultado)
		}
	}
}

func (c *ClientePeticion) iniciar() {
	c.cliente.Connect("cliente_calculadora")
	c.cliente.Listen(c.manejarRespuesta)

	fmt.Println("Enviando petición de suma al servidor (5 + 7)...")
	peticion := map[string]interface{}{
		"accion": "sumar",
		"a":      5,
		"b":      7,
	}
	c.cliente.Send("servidor_calculadora", peticion)

	tiempoEspera := 0
	for c.respuestaRecibida == nil && tiempoEspera < 5 {
		fmt.Println("⏳ Esperando respuesta...")
		time.Sleep(1 * time.Second)
		tiempoEspera++
	}

	if c.respuestaRecibida == nil {
		fmt.Println("❌ Tiempo de espera agotado. El servidor no contestó.")
	}

	c.cliente.Disconnect()
}

func main() {
	app := &ClientePeticion{
		cliente: nerve.NewNexusClient(),
	}
	app.iniciar()
}
