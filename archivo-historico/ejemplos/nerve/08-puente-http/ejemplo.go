/**
 * Ejemplo: Servidor HTTP con net/http (Estándar de Go)
 * 
 * Qué enseña este ejemplo:
 *   - Crear una aplicación web básica usando la librería estándar.
 *   - Decodificar un JSON que viene en el cuerpo de la petición.
 *   - Manejar métodos HTTP específicos (asegurarse de que sea un POST).
 * 
 * Para tu reto (Puente HTTP para Nerve):
 *   Cuando la ruta reciba los datos, deberás usar el cliente Nerve 
 *   para retransmitir la información hacia el hub de Nerve.
 */

package main

import (
	"encoding/json"
	"fmt"
	"net/http"
)

// 1. Definir la estructura (struct) de los datos que esperamos recibir
// Las etiquetas `json:"mensaje"` indican a Go cómo buscar el campo en el JSON.
type MensajePayload struct {
	Mensaje string `json:"mensaje"`
}

func main() {
	// 2. Definir las rutas (endpoints)
	http.HandleFunc("/", rutaRaiz)
	http.HandleFunc("/enviar", recibirYReenviar)

	puerto := ":8080"
	fmt.Printf("Servidor Go escuchando en http://localhost%s\n", puerto)
	
	// 3. Encender el servidor
	err := http.ListenAndServe(puerto, nil)
	if err != nil {
		fmt.Println("Error iniciando el servidor:", err)
	}
}

// Ruta GET básica
func rutaRaiz(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintln(w, "Servidor funcionando")
}

// Ruta POST que será nuestro "puente"
func recibirYReenviar(w http.ResponseWriter, r *http.Request) {
	// Asegurarnos de que sólo aceptamos peticiones POST
	if r.Method != http.MethodPost {
		http.Error(w, "Método no permitido. Usa POST.", http.StatusMethodNotAllowed)
		return
	}

	// Crear una variable para guardar los datos
	var payload MensajePayload

	// Decodificar el JSON del cuerpo (body) de la petición hacia nuestro struct
	err := json.NewDecoder(r.Body).Decode(&payload)
	if err != nil {
		http.Error(w, "JSON inválido", http.StatusBadRequest)
		return
	}

	if payload.Mensaje == "" {
		http.Error(w, "Falta el campo 'mensaje' en el JSON", http.StatusBadRequest)
		return
	}

	// En la terminal veremos lo que llegó
	fmt.Printf("📩 Recibido por HTTP: %s\n", payload.Mensaje)

	// ¡Aquí es donde integrarías Nerve! 
	// Ejemplo: clienteNerve.Publicar("canal_http", payload.Mensaje)

	// Responder a quien hizo la petición HTTP (con un JSON)
	w.Header().Set("Content-Type", "application/json")
	respuesta := fmt.Sprintf(`{"status": "ok", "recibido": "%s"}`, payload.Mensaje)
	fmt.Fprintln(w, respuesta)
}
