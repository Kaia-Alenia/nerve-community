package main

import (
	"fmt"
	"os"
	"os/signal"
	"syscall"
	"time"

	"nerve"
)

func main() {
	fmt.Println("Iniciando publicador (estación de radio)...")
	cliente := nerve.NewNexusClient()
	cliente.Connect("publicador_noticias")
	fmt.Println("✅ Publicador conectado al Hub.")

	ticker := time.NewTicker(3 * time.Second)
	quit := make(chan os.Signal, 1)
	signal.Notify(quit, os.Interrupt, syscall.SIGTERM)

	contador := 1
	
	go func() {
		for {
			select {
			case <-ticker.C:
				noticia := map[string]interface{}{
					"canal":     "noticias_tech",
					"titular":   fmt.Sprintf("Noticia #%d: Nerve Hub funciona genial", contador),
					"timestamp": time.Now().Unix(),
				}

				fmt.Printf(" Transmitiendo (broadcast): %s\n", noticia["titular"])
				cliente.Broadcast(noticia)
				contador++
			}
		}
	}()

	<-quit
	fmt.Println("\nApagando publicador...")
	ticker.Stop()
	cliente.Disconnect()
}
