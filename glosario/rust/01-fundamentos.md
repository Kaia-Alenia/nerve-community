# 🦀 01 - Fundamentos

### `let` y `mut`

**¿Qué es?**
`let` es la palabra clave para declarar variables en Rust. Por defecto, todas las variables son inmutables (no pueden cambiar su valor una vez asignado). Para permitir la mutabilidad, se debe usar explícitamente `let mut`.

**¿Para qué se usa?**
Para almacenar datos en memoria. La inmutabilidad por defecto fomenta la seguridad y previene bugs de concurrencia, obligando al programador a ser explícito sobre qué datos van a cambiar de estado a lo largo del tiempo.

**Ejemplo:**
```rust
fn main() {
    let nombre = "Ana"; // Inmutable, seguro de compartir
    let mut edad = 30;  // Mutable, puede reasignarse
    
    edad += 1;
    println!("{} tiene {} años", nombre, edad);
}
```

**Errores comunes de principiante:**
- Intentar reasignar o modificar una variable declarada solo con `let`, causando el error de compilación `cannot assign twice to immutable variable`.

**Términos relacionados:** [`Constantes`](#constantes-const), [`Shadowing`](#shadowing-sombreo)

### `Tipos de datos escalares`

**¿Qué es?**
Rust tiene un tipado estático muy fuerte. Los escalares representan un valor único e incluyen: enteros (`i32`, `u64`), punto flotante (`f32`, `f64`), booleanos (`bool`), y caracteres Unicode de 4 bytes (`char`).

**¿Para qué se usa?**
Son los bloques de construcción básicos para datos más complejos. Especificar el tamaño exacto (ej. `i8` vs `i64`) ayuda a optimizar el uso de memoria de manera determinista sin depender de un Garbage Collector.

**Ejemplo:**
```rust
fn main() {
    let entero: i32 = -50;
    let flotante: f64 = 3.1415;
    let activo: bool = true;
    let letra: char = '🦀'; // Soporta emojis de forma nativa
    
    println!("{} {} {} {}", entero, flotante, activo, letra);
}
```

**Errores comunes de principiante:**
- Asignar un número decimal a una variable que el compilador infirió como entero, o intentar sumar un `i32` con un `i64` directamente (Rust no hace coerción implícita de tipos, debes usar `as`).

**Términos relacionados:** [`let y mut`](#let-y-mut)

### `Shadowing (Sombreo)`

**¿Qué es?**
La capacidad de declarar una nueva variable con el mismo nombre que una variable anterior. La nueva variable "hace sombra" a la primera, reemplazándola en el alcance actual. Puede incluso cambiar el tipo de dato.

**¿Para qué se usa?**
Para evitar tener que inventar nombres distintos (ej. `espacios_str` y `espacios_num`) cuando solo quieres transformar un dato de un formato a otro y no necesitas conservar el valor original.

**Ejemplo:**
```rust
fn main() {
    let espacios = "   ";
    // Shadowing: reutilizamos el nombre pero cambiamos a número
    let espacios = espacios.len(); 
    
    println!("Hay {} espacios", espacios);
}
```

**Errores comunes de principiante:**
- Confundir *shadowing* (usando de nuevo `let`) con mutabilidad (usando `mut`). Si usas `mut`, no puedes cambiar el tipo de dato; si usas *shadowing*, estás creando una variable nueva en memoria, por lo que sí puedes cambiar el tipo.

**Términos relacionados:** [`let y mut`](#let-y-mut)

### `Constantes (const)`

**¿Qué es?**
Valores atados a un nombre que nunca pueden cambiar, no solo inmutables por defecto, sino siempre inmutables. Deben ser anotados explícitamente con su tipo y evaluables en tiempo de compilación.

**¿Para qué se usa?**
Para definir valores fijos en el programa (como configuraciones, límites máximos, rutas físicas) que pueden ser usados globalmente en cualquier ámbito.

**Ejemplo:**
```rust
const MAX_CONEXIONES: u32 = 100_000;

fn main() {
    println!("El servidor soporta hasta {} conexiones", MAX_CONEXIONES);
}
```

**Errores comunes de principiante:**
- Omitir el tipo de dato al declarar una constante, lo que provocará un error de compilación inmediato (`missing type for const item`).
- Intentar asignar a una constante el resultado de una función que se evalúa en tiempo de ejecución.

**Términos relacionados:** [`let y mut`](#let-y-mut)
