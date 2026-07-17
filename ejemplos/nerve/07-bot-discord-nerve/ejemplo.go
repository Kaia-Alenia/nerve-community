/**
 * Ejemplo: Bot básico con discordgo
 * 
 * Qué enseña este ejemplo:
 *   - Cómo configurar e iniciar una sesión de discordgo en Go.
 *   - Configurar los "Intents" para especificar qué eventos quieres.
 *   - Añadir un "handler" (manejador) para eventos de nuevos mensajes.
 * 
 * Para tu reto (Bot Discord Nerve):
 *   En vez de solo responder con "¡Hola!", conectarás el bot de Discord con
 *   tu cliente Nerve. Cuando llegue un mensaje a Discord, usarás tu cliente 
 *   Nerve para notificar a la red, y viceversa.
 * 
 * Glosario:
 *   discordgo.New()         — Crea una nueva sesión del bot.
 *   dg.Identify.Intents     — Define qué eventos de Discord recibirá el bot (ej. GuildMessages).
 *   dg.AddHandler()         — Registra una función que se llamará cuando ocurra un evento.
 *   s.ChannelMessageSend()  — Envía un mensaje a un canal de Discord.
 */

package main

import (
	"fmt"
	"os"
	"os/signal"
	"strings"
	"syscall"

	"github.com/bwmarrin/discordgo"
)

func main() {
	// Reemplaza esto con tu token real o usa variables de entorno
	token := os.Getenv("DISCORD_TOKEN")
	if token == "" {
		token = "TU_TOKEN_AQUI"
	}

	if token == "TU_TOKEN_AQUI" {
		fmt.Println("⚠️ ADVERTENCIA: Reemplaza 'TU_TOKEN_AQUI' con el token de tu bot de Discord.")
		fmt.Println("Puedes obtenerlo en: https://discord.com/developers/applications")
		return
	}

	// 1. Crear una nueva sesión de Discord usando el token del bot
	dg, err := discordgo.New("Bot " + token)
	if err != nil {
		fmt.Println("Error creando la sesión de Discord:", err)
		return
	}

	// 2. Registrar el manejador (handler) para el evento MessageCreate
	dg.AddHandler(messageCreate)

	// 3. Configurar los Intents (permisos). Necesitamos los de mensajes.
	// Nota: Para MessageContent, asegúrate de habilitarlo en el portal de desarrolladores.
	dg.Identify.Intents = discordgo.IntentsGuildMessages | discordgo.IntentsMessageContent

	// 4. Abrir una conexión con Discord
	err = dg.Open()
	if err != nil {
		fmt.Println("Error abriendo conexión:", err)
		return
	}

	// Esperar hasta que se reciba una señal para terminar (CTRL+C)
	fmt.Println("El bot está funcionando. Presiona CTRL-C para salir.")
	sc := make(chan os.Signal, 1)
	signal.Notify(sc, syscall.SIGINT, syscall.SIGTERM, os.Interrupt)
	<-sc

	// 5. Cerrar la sesión de forma limpia
	dg.Close()
}

// messageCreate se llamará CADA VEZ que se envíe un mensaje a un canal al que el bot tenga acceso
func messageCreate(s *discordgo.Session, m *discordgo.MessageCreate) {
	// Ignorar todos los mensajes creados por el bot mismo
	if m.Author.ID == s.State.User.ID {
		return
	}

	// Si el mensaje dice "ping", responder con "pong"
	if strings.ToLower(m.Content) == "ping" {
		fmt.Printf("[%s] dijo ping, respondiendo...\n", m.Author.Username)
		
		// Enviar el mensaje al mismo canal donde se recibió el ping
		s.ChannelMessageSend(m.ChannelID, "pong 🏓")
	}
}
