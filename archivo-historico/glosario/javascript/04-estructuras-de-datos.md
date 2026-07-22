# 04 - Estructuras de datos

### Arrays (Arreglos)

**¿Qué es?**
Son listas ordenadas de datos. A diferencia de lenguajes de bajo nivel, los Arrays en JavaScript son objetos dinámicos: pueden crecer o encogerse automáticamente y pueden contener una mezcla de diferentes tipos de datos (números, strings, objetos o incluso otros arrays) en la misma colección.

**¿Para qué se usa?**
Para agrupar y manejar colecciones de elementos que tienen un orden específico o secuencial, como una lista de tareas, los resultados de una base de datos o los elementos de un menú.

**Ejemplo:**
```javascript
// Declaración y mezcla de tipos
const mochila = ["mapa", "brújula", 100, { tipo: "pocion" }];

// Agregar elementos al final
mochila.push("linterna");

// Eliminar el último elemento
const itemRemovido = mochila.pop();

console.log(`La mochila tiene ${mochila.length} objetos.`);
console.log(`El primer objeto es: ${mochila[0]}`);
```

**Errores comunes de principiante:**
- Intentar acceder al último elemento usando un índice negativo (ej. `mochila[-1]`) asumiendo que funcionará como en Python. En JavaScript esto devuelve `undefined`; debes usar `mochila[mochila.length - 1]` o el moderno método `mochila.at(-1)`.
- Reasignar el array completo (usando `const`) en lugar de mutarlo con métodos como `.push()`.

**Términos relacionados:** [Métodos de Array](#métodos-de-array-map-filter-reduce), [Desestructuración](#desestructuración-destructuring)

---

### Métodos de Array (`map`, `filter`, `reduce`)

**¿Qué es?**
Son Funciones de Orden Superior integradas en el prototipo del objeto Array. Permiten recorrer y transformar listas de manera declarativa y funcional, en lugar de usar bucles `for` imperativos.
- `map()`: Crea un array nuevo transformando cada elemento.
- `filter()`: Crea un array nuevo solo con los elementos que pasen una condición.
- `reduce()`: Acumula todos los elementos en un único valor (ej. una suma).

**¿Para qué se usa?**
Son el estándar moderno para manipular datos masivos en el frontend (ej. procesar respuestas de APIs o renderizar listas de componentes en React). Favorecen la inmutabilidad y hacen el código mucho más expresivo.

**Ejemplo:**
```javascript
const productos = [
    { nombre: "Mouse", precio: 20 },
    { nombre: "Teclado", precio: 50 },
    { nombre: "Monitor", precio: 200 }
];

// Obtener solo los nombres (map)
const nombres = productos.map(p => p.nombre);
console.log("Nombres:", nombres);

// Filtrar productos caros (filter)
const caros = productos.filter(p => p.precio >= 100);
console.log("Caros:", caros);

// Sumar el total de los precios (reduce)
const total = productos.reduce((acumulador, p) => acumulador + p.precio, 0);
console.log("Precio Total:", total);
```

**Errores comunes de principiante:**
- Creer que estos métodos modifican (mutan) el array original. Siempre devuelven un **array nuevo**, por lo que debes guardar su resultado en una variable.
- Olvidar usar la palabra `return` dentro de la función callback (cuando usas llaves `{}` en vez del retorno implícito), lo cual hace que `.map()` devuelva un array de `undefined`.

**Términos relacionados:** [Arrays](#arrays-arreglos), [Arrow Functions](./03-funciones.md#arrow-functions-)

---

### Objetos Literales

**¿Qué es?**
Son colecciones no ordenadas de pares "clave-valor" (similares a los diccionarios en Python). En JavaScript, casi todo (excepto los tipos primitivos) es un objeto bajo el capó. Las claves siempre se convierten a strings o symbols, mientras que los valores pueden ser de cualquier tipo (incluyendo funciones, que entonces se denominan "métodos").

**¿Para qué se usa?**
Para representar entidades estructuradas y agrupar propiedades relacionadas bajo un mismo nombre. Son el formato de transporte de datos más ubicuo en la web.

**Ejemplo:**
```javascript
const jugador = {
    nombre: "Hero",
    nivel: 5,
    equipamiento: ["espada", "escudo"],
    // Un método del objeto
    saludar() {
        console.log(`Soy ${this.nombre}, nivel ${this.nivel}`);
    }
};

// Acceso por punto (dot notation)
jugador.nivel += 1;

// Acceso por corchetes (bracket notation, útil para claves dinámicas)
const propiedad = "nombre";
console.log(jugador[propiedad]); // "Hero"

jugador.saludar();
```

**Errores comunes de principiante:**
- Olvidar las comas `,` para separar las propiedades al definir el objeto, lo cual causa errores de sintaxis.
- Perder el contexto de `this` al extraer un método de un objeto y asignarlo a una variable suelta, o al usar una Arrow Function para declarar un método del objeto (las arrow functions no tienen `this` propio).

**Términos relacionados:** [Desestructuración](#desestructuración-destructuring), [JSON](./07-archivos-y-entrada-salida.md#json-javascript-object-notation)

---

### Desestructuración (Destructuring)

**¿Qué es?**
Es una sintaxis especial y elegante introducida en ES6 que permite "desempacar" o extraer valores de arrays o propiedades de objetos y asignarlos directamente a variables individuales en una sola línea de código.

**¿Para qué se usa?**
Para extraer datos anidados de forma rápida y concisa, reduciendo el código repetitivo (`objeto.propiedad`). Es vital en Node.js (para extraer módulos específicos) y en React (para extraer propiedades de estado y "props").

**Ejemplo:**
```javascript
const usuario = { id: 42, alias: "DevNinja", rango: "Senior" };

// Desestructuración de Objeto
// (El nombre de la variable debe coincidir con la clave)
const { alias, rango } = usuario;
console.log(`${alias} es ${rango}`);

const coordenadas = [10, 25, 80];

// Desestructuración de Array
// (El orden importa, no los nombres)
const [x, y, z] = coordenadas;
console.log(`X: ${x}, Y: ${y}`);

// Desestructurando parámetros en una función
function saludar({ alias }) {
    console.log(`Hola, ${alias}`);
}
saludar(usuario);
```

**Errores comunes de principiante:**
- Intentar desestructurar propiedades que no existen en el objeto, lo cual no lanza error sino que asigna `undefined` silenciosamente a la variable.
- Confundir la sintaxis de array con la de objeto: intentar hacer `const { x, y } = [10, 20]` no funcionará, ya que los arrays se desestructuran con corchetes `[]`.

**Términos relacionados:** [Objetos Literales](#objetos-literales), [Arrays](#arrays-arreglos)
