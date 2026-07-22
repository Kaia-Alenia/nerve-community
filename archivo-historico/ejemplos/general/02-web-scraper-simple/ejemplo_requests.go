// Ejemplo: Extraer múltiples elementos de una página con net/http + goquery en Go
//
// Qué enseña este ejemplo:
//   - Cómo hacer una petición HTTP GET con net/http
//   - Cómo usar PuerkitoBio/goquery (inspirado en jQuery) para buscar elementos HTML
//   - Cómo guardar datos en un archivo CSV
//
// Para tu reto (web scraper):
//   Instala la dependencia ejecutando: go get github.com/PuerkitoBio/goquery
//
// Glosario de términos "raros":
//   http.Get           — Pide datos a una URL de internet.
//   defer res.Body.Close() — Asegura que la conexión de red se cierre automáticamente al terminar.
//   goquery.NewDocumentFromReader — Lee el HTML y lo prepara para ser navegado.
//   doc.Find()         — Busca elementos usando selectores CSS (ej: ".quote").
//   s.Find().Text()    — Extrae el texto dentro del elemento encontrado.

package main

import (
	"encoding/csv"
	"fmt"
	"log"
	"net/http"
	"os"
	"strings"

	"github.com/PuerkitoBio/goquery"
)

const URL = "https://quotes.toscrape.com/"

type Dato struct {
	Texto string
	Autor string
}

func main() {
	// 1. Hacer la petición GET
	res, err := http.Get(URL)
	if err != nil {
		log.Fatalf("Error al conectar: %v", err)
	}
	defer res.Body.Close()

	if res.StatusCode != 200 {
		log.Fatalf("Error HTTP: %d", res.StatusCode)
	}

	// 2. Crear el documento goquery desde la respuesta
	doc, err := goquery.NewDocumentFromReader(res.Body)
	if err != nil {
		log.Fatalf("Error al procesar HTML: %v", err)
	}

	// 3. Buscar TODOS los elementos con class="quote"
	elementos := doc.Find(".quote")
	fmt.Printf("Se encontraron %d frases en la página.\n\n", elementos.Length())

	var datosExtraidos []Dato

	// 4. Iterar sobre cada elemento encontrado
	elementos.Each(func(i int, s *goquery.Selection) {
		// s representa cada bloque individual ".quote"
		texto := s.Find(".text").Text()
		autor := s.Find(".author").Text()

		datosExtraidos = append(datosExtraidos, Dato{Texto: texto, Autor: autor})
		
		fmt.Printf("\"%s\"\n", texto)
		fmt.Printf("  — %s\n\n", autor)
	})

	// 5. Guardar los datos en un archivo CSV
	file, err := os.Create("frases.csv")
	if err != nil {
		log.Fatalf("Error al crear archivo CSV: %v", err)
	}
	defer file.Close()

	escritor := csv.NewWriter(file)
	defer escritor.Flush() // Asegura que los datos en buffer se escriban al disco

	// Escribir cabeceras
	escritor.Write([]string{"texto", "autor"})

	// Escribir filas
	for _, dato := range datosExtraidos {
		// Reemplazamos saltos de línea para mantener el CSV limpio
		textoLimpio := strings.ReplaceAll(dato.Texto, "\n", " ")
		escritor.Write([]string{textoLimpio, dato.Autor})
	}

	fmt.Println("✓ Datos guardados exitosamente en 'frases.csv'")
}
