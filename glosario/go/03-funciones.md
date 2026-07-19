# 03 - Funciones

### `func`

**¿Qué es?**
Palabra clave fundamental para definir una función en Go. A diferencia de lenguajes dinámicos, Go exige declarar explícitamente los tipos de todos los parámetros de entrada y los tipos de retorno, garantizando seguridad de tipos en tiempo de compilación.

**¿Para qué se usa?**
Para agrupar bloques de código reutilizable, modularizar la lógica de una aplicación y separar responsabilidades dentro de un paquete.

**Ejemplo:**
```go
package main

import "fmt"

func sumar(a int, b int) int {
    return a + b
}

func main() {
    resultado := sumar(2, 3)
    fmt.Println("La suma es:", resultado)
}
```

**Errores comunes de principiante:**
- Olvidar especificar el tipo de retorno en la firma de la función, provocando un error de compilación.
- Colocar la llave de apertura `{` en la línea siguiente en lugar de en la misma línea de la firma, lo que rompe la compilación por el punto y coma implícito.

**Términos relacionados:** [`múltiples retornos`](#múltiples-retornos)

---

### `múltiples retornos`

**¿Qué es?**
La capacidad nativa de las funciones en Go para devolver más de un valor al mismo tiempo. Es un patrón central en el lenguaje, especialmente utilizado para el manejo de errores.

**¿Para qué se usa?**
Su uso más idiomático es devolver el resultado de una operación exitosa como primer valor, y un valor de tipo `error` como segundo valor. Esto obliga al desarrollador a lidiar con las fallas explícitamente.

**Ejemplo:**
```go
package main

import (
    "fmt"
    "errors"
)

func dividir(a, b float64) (float64, error) {
    if b == 0 {
        return 0, errors.New("división por cero")
    }
    return a / b, nil
}

func main() {
    res, err := dividir(10.0, 2.0)
    if err != nil {
        fmt.Println("Error:", err)
    } else {
        fmt.Println("Resultado:", res)
    }
}
```

**Errores comunes de principiante:**
- Ignorar silenciosamente el segundo valor (el error) asignándolo al identificador en blanco `_`, lo que puede llevar a que la aplicación falle inesperadamente más adelante.

**Términos relacionados:** [`manejo de errores`](../go/06-manejo-de-errores.md#error-interfaz), [`func`](#func)

---

### `defer`

**¿Qué es?**
Una instrucción que pospone la ejecución de una función hasta que la función que la contiene haya terminado (ya sea que regrese normalmente o por un pánico). 

**¿Para qué se usa?**
Es indispensable para liberar recursos de forma segura y legible, como cerrar archivos, conexiones de red o liberar candados (mutex), asegurando que se ejecuten sin importar cuántas ramas de retorno tenga la función.

**Ejemplo:**
```go
package main

import "fmt"

func procesar() {
    fmt.Println("Abriendo archivo...")
    defer fmt.Println("Cerrando archivo (ejecutado al final)")
    
    fmt.Println("Leyendo datos...")
    // Si hubiera un error o un return aquí, el defer aún se ejecuta.
}

func main() {
    procesar()
}
```

**Errores comunes de principiante:**
- Usar `defer` dentro de un bucle `for` muy grande (ej. abriendo miles de archivos). Como los `defer` se acumulan en memoria y solo se ejecutan al salir de la función, esto puede agotar la memoria o los descriptores de archivo.
- Asumir el orden de ejecución: los múltiples `defer` se ejecutan en orden LIFO (último en entrar, primero en salir).

**Términos relacionados:** [`func`](#func)

---

### `funciones variádicas`

**¿Qué es?**
Son funciones que pueden aceptar un número variable de argumentos del mismo tipo utilizando la sintaxis `...` antes del tipo del parámetro. 

**¿Para qué se usa?**
Para crear APIs más flexibles donde no se conoce de antemano cuántos argumentos se pasarán, evitando la necesidad de obligar al usuario a crear un slice (array dinámico) manualmente. La función `fmt.Println` es el ejemplo más famoso.

**Ejemplo:**
```go
package main

import "fmt"

func sumarTodos(numeros ...int) int {
    total := 0
    // "numeros" es tratado como un slice de int dentro de la función
    for _, num := range numeros {
        total += num
    }
    return total
}

func main() {
    fmt.Println(sumarTodos(1, 2, 3))       // Imprime 6
    fmt.Println(sumarTodos(10, 20, 30, 40)) // Imprime 100
}
```

**Errores comunes de principiante:**
- Intentar colocar un parámetro normal después del parámetro variádico. El parámetro `...` debe ser estrictamente el último argumento en la firma de la función.
- Olvidar desempaquetar un slice existente al pasarlo a la función variádica usando la misma sintaxis `...` (ej. `sumarTodos(misNumeros...)`).

**Términos relacionados:** [`func`](#func)
