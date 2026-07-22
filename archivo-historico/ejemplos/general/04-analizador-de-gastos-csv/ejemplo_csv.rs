/*
Ejemplo: Leer un CSV real desde disco, filtrar y calcular sumas

Qué enseña este ejemplo:
  - Cómo usar la biblioteca estándar para leer archivos estructurados.
  - Cómo convertir strings a números con .parse()
  - Cómo agrupar usando un HashMap

Para tu reto (analizador de gastos):
  Aplica el mismo patrón para leer tu CSV de gastos
  (fecha, categoría, monto) y calcular totales por categoría.

Glosario:
  File::open(ruta)     — Abre un archivo en modo lectura.
  .parse::<f64>()      — Intenta convertir un string a un número decimal (float de 64 bits).
  HashMap::new()       — Crea una estructura de diccionario para guardar totales por clave.
  .entry(clave)        — Busca una clave en el map para modificarla o insertarla si no existe.
*/

use std::collections::HashMap;
use std::fs::File;
use std::io::Write;
use std::path::Path;

struct Empleado {
    _nombre: String,
    departamento: String,
    salario: f64,
}

struct Estadisticas {
    suma: f64,
    cantidad: i32,
}

fn leer_empleados(ruta_csv: &str) -> Vec<Empleado> {
    let mut empleados = Vec::new();

    let file = match File::open(ruta_csv) {
        Ok(f) => f,
        Err(_) => {
            println!("Archivo no encontrado: {}", ruta_csv);
            return empleados;
        }
    };

    use std::io::{BufRead, BufReader};
    let reader = BufReader::new(file);

    for (index, line) in reader.lines().enumerate() {
        if index == 0 {
            continue; // Saltar cabecera
        }
        if let Ok(l) = line {
            let cols: Vec<&str> = l.split(',').collect();
            if cols.len() >= 3 {
                let nombre = cols[0].trim().to_string();
                let departamento = cols[1].trim().to_string();
                let salario = cols[2].trim().parse::<f64>().unwrap_or(0.0);

                empleados.push(Empleado {
                    _nombre: nombre,
                    departamento,
                    salario,
                });
            }
        }
    }

    empleados
}

fn reporte_por_departamento(empleados: &[Empleado]) {
    let mut totales: HashMap<String, Estadisticas> = HashMap::new();

    for emp in empleados {
        let entry = totales
            .entry(emp.departamento.clone())
            .or_insert(Estadisticas { suma: 0.0, cantidad: 0 });
        entry.suma += emp.salario;
        entry.cantidad += 1;
    }

    println!("\n--- Reporte por departamento ---");
    for (dept, stats) in totales.iter() {
        let promedio = stats.suma / stats.cantidad as f64;
        println!(
            "  {}: total=${} | promedio=${} | empleados={}",
            dept, stats.suma, promedio, stats.cantidad
        );
    }
}

fn main() {
    let archivo = "empleados.csv";

    if !Path::new(archivo).exists() {
        let mut file = File::create(archivo).expect("No se pudo crear el archivo");
        let datos = "\
nombre,departamento,salario
Ana García,Ingeniería,35000
Luis Martínez,Marketing,28000
Carmen López,Ingeniería,42000
Pedro Sánchez,Marketing,31000
Sofía Ramírez,Ingeniería,39000
";
        file.write_all(datos.as_bytes()).unwrap();
        println!("Archivo '{}' creado de ejemplo.", archivo);
    }

    let empleados = leer_empleados(archivo);
    println!("\nSe leyeron {} empleados.", empleados.len());
    reporte_por_departamento(&empleados);
}
