# 01 - Fundamentos

### `variables (var, :=)`

**¿Qué es?**
Contenedores en memoria. En Go puedes usar `var` para declararlas formalmente o `:=` para que Go infiera el tipo automáticamente (solo dentro de funciones).

**¿Para qué se usa?**
Para almacenar información que tu programa usará, como contadores o nombres.

**Ejemplo:**
```go
package main

import "fmt"

func main() {
    var nombre string = "Ana"
    edad := 30 // Go sabe que es un int
    fmt.Println(nombre, edad)
}
```

**Errores comunes de principiante:**
- Usar `:=` fuera de una función (no está permitido).
- Declarar una variable y no usarla (Go lanzará un error de compilación).

**Términos relacionados:** [`tipos de datos`](#tipos-de-datos-string-int-float64-bool)

### `tipos de datos (string, int, float64, bool)`

**¿Qué es?**
Clasificaciones estrictas de información en Go. Los más comunes son texto (`string`), números enteros (`int`), decimales de alta precisión (`float64`) y booleanos (`bool`).

**¿Para qué se usa?**
Go es fuertemente tipado; necesita saber exactamente cuánta memoria asignar y qué operaciones son válidas.

**Ejemplo:**
```go
package main

import "fmt"

func main() {
    texto := "Hola"
    entero := 5
    decimal := 3.14
    activo := true
    fmt.Println(texto, entero, decimal, activo)
}
```

**Errores comunes de principiante:**
- Intentar sumar un `int` y un `float64` sin convertir uno de los dos explícitamente (`float64(entero) + decimal`).

**Términos relacionados:** [`variables`](#variables-var-)

### `fmt (paquete)`

**¿Qué es?**
El paquete estándar 'format' de Go, utilizado para leer de la entrada y escribir en la salida (pantalla).

**¿Para qué se usa?**
Para imprimir mensajes en la terminal, formatear texto o pedir datos al usuario.

**Ejemplo:**
```go
package main

import "fmt"

func main() {
    fmt.Println("Hola, Mundo")
    fmt.Printf("Edad: %d\n", 30)
}
```

**Errores comunes de principiante:**
- Importar `fmt` y no usarlo (da error de compilación).

**Términos relacionados:** [`modulos`](../go/05-modulos-y-librerias.md#módulo-go-mod)



### `package main`

**¿Qué es?**
La declaración obligatoria en la primera línea de cualquier programa ejecutable en Go.

**¿Para qué se usa?**
Indica al compilador de Go que este archivo debe compilarse como un programa ejecutable (una aplicación) y no como una librería compartida.

**Ejemplo:**
```go
package main

import "fmt"

func main() {
    fmt.Println("Hola")
}
```

**Errores comunes de principiante:**
- Olvidar ponerlo, lo que causa que Go no sepa por dónde empezar a compilar.

**Términos relacionados:** [`func main()`](#package-main)

