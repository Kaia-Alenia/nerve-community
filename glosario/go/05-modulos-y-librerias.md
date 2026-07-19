# 🐹 05 - Módulos y librerías

### `módulo (go mod)`

**¿Qué es?**
Un módulo es una colección de paquetes de Go que se versionan juntos. Representa la unidad de distribución en Go y se define mediante un archivo `go.mod` en la raíz del proyecto.

**¿Para qué se usa?**
Para gestionar las dependencias de tu proyecto de manera oficial y determinista. `go mod init` inicializa el módulo y `go get` descarga e instala dependencias de terceros, actualizando el `go.mod` y el `go.sum` (para seguridad de las descargas).

**Ejemplo:**
```bash
# Inicializa el módulo en la carpeta actual
go mod init github.com/miusuario/miproyecto

# Descarga una librería de terceros (ej. un enrutador web)
go get github.com/go-chi/chi/v5
```

**Errores comunes de principiante:**
- Intentar ejecutar `go get` en una carpeta que no ha sido inicializada con `go mod init`. Go necesita el archivo `go.mod` para registrar la dependencia.
- Usar `go get fmt` o `go get os`. Los paquetes de la biblioteca estándar vienen integrados en el compilador y no se descargan.

**Términos relacionados:** [`paquete (package)`](#paquete-package)

---

### `paquete (package)`

**¿Qué es?**
Un paquete (`package`) es la forma en que Go agrupa código relacionado (funciones, tipos, variables) dentro de un mismo directorio. Todo archivo de Go debe pertenecer a un paquete.

**¿Para qué se usa?**
Para encapsular lógica, evitar colisiones de nombres y organizar arquitectónicamente el código. El paquete `main` es especial: le indica al compilador que debe crear un archivo ejecutable, mientras que cualquier otro nombre de paquete compila como una librería.

**Ejemplo:**
```go
package matematicas

// Una función con mayúscula inicial (Sumar) se exporta y puede usarse desde otros paquetes.
func Sumar(a, b int) int {
    return a + b
}

// Una función con minúscula (restar) es privada de este paquete.
func restar(a, b int) int {
    return a - b
}
```

**Errores comunes de principiante:**
- Declarar dos nombres de paquete diferentes para archivos que viven en la misma carpeta. Todos los archivos `.go` en un mismo directorio deben declarar el mismo `package`.

**Términos relacionados:** [`import`](#import)

---

### `import`

**¿Qué es?**
La instrucción utilizada para incluir otros paquetes (tanto de la biblioteca estándar como de terceros, o locales de tu propio módulo) dentro de un archivo Go para poder usar su código exportado.

**¿Para qué se usa?**
Para acceder a funciones, interfaces y tipos definidos fuera del paquete actual.

**Ejemplo:**
```go
package main

import (
    "fmt"
    "os"
    "strings"
)

func main() {
    texto := "hola mundo"
    textoMayusculas := strings.ToUpper(texto)
    fmt.Println(textoMayusculas)
    fmt.Println("Argumentos CLI:", os.Args)
}
```

**Errores comunes de principiante:**
- Importar un paquete y no utilizarlo en el código. A diferencia de otros lenguajes, Go es estricto y producirá un error de compilación (`imported and not used`), obligando a mantener el código limpio.
- Importación circular (el Paquete A importa al B, y el B importa al A). Go no lo permite y fallará la compilación.

**Términos relacionados:** [`paquete (package)`](#paquete-package)

---

### `go run / go build`

**¿Qué es?**
Son los comandos principales de la CLI de Go para compilar y ejecutar código. `go run` compila el código en memoria, lo ejecuta y limpia los archivos temporales. `go build` compila el código y genera un archivo binario ejecutable estático.

**¿Para qué se usa?**
`go run` se utiliza constantemente durante la fase de desarrollo para iterar rápido. `go build` se utiliza en la fase de despliegue para generar el artefacto final que irá a producción.

**Ejemplo:**
```bash
# Compilar y ejecutar rápidamente (ideal para desarrollo)
go run main.go

# Generar un archivo binario llamado "mi_app" (ideal para despliegue)
go build -o mi_app main.go

# Ejecutar el binario generado
./mi_app
```

**Errores comunes de principiante:**
- Ejecutar `go build`, ver que no se imprime nada en la consola y pensar que falló. `go build` es silencioso si tiene éxito; solo genera el archivo. Debes ejecutar el archivo resultante manualmente.

**Términos relacionados:** [`módulo (go mod)`](#módulo-go-mod)
