# 🐹 02 - Control de flujo

### `if / else`

**¿Qué es?**
Estructuras condicionales que no requieren paréntesis alrededor de la condición.

**¿Para qué se usa?**
Para decidir qué bloque de código ejecutar en función de una expresión booleana.

**Ejemplo:**
```go
package main

import "fmt"

func main() {
    edad := 20
    if edad >= 18 {
        fmt.Println("Adulto")
    } else {
        fmt.Println("Menor")
    }
}
```

**Errores comunes de principiante:**
- Poner la llave de apertura `{` en una línea nueva (Go exige que esté en la misma línea que el `if` o `else`).

**Términos relacionados:** [`switch`](#if--else)

### `for`

**¿Qué es?**
La ÚNICA estructura de bucle en Go. Puede usarse como un bucle clásico `for`, como un `while` o para iterar sobre colecciones.

**¿Para qué se usa?**
Para repetir acciones. Go simplifica esto teniendo una sola palabra clave para todos los casos de repetición.

**Ejemplo:**
```go
package main

import "fmt"

func main() {
    i := 0
    // Como un while
    for i < 10 {
        i++
    }

    // Clásico
    for i := 0; i < 5; i++ {
        fmt.Println(i)
    }
}
```

**Errores comunes de principiante:**
- Buscar la palabra reservada `while` (no existe en Go).

**Términos relacionados:** [`range`](#range)

### `range`

**¿Qué es?**
Una palabra clave que se usa junto con `for` para iterar (recorrer) elementos de arrays, slices, mapas o canales.

**¿Para qué se usa?**
Para recorrer colecciones de forma segura sin tener que llevar un contador manual.

**Ejemplo:**
```go
package main

import "fmt"

func main() {
    numeros := []int{1, 2, 3}
    for indice, valor := range numeros {
        fmt.Printf("Índice %d: %d\n", indice, valor)
    }
}
```

**Errores comunes de principiante:**
- Olvidar que `range` devuelve DOS valores (índice y valor). Si solo quieres el valor, debes usar el identificador en blanco `_` para ignorar el índice: `for _, v := range lista`.

**Términos relacionados:** [`for`](#for)



### `defer`

**¿Qué es?**
Una instrucción que pospone la ejecución de una función hasta que la función actual termine (justo antes del return).

**¿Para qué se usa?**
Principalmente para asegurar la limpieza de recursos: cerrar archivos, liberar conexiones de base de datos o desbloquear mutexes.

**Ejemplo:**
```go
package main

import (
    "fmt"
    "os"
)

func main() {
    f, _ := os.Create("test.txt")
    defer f.Close() // Se ejecutará al final de main()
    fmt.Println("Archivo creado")
}
```

**Errores comunes de principiante:**
- Poner `defer` dentro de un bucle `for` gigante (se acumulan en memoria y solo se ejecutan al salir de la función, no del bucle).

**Términos relacionados:** [`func main()`](../go/01-fundamentos.md#package-main)
