/*
Ejemplo: Mini juego "adivina el color" con math/rand, bucle y conteo de intentos

Qué enseña este ejemplo:
  - Cómo usar rand.Intn() para seleccionar un elemento al azar de un slice
  - Cómo estructurar el bucle de intentos con for + contador
  - Cómo dar pistas simples (mayor/menor en números, aquí: letra inicial)
  - Cómo manejar input no válido con validación condicional

Para tu reto (adivina el número):
  Aplica el mismo patrón de bucle + contador + pistas,
  pero usa rand.Intn(100) + 1 para generar un número
  y compara si el intento es mayor o menor al número secreto.

Glosario:
  rand.Intn(n)                 — genera un entero al azar entre 0 y n-1
  strings.ToLower(s)           — convierte un string a minúsculas
  strings.TrimSpace(s)         — elimina espacios al inicio y final del string
  bufio.NewReader(os.Stdin)    — crea un lector para leer entrada desde la terminal
*/

package main

import (
	"bufio"
	"fmt"
	"math/rand"
	"os"
	"strings"
)

func contiene(slice []string, item string) bool {
	for _, s := range slice {
		if s == item {
			return true
		}
	}
	return false
}

func main() {
	colores := []string{"rojo", "azul", "verde", "amarillo", "morado", "naranja"}
	maxIntentos := 4
	
	// elegir color al azar
	colorSecreto := colores[rand.Intn(len(colores))]
	intentos := 0

	fmt.Println("=== Adivina el color ===")
	fmt.Printf("Tengo un color en mente. Tienes %d intentos.\n", maxIntentos)
	fmt.Printf("Opciones posibles: %s\n\n", strings.Join(colores, ", "))

	reader := bufio.NewReader(os.Stdin)

	for intentos < maxIntentos {
		fmt.Printf("Intento %d/%d: ", intentos+1, maxIntentos)
		respuesta, _ := reader.ReadString('\n')
		intento := strings.ToLower(strings.TrimSpace(respuesta))

		// Validar
		if !contiene(colores, intento) {
			fmt.Printf("'%s' no es un color válido. Elige de la lista.\n\n", intento)
			continue
		}

		intentos++

		if intento == colorSecreto {
			fmt.Printf("\n¡Correcto! Era '%s'. Lo lograste en %d intento(s).\n", colorSecreto, intentos)
			return
		}

		// Pista (comparando primer carácter)
		if intento[0] < colorSecreto[0] {
			fmt.Printf("No es '%s'. El color secreto va después alfabéticamente.\n", intento)
		} else {
			fmt.Printf("No es '%s'. El color secreto va antes alfabéticamente.\n", intento)
		}
		fmt.Println()
	}

	fmt.Printf("\nSe acabaron los intentos. El color era '%s'.\n", colorSecreto)
}
