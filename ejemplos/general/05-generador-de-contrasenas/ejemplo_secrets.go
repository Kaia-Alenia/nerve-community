/*
Ejemplo: Construir un PIN bancario seguro usando criptografía
 
Qué enseña este ejemplo:
  - Cuándo usar crypto/rand en lugar de math/rand (y por qué importa)
  - Cómo definir constantes de caracteres (alfabeto, números, símbolos)
  - Cómo garantizar que el resultado incluya al menos un carácter de cada tipo
 
Para tu reto (generador de contraseñas):
  Aplica el mismo patrón: construye el pool de caracteres según los
  parámetros del usuario (longitud, símbolos sí/no, mayúsculas sí/no),
  y usa crypto/rand para construir la contraseña.
 
Glosario:
  crypto/rand         — paquete que ofrece aleatoriedad criptográficamente segura.
  math/rand           — NO usar para contraseñas, sus resultados son predecibles.
  rand.Int(rand.Reader, max) — Devuelve un entero seguro grande, hay que convertirlo.
*/

package main

import (
	"crypto/rand"
	"fmt"
	"math/big"
)

const (
	Digitos    = "0123456789"
	Mayusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	Simbolos   = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
)

// Funciones de ayuda
func choice(pool string) byte {
	max := big.NewInt(int64(len(pool)))
	n, _ := rand.Int(rand.Reader, max)
	return pool[n.Int64()]
}

func shuffle(caracteres []byte) {
	for i := len(caracteres) - 1; i > 0; i-- {
		max := big.NewInt(int64(i + 1))
		n, _ := rand.Int(rand.Reader, max)
		j := n.Int64()
		caracteres[i], caracteres[j] = caracteres[j], caracteres[i]
	}
}

func generarPin(longitud int, soloNumeros bool) string {
	var pool string
	if soloNumeros {
		pool = Digitos
	} else {
		pool = Mayusculas + Digitos
	}

	pin := make([]byte, longitud)
	for i := 0; i < longitud; i++ {
		pin[i] = choice(pool)
	}
	return string(pin)
}

func generarPinGarantizado(longitud int) string {
	if longitud < 3 {
		panic("La longitud mínima para un PIN garantizado es 3.")
	}

	poolCompleto := Mayusculas + Digitos + Simbolos

	caracteres := make([]byte, longitud)
	
	// 1. Garantizar al menos uno de cada tipo requerido
	caracteres[0] = choice(Mayusculas)
	caracteres[1] = choice(Digitos)
	caracteres[2] = choice(Simbolos)

	// 2. Rellenar el resto
	for i := 3; i < longitud; i++ {
		caracteres[i] = choice(poolCompleto)
	}

	// 3. Mezclar
	shuffle(caracteres)

	return string(caracteres)
}

func main() {
	fmt.Println("=== Generador de PINs seguros ===\n")

	fmt.Println("PINs numéricos (6 dígitos):")
	for i := 0; i < 3; i++ {
		fmt.Printf("  %s\n", generarPin(6, true))
	}

	fmt.Println("\nPINs alfanuméricos (8 caracteres):")
	for i := 0; i < 3; i++ {
		fmt.Printf("  %s\n", generarPin(8, false))
	}

	fmt.Println("\nPINs con garantía (letra + dígito + símbolo, 10 chars):")
	for i := 0; i < 3; i++ {
		fmt.Printf("  %s\n", generarPinGarantizado(10))
	}
}
