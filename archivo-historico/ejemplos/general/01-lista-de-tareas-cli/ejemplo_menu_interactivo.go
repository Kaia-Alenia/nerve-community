// Ejemplo: Mini gestor de contactos con menú interactivo y persistencia JSON en Go
//
// Qué enseña este ejemplo:
//   - Cómo crear un loop con for {}
//   - Cómo usar bufio.NewScanner para leer líneas de la terminal
//   - Cómo leer y guardar archivos con os.ReadFile y os.WriteFile
//   - Cómo usar encoding/json para convertir structs de Go a JSON y viceversa
//
// Glosario de términos "raros":
//   bufio.NewScanner — Crea un "escáner" que facilita leer texto de la consola línea por línea.
//   os.ReadFile      — Lee todo el contenido de un archivo de una sola vez.
//   os.WriteFile     — Guarda datos en un archivo, sobreescribiéndolo.
//   json.Marshal     — (De "marshall") Convierte tus variables de Go a texto JSON.
//   json.Unmarshal   — Convierte texto JSON de vuelta a variables de Go.
//   0644             — Permisos del archivo (lectura/escritura para ti, lectura para otros).

package main

import (
	"bufio"
	"encoding/json"
	"fmt"
	"os"
	"strconv"
	"strings"
)

const ARCHIVO = "contactos.json"

// Contacto representa un elemento de nuestra lista.
// Las etiquetas `json:"nombre"` indican cómo se llamará el campo en el archivo.
type Contacto struct {
	Nombre   string `json:"nombre"`
	Telefono string `json:"telefono"`
}

func cargarContactos() []Contacto {
	// Intentamos leer el archivo
	data, err := os.ReadFile(ARCHIVO)
	if err != nil {
		// Si hay un error (ej. el archivo no existe), devolvemos lista vacía
		return []Contacto{}
	}

	var contactos []Contacto
	// Convertimos el JSON a la lista de structs
	json.Unmarshal(data, &contactos)
	return contactos
}

func guardarContactos(contactos []Contacto) {
	// MarshalIndent hace que el JSON sea legible (con espacios)
	data, _ := json.MarshalIndent(contactos, "", "    ")
	os.WriteFile(ARCHIVO, data, 0644)
}

func mostrarContactos(contactos []Contacto) {
	if len(contactos) == 0 {
		fmt.Println("No hay contactos guardados todavía.")
		return
	}
	fmt.Println("\n--- Tus contactos ---")
	for i, contacto := range contactos {
		fmt.Printf("  %d. %s — %s\n", i+1, contacto.Nombre, contacto.Telefono)
	}
}

// Función auxiliar para leer texto
func preguntar(prompt string, scanner *bufio.Scanner) string {
	fmt.Print(prompt)
	scanner.Scan()
	return strings.TrimSpace(scanner.Text())
}

func main() {
	contactos := cargarContactos()
	scanner := bufio.NewScanner(os.Stdin)

	for {
		fmt.Println("\n=== Gestor de Contactos ===")
		fmt.Println("1. Ver contactos")
		fmt.Println("2. Agregar contacto")
		fmt.Println("3. Actualizar teléfono")
		fmt.Println("4. Eliminar contacto")
		fmt.Println("5. Salir")

		opcion := preguntar("\nElige una opción (1-5): ", scanner)

		switch opcion {
		case "1":
			mostrarContactos(contactos)

		case "2":
			nombre := preguntar("Nombre: ", scanner)
			telefono := preguntar("Teléfono: ", scanner)

			if nombre != "" {
				contactos = append(contactos, Contacto{Nombre: nombre, Telefono: telefono})
				guardarContactos(contactos)
				fmt.Printf("✓ Contacto '%s' guardado.\n", nombre)
			} else {
				fmt.Println("El nombre no puede estar vacío.")
			}

		case "3":
			mostrarContactos(contactos)
			if len(contactos) == 0 {
				continue
			}

			idxStr := preguntar("\nNúmero del contacto a actualizar: ", scanner)
			idx, err := strconv.Atoi(idxStr)
			idx -= 1 // Ajustamos para índice 0

			if err == nil && idx >= 0 && idx < len(contactos) {
				nuevoTel := preguntar("Nuevo teléfono: ", scanner)
				contactos[idx].Telefono = nuevoTel
				guardarContactos(contactos)
				fmt.Println("✓ Contacto actualizado.")
			} else {
				fmt.Println("Número inválido.")
			}

		case "4":
			mostrarContactos(contactos)
			if len(contactos) == 0 {
				continue
			}

			idxStr := preguntar("\nNúmero del contacto a eliminar: ", scanner)
			idx, err := strconv.Atoi(idxStr)
			idx -= 1

			if err == nil && idx >= 0 && idx < len(contactos) {
				eliminado := contactos[idx]
				// Magia para eliminar un elemento de un slice en Go:
				contactos = append(contactos[:idx], contactos[idx+1:]...)
				guardarContactos(contactos)
				fmt.Printf("✓ Contacto '%s' eliminado.\n", eliminado.Nombre)
			} else {
				fmt.Println("Número inválido.")
			}

		case "5":
			fmt.Println("¡Hasta luego!")
			return

		default:
			fmt.Println("Opción no reconocida, intenta de nuevo.")
		}
	}
}
