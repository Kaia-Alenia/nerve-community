# 🐹 04 - Estructuras de datos

### `array`

**¿Qué es?**
Una secuencia numerada de elementos de un solo tipo con una longitud fija. En Go, la longitud de un array es parte de su tipo (ej. `[3]int` es diferente de `[4]int`).

**¿Para qué se usa?**
Se usa en casos específicos donde el tamaño exacto es conocido y no cambiará, o como la estructura de almacenamiento subyacente que respalda a los slices. Rara vez se usan directamente en código Go convencional comparado con los slices.

**Ejemplo:**
```go
package main

import "fmt"

func main() {
    // Declaración e inicialización de un array fijo de tamaño 3
    var numeros [3]int
    numeros[0] = 10
    numeros[1] = 20
    numeros[2] = 30
    
    // Forma corta
    colores := [2]string{"Rojo", "Azul"}
    
    fmt.Println(numeros, colores)
}
```

**Errores comunes de principiante:**
- Intentar pasar un array a una función esperando que se modifique. En Go, los arrays se pasan por valor (se copia todo el arreglo), a diferencia de C.
- Intentar usar `append()` con un array; no funciona, `append` es solo para slices.

**Términos relacionados:** [`slice`](#slice)

---

### `slice`

**¿Qué es?**
Un segmento dinámico y flexible sobre un array subyacente. A diferencia de los arrays, los slices no tienen un tamaño fijo en su tipo (`[]int`). Son mucho más comunes e idiomáticos en Go.

**¿Para qué se usa?**
Para manejar colecciones dinámicas de datos que pueden crecer o encogerse. Es la estructura de datos por defecto para listas en Go.

**Ejemplo:**
```go
package main

import "fmt"

func main() {
    // Declarando un slice directamente
    nombres := []string{"Ana", "Juan"}
    
    // Agregando elementos con append
    nombres = append(nombres, "Pedro")
    
    fmt.Println(nombres) // Imprime: [Ana Juan Pedro]
}
```

**Errores comunes de principiante:**
- Confundir la sintaxis de un array fijo `[3]int` con la de un slice `[]int`.
- No entender que múltiples slices pueden apuntar al mismo array subyacente; modificar uno puede alterar a otro si sus rangos se solapan.

**Términos relacionados:** [`array`](#array), [`append`](#append), [`make`](#make)

---

### `append`

**¿Qué es?**
Una función incorporada en Go (`built-in`) que añade elementos al final de un slice. Si el array subyacente del slice no tiene capacidad suficiente, `append` asignará un nuevo array más grande y copiará los elementos.

**¿Para qué se usa?**
Para agregar datos a un slice dinámicamente sin tener que gestionar la reserva de memoria de forma manual.

**Ejemplo:**
```go
package main

import "fmt"

func main() {
    numeros := []int{1, 2}
    
    // Agregando un elemento
    numeros = append(numeros, 3)
    
    // Agregando múltiples elementos
    numeros = append(numeros, 4, 5)
    
    fmt.Println(numeros) // Imprime: [1 2 3 4 5]
}
```

**Errores comunes de principiante:**
- Olvidar reasignar el resultado de `append` de vuelta a la variable (ej. escribir `append(numeros, 3)` en lugar de `numeros = append(numeros, 3)`), ya que `append` retorna un *nuevo* slice y no modifica la referencia original in-place.

**Términos relacionados:** [`slice`](#slice)

---

### `map`

**¿Qué es?**
Una colección de pares clave-valor desordenada (equivalente a diccionarios en Python o HashMaps en Java). Provee acceso constante O(1) en promedio.

**¿Para qué se usa?**
Para búsquedas rápidas, asociaciones de datos y conteos donde necesitas acceder a valores basados en una clave única que no es un índice numérico secuencial.

**Ejemplo:**
```go
package main

import "fmt"

func main() {
    // Inicialización usando make
    edades := make(map[string]int)
    edades["Ana"] = 30
    edades["Carlos"] = 25
    
    // Verificando si existe una clave (el ok idiom)
    edad, existe := edades["Juan"]
    if existe {
        fmt.Println("La edad de Juan es:", edad)
    } else {
        fmt.Println("Juan no está en el mapa")
    }
}
```

**Errores comunes de principiante:**
- Intentar escribir en un mapa declarado pero no inicializado (`var edades map[string]int`), lo cual provoca un 'panic' (nil map). Siempre se debe inicializar con `make` o con un literal `map[string]int{}`.

**Términos relacionados:** [`make`](#make)

---

### `make`

**¿Qué es?**
Una función incorporada (`built-in`) que se utiliza para reservar e inicializar memoria para *slices*, *maps*, y *channels*. A diferencia de `new`, `make` devuelve un valor inicializado listo para usar, no un puntero a un valor con ceros.

**¿Para qué se usa?**
Para inicializar tipos de datos dinámicos internos de Go de forma segura. Permite pre-asignar capacidad en los slices (para optimización) e inicializar mapas para evitar panics.

**Ejemplo:**
```go
package main

import "fmt"

func main() {
    // Creando un mapa listo para escribir
    diccionario := make(map[string]string)
    diccionario["Go"] = "Genial"
    
    // Creando un slice con longitud 0 y capacidad 10
    // Optimiza memoria si sabemos que agregaremos unos 10 elementos
    lista := make([]int, 0, 10)
    lista = append(lista, 5)
    
    fmt.Println(diccionario, lista)
}
```

**Errores comunes de principiante:**
- Usar `new` en lugar de `make` para crear un slice o un mapa, lo que resultará en un puntero inútil a un slice/map nulo.

**Términos relacionados:** [`slice`](#slice), [`map`](#map)
