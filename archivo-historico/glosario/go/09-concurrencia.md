# 09 - Concurrencia

### `goroutine`

**¿Qué es?**
Una goroutine es una función que se ejecuta de manera concurrente con otras goroutines en el mismo espacio de direcciones. Son gestionadas por el runtime de Go, no por el sistema operativo, lo que las hace extremadamente ligeras (ocupan unos pocos kilobytes de memoria inicial). 

**¿Para qué se usa?**
Para realizar programación concurrente de forma sencilla utilizando la palabra clave `go` delante de una llamada a función. Permite realizar múltiples tareas al mismo tiempo (ej. manejar miles de peticiones web concurrentes) sin el gran coste de memoria de los hilos (threads) tradicionales.

**Ejemplo:**
```go
package main

import (
    "fmt"
    "time"
)

func tarea(id int) {
    fmt.Printf("Tarea %d en ejecución\n", id)
}

func main() {
    // Lanzar concurrentemente
    go tarea(1)
    go tarea(2)
    
    // Pequeña pausa para dar tiempo a que terminen antes de que main() salga
    time.Sleep(100 * time.Millisecond)
    fmt.Println("Main terminado")
}
```

**Errores comunes de principiante:**
- Olvidar que la función `main` es en sí misma una goroutine. Si `main` termina, todas las demás goroutines se destruyen abruptamente sin importar si terminaron su trabajo. Nunca confíes en `time.Sleep` en código real.

**Términos relacionados:** [`sync.WaitGroup`](#syncwaitgroup)

---

### `channel`

**¿Qué es?**
Un canal (`channel`) es un conducto tipado a través del cual puedes enviar y recibir valores mediante el operador de canal, `<-`. Sigue la filosofía de Go: "No te comuniques compartiendo memoria; comparte memoria comunicándote".

**¿Para qué se usa?**
Para sincronizar la ejecución de múltiples goroutines y transferir datos de forma segura entre ellas sin necesidad de usar candados explícitos (mutexes).

**Ejemplo:**
```go
package main

import "fmt"

func productor(c chan string) {
    c <- "mensaje desde goroutine" // Envía un valor al canal
}

func main() {
    // Se inicializa el canal con make
    c := make(chan string)
    
    go productor(c)
    
    // Bloquea hasta recibir un valor del canal
    mensaje := <-c 
    fmt.Println("Recibido:", mensaje)
}
```

**Errores comunes de principiante:**
- Deadlocks (bloqueo mutuo). Si una goroutine intenta recibir de un canal, bloqueará para siempre hasta que otra envíe. Si todas las goroutines están dormidas, Go detectará el deadlock y hará panic.
- Intentar enviar datos a un canal cerrado, lo que provocará un panic.

**Términos relacionados:** [`goroutine`](#goroutine), [`select`](#select)

---

### `select`

**¿Qué es?**
Una estructura de control, similar a un `switch`, pero exclusiva para canales. Permite que una goroutine espere múltiples operaciones de comunicación concurrente.

**¿Para qué se usa?**
Para "multiplexar" canales. Permite gestionar tiempos de espera (timeouts), enviar/recibir sin bloquear si el canal no está listo (usando `default`), y manejar múltiples canales al mismo tiempo de forma elegante.

**Ejemplo:**
```go
package main

import (
    "fmt"
    "time"
)

func main() {
    c1 := make(chan string)
    c2 := make(chan string)

    go func() {
        time.Sleep(1 * time.Second)
        c1 <- "resultado 1"
    }()
    
    go func() {
        time.Sleep(2 * time.Second)
        c2 <- "resultado 2"
    }()

    for i := 0; i < 2; i++ {
        select {
        case msg1 := <-c1:
            fmt.Println("Recibido de c1:", msg1)
        case msg2 := <-c2:
            fmt.Println("Recibido de c2:", msg2)
        }
    }
}
```

**Errores comunes de principiante:**
- Usar un bucle infinito for-select sin incluir una condición de salida u olvidando manejar cuando el canal se cierra, provocando un consumo del 100% de CPU.

**Términos relacionados:** [`channel`](#channel)

---

### `sync.WaitGroup`

**¿Qué es?**
Una estructura del paquete estándar `sync` que actúa como un contador seguro para concurrencia. Permite esperar a que un conjunto (grupo) de goroutines terminen su ejecución.

**¿Para qué se usa?**
Es la forma idiomática y correcta (en lugar de `time.Sleep`) para decirle a la función `main` que debe pausarse y esperar a que todas las tareas en background finalicen antes de cerrar el programa.

**Ejemplo:**
```go
package main

import (
    "fmt"
    "sync"
)

func worker(id int, wg *sync.WaitGroup) {
    // Al finalizar, decrementa el contador en 1
    defer wg.Done()
    fmt.Printf("Worker %d trabajando...\n", id)
}

func main() {
    var wg sync.WaitGroup

    for i := 1; i <= 3; i++ {
        wg.Add(1) // Incrementa el contador en 1 por cada goroutine
        go worker(i, &wg)
    }

    // Bloquea hasta que el contador vuelva a 0
    wg.Wait()
    fmt.Println("Todos los workers finalizaron")
}
```

**Errores comunes de principiante:**
- Pasar el `sync.WaitGroup` a la goroutine por valor en lugar de por puntero (`*sync.WaitGroup`). Si se pasa por valor, se copia y el `Wait()` original nunca se enterará del `Done()`, generando un deadlock.
- Llamar a `wg.Add(1)` *dentro* de la goroutine. Debe llamarse siempre en el hilo principal antes de lanzar el `go`, o podría darse el caso de que `Wait()` evalúe antes de que se haya ejecutado el `Add(1)`.

**Términos relacionados:** [`goroutine`](#goroutine)
