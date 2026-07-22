# 02 - Control de flujo

### `if / else / if let`

**¿Qué es?**
Estructuras condicionales que, a diferencia de lenguajes de la familia C, no requieren paréntesis alrededor de la condición y actúan como expresiones (pueden devolver un valor).

**¿Para qué se usa?**
Para la toma de decisiones lógicas. Al ser expresiones, evitan la necesidad de declarar variables mutables previas solo para asignarles un valor basado en una condición.

**Ejemplo:**
```rust
fn main() {
    let edad = 20;
    
    // Asignación directa porque 'if' es una expresión
    let estado = if edad >= 18 { "Adulto" } else { "Menor" };
    
    println!("El usuario es: {}", estado);
}
```

**Errores comunes de principiante:**
- Poner un punto y coma `;` al final de la expresión dentro de las llaves del `if` cuando se intenta retornar un valor para asignarlo a una variable.

**Términos relacionados:** [`match`](#match)

### `loop / while / for`

**¿Qué es?**
Los tres bucles nativos de Rust. `loop` es un bucle infinito incondicional, `while` repite mientras una condición sea verdadera, y `for` itera de manera segura sobre colecciones (iteradores).

**¿Para qué se usa?**
Para repetir tareas. `for` es el más usado en Rust por ser seguro contra desbordamientos (out-of-bounds), mientras que `loop` es útil para reintentos de conexión donde devuelves un valor al hacer `break`.

**Ejemplo:**
```rust
fn main() {
    // Bucle for sobre un rango (1 a 4)
    for i in 1..5 {
        print!("{} ", i);
    }
    
    let mut contador = 0;
    // Bucle infinito que devuelve un valor al romperse
    let resultado = loop {
        contador += 1;
        if contador == 10 { break contador * 2; }
    };
    println!("\nResultado del loop: {}", resultado);
}
```

**Errores comunes de principiante:**
- Modificar manualmente un índice dentro de un bucle `while` para iterar arrays, en lugar de usar `for x in arr.iter()`, lo que es más lento (por validaciones de límites en cada ciclo) y propenso a pánicos.

**Términos relacionados:** [`break y continue`](#break-y-continue)

### `match`

**¿Qué es?**
Una estructura de control de flujo extremadamente poderosa que compara un valor contra una serie de patrones exhaustivos (similar a `switch` en otros lenguajes, pero mucho más estricto y expresivo).

**¿Para qué se usa?**
Para bifurcar lógica basándose en el estado o tipo de un valor. Desempaqueta limpiamente valores de enums (como `Option` o `Result`) forzando al desarrollador a manejar todos los casos posibles.

**Ejemplo:**
```rust
fn main() {
    let codigo_http = 404;
    
    let mensaje = match codigo_http {
        200 => "OK",
        400 | 401 | 403 => "Error de cliente",
        404 => "No encontrado",
        _ => "Código desconocido", // El '_' es el caso por defecto
    };
    println!("Estado: {}", mensaje);
}
```

**Errores comunes de principiante:**
- No cubrir todos los casos posibles. A diferencia de un switch de C, el compilador de Rust no te dejará compilar si el `match` no es exhaustivo (si falta el comodín `_` o algún patrón).

**Términos relacionados:** [`if let`](#if--else--if-let)

### `break y continue`

**¿Qué es?**
Instrucciones de salto dentro de iteraciones. `break` interrumpe y sale del bucle actual de inmediato, mientras que `continue` salta el resto de la iteración actual y pasa a la siguiente.

**¿Para qué se usa?**
Para controlar el flujo fino dentro de bucles, como abortar una búsqueda cuando se encuentra el objetivo o ignorar elementos que no cumplen ciertas condiciones sin anidar múltiples `if`.

**Ejemplo:**
```rust
fn main() {
    for i in 1..=10 {
        if i % 2 == 0 {
            continue; // Salta los pares
        }
        if i > 7 {
            break; // Rompe el bucle antes del 9
        }
        println!("Impar: {}", i);
    }
}
```

**Errores comunes de principiante:**
- Intentar usar `break` fuera de un bucle, o usarlo para retornar valores en bucles `while` y `for` (solo el bucle `loop` permite usar `break` para retornar un valor evaluado).

**Términos relacionados:** [`loop / while / for`](#loop--while--for)
