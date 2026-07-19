# 🐹 07 - Archivos y entrada/salida

### `os.ReadFile / os.WriteFile`

**¿Qué es?**
Funciones convenientes del paquete `os` (previamente en `io/ioutil`) para leer o escribir todo el contenido de un archivo de una sola vez en la memoria.

**¿Para qué se usa?**
Para tareas rápidas y scripts donde los archivos son pequeños y se pueden cargar completamente en la memoria RAM sin problemas de rendimiento.

**Ejemplo:**
```go
package main

import (
    "fmt"
    "os"
)

func main() {
    // Escribir un archivo
    err := os.WriteFile("temporal.txt", []byte("¡Hola mundo!"), 0644)
    if err != nil {
        fmt.Println("Error escribiendo:", err)
        return
    }

    // Leer el archivo entero
    data, err := os.ReadFile("temporal.txt")
    if err != nil {
        fmt.Println("Error leyendo:", err)
        return
    }
    fmt.Println(string(data))
    
    // Limpieza
    os.Remove("temporal.txt")
}
```

**Errores comunes de principiante:**
- Usar `ReadFile` para leer archivos muy grandes (ej. logs de GBs), lo que causará que la memoria del programa se agote. Para esos casos se debe usar lectura por flujos (streams) o buffers.

**Términos relacionados:** [`os.Open`](#osopen--oscreate)

---

### `os.Open / os.Create`

**¿Qué es?**
Funciones del paquete `os` que devuelven un descriptor de archivo (`*os.File`), permitiendo operaciones granulares (leer o escribir en fragmentos).

**¿Para qué se usa?**
Cuando necesitas un control más fino sobre cómo se procesa el archivo, por ejemplo leyendo línea por línea o cargando en memoria pequeños bloques (chunks) para archivos grandes.

**Ejemplo:**
```go
package main

import (
    "fmt"
    "os"
)

func main() {
    // os.Create abre o crea un archivo (lo trunca si existe)
    file, err := os.Create("manual.txt")
    if err != nil {
        fmt.Println("Error:", err)
        return
    }
    
    // IMPORTANTE: Asegurarnos de que el archivo se cierre siempre
    defer file.Close()
    
    _, err = file.WriteString("Línea 1\n")
    if err != nil {
        fmt.Println("Error al escribir:", err)
    }
    
    // Limpieza
    os.Remove("manual.txt")
}
```

**Errores comunes de principiante:**
- Olvidar usar `defer file.Close()` inmediatamente después de que `err` es verificado exitosamente. Esto deja descriptores de archivos huérfanos y puede agotar el límite de archivos abiertos por el SO.

**Términos relacionados:** [`defer`](../go/03-funciones.md#defer)

---

### `bufio` (bufio.Scanner)

**¿Qué es?**
Un paquete que envuelve a un `io.Reader` u `io.Writer` subyacente (como un archivo) y añade almacenamiento intermedio (buffering), reduciendo la cantidad de llamadas al sistema y mejorando la eficiencia.

**¿Para qué se usa?**
Su uso más popular, a través de `bufio.Scanner`, es para leer un archivo línea por línea de manera sencilla y eficiente sin cargar todo en memoria a la vez.

**Ejemplo:**
```go
package main

import (
    "bufio"
    "fmt"
    "strings"
)

func main() {
    // Simulamos un archivo usando un Reader sobre un string para el ejemplo
    data := "primera línea\nsegunda línea\ntercera línea"
    lector := strings.NewReader(data)
    
    // Creamos el scanner
    scanner := bufio.NewScanner(lector)
    
    // scanner.Scan() lee hasta el siguiente salto de línea
    for scanner.Scan() {
        fmt.Println("Línea leída:", scanner.Text())
    }
    
    if err := scanner.Err(); err != nil {
        fmt.Println("Error al leer:", err)
    }
}
```

**Errores comunes de principiante:**
- No revisar el `scanner.Err()` después de que termina el ciclo `for scanner.Scan()`. `Scan()` devuelve `false` ya sea por llegar al fin de archivo (EOF) o por un error, y debes distinguir cuál fue.

**Términos relacionados:** [`os.Open`](#osopen--oscreate)

---

### `io.Reader / io.Writer`

**¿Qué es?**
Son las dos interfaces más fundamentales e importantes de Go. Un `Reader` es cualquier cosa de la que se puedan leer bytes (archivos, conexiones HTTP, buffers de memoria), y un `Writer` es cualquier cosa donde se puedan escribir bytes.

**¿Para qué se usa?**
Son el corazón del diseño compositivo en Go. Permiten escribir código que funciona igual con un archivo, una conexión de red o un string, sin cambiar la lógica de la función. Todo el ecosistema de I/O de Go gira en torno a ellas.

**Ejemplo:**
```go
package main

import (
    "io"
    "os"
)

// Esta función acepta CUALQUIER Writer (archivo, red, consola...)
func EscribirMensaje(w io.Writer, mensaje string) {
    w.Write([]byte(mensaje + "\n"))
}

func main() {
    // Escribimos a la consola (os.Stdout implementa io.Writer)
    EscribirMensaje(os.Stdout, "¡Hola consola!")
    
    // También podríamos pasarle un archivo:
    // f, _ := os.Create("test.txt")
    // EscribirMensaje(f, "Hola archivo")
}
```

**Errores comunes de principiante:**
- Acoplar fuertemente funciones a tipos concretos como `*os.File` cuando la función solo necesita leer. Es mucho mejor que la función acepte un `io.Reader`.

**Términos relacionados:** [`interfaces`](../go/08-poo-basica.md#interface)

