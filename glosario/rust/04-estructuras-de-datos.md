# 🦀 04 - Estructuras de datos

### `Vec<T> (Vectores)`

**¿Qué es?**
Listas dinámicas que pueden crecer, similares a las listas de Python o slices en Go.

**¿Para qué se usa?**
Para almacenar colecciones de elementos del mismo tipo.

**Ejemplo:**
```rust
fn main() {
    let mut numeros = vec![1, 2, 3];
    numeros.push(4);
    println!("{:?}", numeros);
}
```

**Errores comunes de principiante:**
- Intentar acceder a un índice fuera de rango con corchetes `numeros[10]`, lo cual causará un panic en vez de un error controlado.

**Términos relacionados:** [`arrays`](#tuplas-y-arrays)

### `Tuplas y Arrays`

**¿Qué es?**
Tuplas agrupan diferentes tipos con un tamaño fijo. Arrays agrupan el mismo tipo con un tamaño fijo.

**¿Para qué se usa?**
Para datos inmutables y conocidos en tiempo de compilación.

**Ejemplo:**
```rust
fn main() {
    let tupla: (i32, f64, char) = (500, 6.4, 'a');
    let arreglo = [1, 2, 3, 4, 5];
    println!("{:?} {:?}", tupla, arreglo);
}
```

**Errores comunes de principiante:**
- Intentar añadir elementos a un array (su tamaño es inmutable).

**Términos relacionados:** [`Vec<T>`](#vect-vectorest-vectores)



### `enum`

**¿Qué es?**
Un tipo de dato que puede ser una de varias variantes posibles. En Rust son extremadamente poderosos porque pueden contener datos en su interior.

**¿Para qué se usa?**
Para modelar estados mutuamente exclusivos. Por ejemplo, una conexión web que está `Conectada`, `Desconectada`, o `Error(String)`.

**Ejemplo:**
```rust
enum Direccion {
    Arriba,
    Abajo(i32), // Variantes con datos
}

fn main() {
    let mov = Direccion::Abajo(10);
}
```

**Errores comunes de principiante:**
- Confundirlos con los enums simples de C. Los enums de Rust son tipos algebraicos completos.

**Términos relacionados:** [`match`](../rust/02-control-de-flujo.md#match)

### `HashMap`

**¿Qué es?**
Un diccionario o tabla hash (colección clave-valor). En Rust es parte de la librería estándar `std::collections`.

**¿Para qué se usa?**
Para asociar claves únicas a valores, como asociar nombres de usuarios a sus edades.

**Ejemplo:**
```rust
use std::collections::HashMap;

fn main() {
    let mut edades = HashMap::new();
    edades.insert("Ana", 30);
}
```

**Errores comunes de principiante:**
- Olvidar importar `use std::collections::HashMap;` ya que no viene incluido por defecto en el preludio.

**Términos relacionados:** [`Vec`](#vect-vectores)
