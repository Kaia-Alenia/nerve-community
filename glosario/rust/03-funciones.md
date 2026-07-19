# 🦀 03 - Funciones

### `fn`

**¿Qué es?**
La palabra clave utilizada para declarar funciones. En Rust, las firmas de las funciones deben especificar estáticamente los tipos de todos los argumentos y el tipo del valor de retorno.

**¿Para qué se usa?**
Para encapsular lógica reutilizable. Al exigir tipos explícitos en la interfaz (los parámetros), el compilador de Rust puede inferir los tipos del cuerpo interno de forma más eficiente.

**Ejemplo:**
```rust
// Parámetros y retorno con tipos explícitos
fn sumar(a: i32, b: i32) -> i32 {
    a + b // Sin punto y coma para retornar
}

fn main() {
    println!("La suma es: {}", sumar(2, 3));
}
```

**Errores comunes de principiante:**
- Omitir el tipo de dato de un parámetro, lo cual generará un error de sintaxis porque Rust no hace inferencia global de tipos en firmas de funciones.

**Términos relacionados:** [`Retorno implícito vs explícito`](#retorno-implícito-vs-explícito)

### `Retorno implícito vs explícito`

**¿Qué es?**
En Rust, la última expresión de un bloque que no termina en punto y coma (`;`) se devuelve automáticamente (retorno implícito). El `return` explícito también existe, pero se reserva para salidas prematuras.

**¿Para qué se usa?**
Hace que el código sea más idiomático, limpio y cercano a lenguajes funcionales.

**Ejemplo:**
```rust
fn calcular_descuento(precio: f64) -> f64 {
    if precio > 100.0 {
        return precio * 0.8; // Retorno explícito (salida prematura)
    }
    precio * 0.9 // Retorno implícito (última línea sin punto y coma)
}

fn main() {
    println!("Total: {}", calcular_descuento(50.0));
}
```

**Errores comunes de principiante:**
- Poner un punto y coma al final de la última línea que se pretende retornar (ej. `a + b;`). Esto convierte la expresión en una instrucción (statement) que retorna la unidad `()`, fallando la compilación por incompatibilidad de tipos.

**Términos relacionados:** [`fn`](#fn)

### `Closures (Clausuras)`

**¿Qué es?**
Funciones anónimas que pueden capturar variables de su entorno o ámbito donde fueron definidas. Se definen utilizando barras verticales `|param1|` en lugar de paréntesis.

**¿Para qué se usa?**
Son omnipresentes en Rust al trabajar con iteradores o hilos (threads). Permiten pasar lógicas concisas como argumentos (callbacks) sin la verbosidad de definir una función estándar con `fn`.

**Ejemplo:**
```rust
fn main() {
    let factor = 2;
    // Closure que captura 'factor' del entorno
    let multiplicar = |num: i32| -> i32 { num * factor };
    
    // Forma aún más corta con inferencia
    let multiplicar_corto = |num| num * factor;
    
    println!("Resultado: {}", multiplicar(5)); // Imprime 10
    println!("Resultado corto: {}", multiplicar_corto(5)); // Imprime 10
}
```

**Errores comunes de principiante:**
- No usar la palabra clave `move` delante del closure cuando se intenta enviar a otro hilo de ejecución, lo que causaría que el closure intente usar referencias a datos que podrían ya no existir en la memoria.

**Términos relacionados:** [`fn`](#fn)

### `Métodos (impl)`

**¿Qué es?**
Son funciones que están adjuntas a una estructura de datos particular (`struct` o `enum`). El primer parámetro de un método siempre es `self` (la instancia sobre la cual se está llamando).

**¿Para qué se usa?**
Para emular el comportamiento de programación orientada a objetos (POO), aglomerando los datos y las funciones que actúan sobre esos datos en una misma interfaz cohesiva.

**Ejemplo:**
```rust
struct Rectangulo {
    ancho: u32,
    alto: u32,
}

impl Rectangulo {
    // Método asociado al struct
    fn area(&self) -> u32 {
        self.ancho * self.alto
    }
}

fn main() {
    let rect = Rectangulo { ancho: 10, alto: 5 };
    println!("Área: {}", rect.area());
}
```

**Errores comunes de principiante:**
- Olvidar poner `&self` (referencia) y poner solo `self`, lo que provoca que el método tome posesión total (*ownership*) del objeto, consumiéndolo e impidiendo que pueda ser usado de nuevo después de la llamada.

**Términos relacionados:** [`POO básica`](../rust/08-poo-basica.md#struct-e-impl)
