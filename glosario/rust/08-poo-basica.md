# 🦀 08 - POO básica (Structs y Ownership)

### `struct` e `impl`

**¿Qué es?**
`struct` es la forma de definir estructuras de datos personalizadas agrupando múltiples variables (atributos). `impl` (implementación) se usa para definir los métodos y el comportamiento asociados a ese struct.

**¿Para qué se usa?**
En Rust no existen las "Clases". `struct` e `impl` son el mecanismo para agrupar datos y comportamiento, promoviendo la composición por encima de las jerarquías de herencia profundas.

**Ejemplo:**
```rust
struct Persona {
    nombre: String,
    edad: u8,
}

impl Persona {
    // Método asociado (como estático, sin self)
    fn nueva(nombre: String) -> Persona {
        Persona { nombre, edad: 0 }
    }

    // Método de instancia (toma referencia a self)
    fn saludar(&self) {
        println!("Hola, soy {}", self.nombre);
    }
}

fn main() {
    let p = Persona::nueva(String::from("Ana"));
    p.saludar();
}
```

**Errores comunes de principiante:**
- Olvidar separar la definición de los datos (`struct`) de la de las funciones (`impl`), intentando meter funciones dentro de las llaves del `struct` como se haría en lenguajes como Java o C#.

**Términos relacionados:** [`Traits`](#traits-rasgos)

### `Ownership (Propiedad)`

**¿Qué es?**
El conjunto único de reglas que rige cómo Rust maneja la memoria. La regla de oro es: "Cada valor tiene un único dueño (owner) en todo momento, y cuando ese dueño sale del ámbito, el valor se descarta de la memoria".

**¿Para qué se usa?**
Para garantizar seguridad total de memoria en tiempo de compilación sin la penalización de rendimiento que tiene un Recolector de Basura (Garbage Collector).

**Ejemplo:**
```rust
fn main() {
    let s1 = String::from("hola");
    let s2 = s1; // La propiedad se MUEVE de s1 a s2
    
    // println!("{}", s1); // ¡Error de compilación! s1 ya no es válido
    println!("{}", s2);   // OK, s2 es el nuevo dueño
}
```

**Errores comunes de principiante:**
- Pelear contra el *Borrow Checker* intentando usar una variable después de haberla pasado como argumento a una función (lo cual por defecto "mueve" la propiedad).

**Términos relacionados:** [`Borrowing`](#borrowing-préstamo--referencias)

### `Borrowing (Préstamo / Referencias)`

**¿Qué es?**
El mecanismo que permite acceder a un dato sin tomar posesión (*ownership*) del mismo. Se hace creando referencias utilizando el símbolo `&` (referencia inmutable) o `&mut` (referencia mutable).

**¿Para qué se usa?**
Para permitir que múltiples partes del programa lean un valor simultáneamente, o que una parte lo modifique, sin transferir la propiedad.

**Ejemplo:**
```rust
fn calcular_longitud(s: &String) -> usize { // Recibe un préstamo
    s.len()
} // s no se destruye aquí porque no somos los dueños

fn main() {
    let texto = String::from("Rust");
    let len = calcular_longitud(&texto); // Presta con &
    println!("'{}' tiene longitud {}", texto, len); // texto sigue válido
}
```

**Errores comunes de principiante:**
- Violar las reglas del préstamo: Rust permite tener **múltiples referencias inmutables**, o **exactamente una referencia mutable**, pero nunca ambas al mismo tiempo. Romper esta regla causa error de compilación.

**Términos relacionados:** [`Ownership`](#ownership-propiedad)

### `Traits (Rasgos)`

**¿Qué es?**
Un conjunto de firmas de métodos que definen un comportamiento común (muy similar a las Interfaces en otros lenguajes). 

**¿Para qué se usa?**
Para implementar polimorfismo. Puedes requerir que una función acepte "cualquier tipo que implemente el trait X" sin importarte si es un Perro, Gato o Vehículo, siempre y cuando todos "hagan el sonido X".

**Ejemplo:**
```rust
trait Hablador {
    fn hablar(&self);
}

struct Gato;
impl Hablador for Gato {
    fn hablar(&self) { println!("Miau!"); }
}

// Acepta cualquier cosa que implemente Hablador
fn hacer_hablar(sujeto: &impl Hablador) {
    sujeto.hablar();
}

fn main() {
    let michi = Gato;
    hacer_hablar(&michi);
}
```

**Errores comunes de principiante:**
- Intentar usar métodos de un Trait sin haberlo importado (traído al ámbito o *scope*) primero. En Rust, un Trait debe estar en uso (scope) explícitamente para que sus métodos estén disponibles.

**Términos relacionados:** [`struct e impl`](#struct-e-impl)
