/*
Ejemplo: Leer un CSV real desde disco, filtrar y calcular sumas

Qué enseña este ejemplo:
  - Cómo abrir y leer un archivo CSV con os.Open y encoding/csv
  - Cómo iterar por cada fila del archivo CSV
  - Cómo convertir strings a números con strconv.ParseFloat
  - Cómo agrupar filas y calcular sumas / promedios usando mapas

Para tu reto (analizador de gastos):
  Aplica el mismo patrón para leer tu CSV de gastos
  (fecha, categoría, monto) y calcular totales por categoría.

Glosario:
  os.Open(archivo)      — Abre un archivo en modo lectura.
  defer f.Close()       — Asegura que el archivo se cerrará cuando termine la función.
  csv.NewReader(f)      — Crea un lector especializado que entiende el formato CSV (comas, comillas).
  strconv.ParseFloat(s) — Convierte un texto como "1234.50" a un número flotante (decimal).
*/

package main

import (
	"encoding/csv"
	"fmt"
	"os"
	"strconv"
)

type Empleado struct {
	Nombre       string
	Departamento string
	Salario      float64
}

func leerEmpleados(rutaCsv string) []Empleado {
	file, err := os.Open(rutaCsv)
	if err != nil {
		fmt.Printf("No se pudo abrir el archivo: %v\n", err)
		return []Empleado{}
	}
	defer file.Close()

	reader := csv.NewReader(file)
	// Leer todas las filas
	filas, err := reader.ReadAll()
	if err != nil {
		fmt.Printf("Error leyendo el CSV: %v\n", err)
		return []Empleado{}
	}

	var empleados []Empleado

	// Iterar omitiendo la cabecera (índice 0)
	for i := 1; i < len(filas); i++ {
		fila := filas[i]
		if len(fila) < 3 {
			continue
		}

		nombre := fila[0]
		departamento := fila[1]
		salario, _ := strconv.ParseFloat(fila[2], 64)

		empleados = append(empleados, Empleado{
			Nombre:       nombre,
			Departamento: departamento,
			Salario:      salario,
		})
	}

	return empleados
}

type Estadisticas struct {
	Suma     float64
	Cantidad int
}

func reportePorDepartamento(empleados []Empleado) {
	totales := make(map[string]*Estadisticas)

	for _, emp := range empleados {
		dept := emp.Departamento
		if totales[dept] == nil {
			totales[dept] = &Estadisticas{}
		}
		totales[dept].Suma += emp.Salario
		totales[dept].Cantidad++
	}

	fmt.Println("\n--- Reporte por departamento ---")
	for dept, stats := range totales {
		promedio := stats.Suma / float64(stats.Cantidad)
		// %.0f imprime sin decimales
		fmt.Printf("  %s: total=$%.0f | promedio=$%.0f | empleados=%d\n", dept, stats.Suma, promedio, stats.Cantidad)
	}
}

func main() {
	archivo := "empleados.csv"

	// Crear archivo de ejemplo si no existe
	if _, err := os.Stat(archivo); os.IsNotExist(err) {
		datos := []string{
			"nombre,departamento,salario",
			"Ana García,Ingeniería,35000",
			"Luis Martínez,Marketing,28000",
			"Carmen López,Ingeniería,42000",
			"Pedro Sánchez,Marketing,31000",
			"Sofía Ramírez,Ingeniería,39000",
		}
		
		f, _ := os.Create(archivo)
		for _, linea := range datos {
			f.WriteString(linea + "\n")
		}
		f.Close()
		fmt.Printf("Archivo '%s' creado de ejemplo.\n", archivo)
	}

	empleados := leerEmpleados(archivo)
	fmt.Printf("\nSe leyeron %d empleados.\n", len(empleados))
	reportePorDepartamento(empleados)
}
