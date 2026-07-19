# 08 - POO básica (Structs e Interfaces)

### `struct`

**¿Qué es?**
Una colección tipada de campos de datos. Dado que Go no tiene el concepto de "clases", los `structs` son el mecanismo principal para agrupar datos relacionados y modelar entidades u objetos complejos.

**¿Para qué se usa?**
Para definir la estructura de los datos (el estado) de tu aplicación, como usuarios, configuraciones, respuestas HTTP, etc. 

**Ejemplo:**
```go
package main

import "fmt"

type Persona struct {
    Nombre   string
    Edad     int
    isActive bool // Campo privado al paquete (empieza con minúscula)
}

func main() {
    // Instanciación
    p := Persona{
        Nombre: "Ana",
        Edad:   30,
    }
    fmt.Printf("%+v\n", p)
}
```

**Errores comunes de principiante:**
- Escribir los nombres de los campos en minúscula (ej. `nombre string`) esperando que se serialicen a JSON o se accedan desde otros paquetes. En Go, solo los campos que empiezan con letra Mayúscula son exportados (públicos).

**Términos relacionados:** [`métodos`](#métodos), [`composición`](#composición-embedding)

---

### `métodos`

**¿Qué es?**
Son funciones especiales que incluyen un argumento receptor (receiver) entre la palabra clave `func` y el nombre de la función. Este receptor enlaza la función al tipo (generalmente un `struct`).

**¿Para qué se usa?**
Para definir el comportamiento asociado a un tipo de dato, simulando los métodos de las clases en la Programación Orientada a Objetos tradicional.

**Ejemplo:**
```go
package main

import "fmt"

type Contador struct {
    valor int
}

// Receptor por valor (no modifica el original)
func (c Contador) Mostrar() {
    fmt.Println("Valor:", c.valor)
}

// Receptor por puntero (puede modificar el original)
func (c *Contador) Incrementar() {
    c.valor++
}

func main() {
    c := Contador{valor: 0}
    c.Incrementar()
    c.Mostrar() // Imprime: Valor: 1
}
```

**Errores comunes de principiante:**
- Usar un receptor por valor (`func (c Contador)`) cuando el método necesita modificar el estado interno del struct. Esto modificará solo una copia; siempre usa punteros (`*Contador`) si vas a mutar datos.

**Términos relacionados:** [`struct`](#struct)

---

### `interface`

**¿Qué es?**
Un tipo abstracto que define un conjunto de firmas de métodos. La magia de Go es que las interfaces se implementan **implícitamente** (duck typing estructural): si un tipo tiene todos los métodos que pide la interfaz, entonces implementa la interfaz, sin usar la palabra `implements`.

**¿Para qué se usa?**
Para escribir código genérico, polimórfico y desacoplado, permitiendo, por ejemplo, inyectar dependencias y facilitar los tests (creando mocks).

**Ejemplo:**
```go
package main

import "fmt"

// Interfaz
type Hablador interface {
    Hablar() string
}

// Struct 1
type Perro struct{}
func (p Perro) Hablar() string { return "Guau" }

// Struct 2
type Gato struct{}
func (g Gato) Hablar() string { return "Miau" }

// Función polimórfica
func HacerSonido(h Hablador) {
    fmt.Println(h.Hablar())
}

func main() {
    HacerSonido(Perro{})
    HacerSonido(Gato{})
}
```

**Errores comunes de principiante:**
- Crear interfaces monolíticas con decenas de métodos. En Go, lo idiomático son interfaces pequeñas y específicas, frecuentemente de un solo método (como `io.Reader` o `fmt.Stringer`).

**Términos relacionados:** [`struct`](#struct)

---

### `composición (embedding)`

**¿Qué es?**
Es el mecanismo de Go para la reutilización de código en lugar de la herencia (Go no tiene `extends`). Permite incrustar (embed) un struct dentro de otro de forma anónima, de modo que el struct contenedor "hereda" directamente los campos y métodos del struct incrustado.

**¿Para qué se usa?**
Para componer comportamientos complejos a partir de piezas más pequeñas, favoreciendo el principio de "composición sobre herencia".

**Ejemplo:**
```go
package main

import "fmt"

type Vehiculo struct {
    Marca string
}

func (v Vehiculo) TocarBocina() {
    fmt.Println("Beep beep!")
}

// Auto "hereda" (compone) Vehiculo
type Auto struct {
    Vehiculo
    Ruedas int
}

func main() {
    miAuto := Auto{
        Vehiculo: Vehiculo{Marca: "Toyota"},
        Ruedas:   4,
    }
    
    // Podemos acceder a los campos y métodos directamente
    fmt.Println(miAuto.Marca)
    miAuto.TocarBocina()
}
```

**Errores comunes de principiante:**
- Pensar en la composición exactamente como herencia (polimorfismo subtipo). Un `Auto` *tiene* un `Vehiculo`, pero un `Auto` *no es* estrictamente del tipo `Vehiculo` (no puedes pasar un `Auto` a una función que espera un `Vehiculo` a menos que uses interfaces).

**Términos relacionados:** [`struct`](#struct)
