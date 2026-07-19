# 🦀 05 - Módulos y librerías

### `cargo` y `crates`

**¿Qué es?**
`cargo` es el gestor oficial de paquetes y sistema de compilación de Rust. Los `crates` (cajas) son el equivalente a los paquetes o librerías; pueden ser binarios (programas ejecutables) o librerías compartidas publicadas en `crates.io`.

**¿Para qué se usa?**
Para inicializar proyectos, gestionar dependencias, correr tests, y compilar el código de manera uniforme en cualquier sistema operativo sin lidiar con Makefiles complejos.

**Ejemplo:**
```bash
cargo new mi_proyecto # Crea un nuevo proyecto
cargo build           # Compila el código
cargo run             # Compila y ejecuta
cargo add rand        # Añade la dependencia 'rand'
```

**Errores comunes de principiante:**
- Descargar un proyecto de Rust y usar directamente `rustc main.rs` en lugar de `cargo run`, perdiendo toda la gestión automática de dependencias y optimizaciones.

**Términos relacionados:** [`Cargo.toml`](#cargotoml)

### `mod` y `use`

**¿Qué es?**
`mod` declara un nuevo módulo (un espacio de nombres) y le dice al compilador que busque un archivo o bloque con ese nombre. `use` sirve para importar elementos (funciones, structs) de un módulo para usarlos sin escribir toda su ruta.

**¿Para qué se usa?**
Para estructurar proyectos grandes dividiendo el código en múltiples archivos lógicos, evitando tener un único `main.rs` de 10,000 líneas.

**Ejemplo:**
```rust
// Define o declara un módulo
mod red {
    pub struct Conexion;
    impl Conexion {
        pub fn nueva() -> Self {
            Conexion
        }
    }
}

// Importa específicamente el struct 'Conexion'
use red::Conexion;

fn main() {
    let c = Conexion::nueva();
}
```

**Errores comunes de principiante:**
- Intentar usar `use archivo::funcion;` sin haber declarado primero `mod archivo;` en el punto de entrada (`main.rs` o `lib.rs`), lo que causa un error de resolución de rutas.

**Términos relacionados:** [`pub (Visibilidad)`](#pub-visibilidad)

### `pub` (Visibilidad)

**¿Qué es?**
La palabra clave que hace que un elemento (función, struct, módulo o campo de un struct) sea público. En Rust, TODO es privado por defecto.

**¿Para qué se usa?**
Para diseñar APIs limpias, ocultando los detalles de implementación interna y exponiendo solo las funciones que otros módulos (o usuarios de tu librería) necesitan usar.

**Ejemplo:**
```rust
mod matematicas {
    // Función privada (solo usable dentro de 'matematicas')
    fn validar(a: i32) -> bool { a > 0 }
    
    // Función pública
    pub fn sumar_positivos(a: i32, b: i32) -> i32 {
        if validar(a) && validar(b) { a + b } else { 0 }
    }
}

fn main() {
    // matematicas::validar(5); // Daría error de visibilidad
    matematicas::sumar_positivos(5, 5); // OK
}
```

**Errores comunes de principiante:**
- Olvidar poner `pub` a los campos internos de un struct público (ej. `pub struct Usuario { pub nombre: String }`), lo que impide instanciarlo desde otros módulos, incluso si el struct en sí es `pub`.

**Términos relacionados:** [`mod y use`](#mod-y-use)

### `Cargo.toml`

**¿Qué es?**
El archivo de manifiesto (escrito en formato TOML) que define la metadata de un proyecto Rust, sus dependencias, configuraciones de compilación y características (features).

**¿Para qué se usa?**
Es el equivalente a `package.json` en Node o `pom.xml` en Java. Le dice a `cargo` exactamente qué versiones de librerías descargar y cómo estructurar la compilación.

**Ejemplo:**
```toml
[package]
name = "servidor_web"
version = "0.1.0"
edition = "2021"

[dependencies]
# Dependencia estándar
serde = "1.0"
# Dependencia con features opcionales activadas
tokio = { version = "1.28", features = ["full"] }
```

**Errores comunes de principiante:**
- Modificar a mano el archivo `Cargo.lock` (que es generado automáticamente por Cargo para fijar las versiones exactas) en lugar de editar solo `Cargo.toml`.

**Términos relacionados:** [`cargo y crates`](#cargo-y-crates)
