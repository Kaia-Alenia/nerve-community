# 06 - Manejo de errores

### `Result<T, E>`

**¿Qué es?**
Un `enum` nativo que representa el éxito (`Ok(T)`) o el fracaso (`Err(E)`) de una operación. A diferencia de las excepciones en otros lenguajes, en Rust los errores son valores que se retornan explícitamente.

**¿Para qué se usa?**
Para forzar al programador a manejar posibles fallos en tiempo de compilación. Las funciones que pueden fallar (como abrir un archivo o parsear un número) devuelven un `Result`.

**Ejemplo:**
```rust
use std::fs::File;

fn main() {
    let archivo: Result<File, std::io::Error> = File::open("datos.txt");
    
    match archivo {
        Ok(file) => println!("Archivo abierto con éxito"),
        Err(error) => println!("Fallo al abrir: {}", error),
    }
}
```

**Errores comunes de principiante:**
- Dejar un `Result` sin evaluar. El compilador lanzará una advertencia (`unused Result that must be used`), indicando que estás ignorando un posible fallo que podría romper tu programa.

**Términos relacionados:** [`Option<T>`](#optiont), [`match`](../rust/02-control-de-flujo.md#match)

### `Option<T>`

**¿Qué es?**
Un `enum` nativo que representa la presencia (`Some(T)`) o ausencia (`None`) de un valor. Reemplaza el concepto de "nulo" (null) que existe en otros lenguajes.

**¿Para qué se usa?**
Para evitar los infames "Null Pointer Exceptions". Como Rust no tiene valores nulos, obliga a desempaquetar el `Option` explícitamente antes de poder usar el dato interno.

**Ejemplo:**
```rust
fn buscar_usuario(id: i32) -> Option<String> {
    if id == 1 {
        Some(String::from("Admin"))
    } else {
        None // Retorna explícitamente la ausencia
    }
}

fn main() {
    if let Some(nombre) = buscar_usuario(1) {
        println!("Usuario encontrado: {}", nombre);
    } else {
        println!("El usuario no existe");
    }
}
```

**Errores comunes de principiante:**
- Usar ciegamente el método `.unwrap()` sobre un `Option` para saltarse las validaciones de seguridad. Si el valor resulta ser `None`, el programa hará *panic* y se cerrará abruptamente.

**Términos relacionados:** [`Result<T, E>`](#resultt-e)

### `El operador ?`

**¿Qué es?**
Es un operador de propagación de errores. Se coloca al final de una llamada a función que retorna un `Result` o un `Option`.

**¿Para qué se usa?**
Para escribir código limpio sin anidar múltiples `match`. Si la función fue exitosa, extrae y devuelve el valor interno (el `Ok` o `Some`). Si falló, hace un `return` automático, propagando el error hacia la función llamadora.

**Ejemplo:**
```rust
use std::fs::File;
use std::io::Read;

// La función retorna un Result
fn leer_config() -> std::io::Result<String> {
    let mut archivo = File::open("config.txt")?; // Falla si no existe
    let mut contenido = String::new();
    archivo.read_to_string(&mut contenido)?;    // Falla si no puede leer
    Ok(contenido)
}

fn main() {
    // Ignoramos el resultado para el ejemplo
    let _ = leer_config();
}
```

**Errores comunes de principiante:**
- Intentar usar `?` dentro de una función (como `main` por defecto) que retorna la unidad `()` en lugar de un `Result` o `Option`, lo que causa un error de compilación.

**Términos relacionados:** [`Result<T, E>`](#resultt-e)

### `panic!`

**¿Qué es?**
Una macro de la librería estándar que detiene inmediatamente la ejecución del programa (o del hilo actual) e imprime un mensaje de error, desenrollando la pila de llamadas (stack unwinding).

**¿Para qué se usa?**
Solo para manejar errores irrecuperables, donde el programa ha entrado en un estado inconsistente y continuar su ejecución sería peligroso (ej. índice de array fuera de límites, corrupción de memoria).

**Ejemplo:**
```rust
fn main() {
    // Cambia esto a 5000 para ver el pánico
    let temperatura_reactor = 3000; 
    
    if temperatura_reactor > 4000 {
        panic!("¡Peligro! Fusión del núcleo inminente. Abortando.");
    }
    
    println!("Todo bajo control.");
}
```

**Errores comunes de principiante:**
- Usar `panic!` como reemplazo genérico de un manejo de errores robusto. Los pánicos deben ser la excepción absoluta, mientras que `Result` debe usarse para cualquier error previsible o recuperable.

**Términos relacionados:** [`Result<T, E>`](#resultt-e)
