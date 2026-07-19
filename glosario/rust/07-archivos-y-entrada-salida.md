# 🦀 07 - Archivos y entrada/salida

### `std::fs::File`

**¿Qué es?**
El struct fundamental proporcionado por la librería estándar para representar un archivo abierto en el sistema operativo.

**¿Para qué se usa?**
Para adquirir un identificador (file descriptor) que permita realizar operaciones de bajo nivel (lectura o escritura) sobre un archivo del disco. Asegura que el archivo se cierre automáticamente cuando la variable sale de su ámbito gracias a la filosofía RAII.

**Ejemplo:**
```rust
use std::fs::File;

fn main() -> std::io::Result<()> {
    // Crear archivo de prueba
    File::create("config.txt")?;
    
    // Abre un archivo en modo solo lectura
    let archivo = File::open("config.txt")?;
    
    // Crea (o trunca) un archivo para escritura
    let nuevo = File::create("salida.log")?;
    
    Ok(())
}
```

**Errores comunes de principiante:**
- Olvidar manejar los permisos correctamente (ej. usar `File::open` cuando se tiene la intención de escribir), lo cual generará errores en tiempo de ejecución.

**Términos relacionados:** [`std::io::Read / Write`](#stdioread--write)

### `std::io::Read / Write`

**¿Qué es?**
Son *traits* (rasgos o interfaces) de la librería estándar que definen los métodos necesarios para leer y escribir bytes.

**¿Para qué se usa?**
Permiten usar funciones estándar como `read_to_string` o `write_all` en cualquier tipo que los implemente (archivos, conexiones TCP, memoria en buffer), haciendo el código altamente polimórfico.

**Ejemplo:**
```rust
use std::fs::File;
use std::io::{Read, Write};

fn main() -> std::io::Result<()> {
    let mut file = File::create("datos.txt")?;
    // write_all pertenece al trait Write
    file.write_all(b"Hola Mundo")?; 

    let mut archivo = File::open("datos.txt")?;
    let mut contenido = String::new();
    // read_to_string pertenece al trait Read
    archivo.read_to_string(&mut contenido)?; 
    
    Ok(())
}
```

**Errores comunes de principiante:**
- Olvidar importar los traits (`use std::io::{Read, Write};`). En Rust, incluso si un struct como `File` implementa los métodos, no puedes usarlos si no has traído el *trait* al contexto.

**Términos relacionados:** [`std::fs::File`](#stdfsfile)

### `std::fs` (Operaciones del SO)

**¿Qué es?**
El módulo de más alto nivel que agrupa funciones convenientes para realizar operaciones comunes del sistema de archivos sin tener que instanciar manualmente estructuras como `File`.

**¿Para qué se usa?**
Para simplificar tareas que requieren una sola operación como leer un archivo entero a un string, borrar archivos, crear directorios o consultar metadata.

**Ejemplo:**
```rust
use std::fs;

fn main() -> std::io::Result<()> {
    // Crear archivo de prueba
    fs::write("config.txt", "port=8080")?;
    
    // Lee todo el archivo en una sola línea de código
    let datos = fs::read_to_string("config.txt")?;
    println!("Configuración: {}", datos);
    
    // Crea un directorio
    fs::create_dir_all("logs/2023")?;
    
    Ok(())
}
```

**Errores comunes de principiante:**
- Usar `fs::read_to_string` indiscriminadamente con archivos de varios Gigabytes, lo que agotará la memoria RAM porque carga la totalidad del archivo de una sola vez.

**Términos relacionados:** [`std::fs::File`](#stdfsfile)

### `BufReader / BufWriter`

**¿Qué es?**
Estructuras (wrappers) que envuelven lectores (`Read`) o escritores (`Write`) y les añaden un búfer en memoria RAM.

**¿Para qué se usa?**
Para mejorar drásticamente el rendimiento de lectura y escritura. En lugar de hacer una costosa llamada al sistema operativo por cada byte, acumulan operaciones en memoria y las ejecutan en bloques grandes.

**Ejemplo:**
```rust
use std::fs::{self, File};
use std::io::{BufReader, BufRead};

fn main() -> std::io::Result<()> {
    // Crear archivo de prueba
    fs::write("lineas.txt", "A\nB\nC")?;
    
    let archivo = File::open("lineas.txt")?;
    let lector = BufReader::new(archivo);
    
    // Iterar línea por línea eficientemente
    for linea in lector.lines() {
        println!("{}", linea?);
    }
    
    Ok(())
}
```

**Errores comunes de principiante:**
- En el caso de `BufWriter`, olvidar que los datos escritos pueden no llegar al disco de inmediato si el búfer no se ha llenado (se vacía automáticamente al destruirse o al llamar a `.flush()`).

**Términos relacionados:** [`std::io::Read / Write`](#stdioread--write)
