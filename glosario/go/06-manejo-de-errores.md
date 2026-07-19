# 06 - Manejo de errores

### `error (interfaz)`

**¿Qué es?**
En Go, `error` es un tipo de interfaz integrada (`built-in`) que representa un estado de error. Cualquier tipo que implemente el método `Error() string` satisface la interfaz `error`. Go no tiene excepciones (`try/catch`); los errores son tratados como valores ordinarios.

**¿Para qué se usa?**
Para indicar que una función no pudo completar su tarea. Se utiliza comúnmente como el último valor devuelto en funciones que tienen múltiples retornos, forzando al programador a decidir explícitamente cómo manejar la falla.

**Ejemplo:**
```go
package main

import (
    "fmt"
    "errors"
)

func hacerAlgo() (string, error) {
    // Retornamos un error vacío ("") y un error instanciado
    return "", errors.New("algo falló en la operación")
}

func main() {
    resultado, err := hacerAlgo()
    if err != nil {
        fmt.Println("Hubo un error:", err)
        return
    }
    fmt.Println(resultado)
}
```

**Errores comunes de principiante:**
- Ignorar los errores asignándolos al identificador en blanco `_` (ej. `res, _ := hacerAlgo()`), lo que oculta fallas graves y hace que el programa sea inestable.

**Términos relacionados:** [`if err != nil`](#if-err--nil), [`múltiples retornos`](../go/03-funciones.md#múltiples-retornos)

---

### `if err != nil`

**¿Qué es?**
El patrón (idiom) más ubicuo en Go para verificar y gestionar errores. Es la forma en la que se comprueba si el valor de la interfaz `error` contiene algo (no es nulo).

**¿Para qué se usa?**
Para evaluar el éxito de la operación anterior. Dado que Go no tiene un bloque `catch` para interceptar fallas ocultas, debes escribir esta evaluación constantemente para interceptar y manejar el flujo de fallos inmediatamente.

**Ejemplo:**
```go
package main

import (
    "fmt"
    "os"
)

func main() {
    _, err := os.Open("archivo-inexistente.txt")
    if err != nil {
        // Manejamos el error e interrumpimos el flujo
        fmt.Println("No se pudo abrir:", err)
        return
    }
    fmt.Println("Archivo abierto exitosamente")
}
```

**Errores comunes de principiante:**
- Quejarse de la repetitividad de escribir este bloque y tratar de abstraerlo incorrectamente. Escribirlo es intencional por diseño: hace que el manejo de errores sea explícito y fácil de auditar.

**Términos relacionados:** [`error (interfaz)`](#error-interfaz)

---

### `panic`

**¿Qué es?**
Una función integrada que detiene el flujo normal de control e inicia el proceso de "pánico" (panicking). Es lo más parecido a lanzar una excepción no capturada en otros lenguajes.

**¿Para qué se usa?**
Debe usarse **exclusivamente** para errores verdaderamente excepcionales y fatales donde el programa no puede o no debe continuar (por ejemplo, si falla la inicialización de la base de datos al arrancar el servidor). No se usa para errores esperados de negocio.

**Ejemplo:**
```go
package main

import "fmt"

func cargarConfiguracion() {
    // Simulamos un fallo crítico
    panic("No se pudo cargar la configuración de la base de datos")
}

func main() {
    defer func() { recover() }() // Evitar que el test automático falle
    fmt.Println("Iniciando sistema...")
    cargarConfiguracion()
    fmt.Println("Esta línea nunca se ejecutará")
}
```

**Errores comunes de principiante:**
- Usar `panic` como reemplazo de `try/catch` o para retornar errores regulares de funciones, violando las prácticas idiomáticas de Go (los errores deben retornarse como valores).

**Términos relacionados:** [`recover`](#recover), [`error (interfaz)`](#error-interfaz)

---

### `recover`

**¿Qué es?**
Una función integrada que recupera el control de una goroutine (hilo ligero) que está en estado de pánico, deteniendo la propagación del pánico y permitiendo que la aplicación continúe ejecutándose.

**¿Para qué se usa?**
Solo es útil cuando se llama directamente dentro de una función diferida (`defer`). Se usa en frameworks web o sistemas resilientes para atrapar pánicos imprevistos y evitar que un solo error tire abajo todo el servidor.

**Ejemplo:**
```go
package main

import "fmt"

func servidor() {
    // defer se asegura de que recover() se ejecute cuando haya un pánico
    defer func() {
        if r := recover(); r != nil {
            fmt.Println("El servidor se recuperó de un pánico:", r)
        }
    }()

    fmt.Println("Procesando petición...")
    panic("Oops, desbordamiento de memoria")
    // fmt.Println("Esto no se ejecuta") // Código inalcanzable (comentado para evitar error del compilador)
}

func main() {
    servidor()
    fmt.Println("El programa principal sigue ejecutándose normalmente")
}
```

**Errores comunes de principiante:**
- Llamar a `recover()` fuera de un `defer`, donde no tiene absolutamente ningún efecto.
- Usar `panic`/`recover` abusivamente para simular `try/catch/finally`.

**Términos relacionados:** [`panic`](#panic), [`defer`](../go/03-funciones.md#defer)
