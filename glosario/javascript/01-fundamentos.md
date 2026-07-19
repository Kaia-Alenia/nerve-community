# 🟨 01 - Fundamentos

### `let` y `const`

**¿Qué es?**
En JavaScript moderno (ES6+), `let` y `const` son las palabras reservadas estándar para declarar variables, reemplazando al antiguo `var`. `let` permite declarar variables cuyo valor o referencia puede cambiar (mutables), mientras que `const` crea una referencia de solo lectura que no puede ser reasignada (inmutable).

**¿Para qué se usa?**
Se utilizan para almacenar y manipular datos en memoria. La regla de oro en JavaScript es usar siempre `const` por defecto para evitar mutaciones accidentales, y cambiar a `let` únicamente cuando sepas de antemano que el valor de la variable necesitará ser actualizado (por ejemplo, en contadores de bucles o acumuladores).

**Ejemplo:**
```javascript
// const: la referencia no puede cambiar
const nombreUsuario = "Alex";
// nombreUsuario = "Ana"; // Esto lanzaría TypeError

// let: el valor puede cambiar
let intentosLogin = 0;
intentosLogin += 1;

// Nota: con const, los objetos y arrays SÍ pueden mutar internamente
const configuracion = { tema: "oscuro" };
configuracion.tema = "claro"; // Esto es válido

console.log(`Usuario: ${nombreUsuario}, Intentos: ${intentosLogin}, Tema: ${configuracion.tema}`);
```

**Errores comunes de principiante:**
- Seguir usando `var`, lo cual causa problemas de "hoisting" (la variable existe antes de declararse) y contamina el alcance (scope) global o de función.
- Creer que `const` hace que un objeto o arreglo sea completamente inmutable; `const` solo bloquea la reasignación de la variable, no la modificación de sus propiedades internas (para eso se usa `Object.freeze()`).

**Términos relacionados:** [Tipos Primitivos](#tipos-primitivos-string-number-boolean-null-undefined), [Objetos](./04-estructuras-de-datos.md#objetos-literales)

---

### Tipos Primitivos (`string`, `number`, `boolean`, `null`, `undefined`)

**¿Qué es?**
Son los bloques de construcción de datos más básicos en JavaScript. A diferencia de lenguajes tipados donde hay enteros, flotantes, etc., JS simplifica esto: `number` abarca tanto enteros como decimales. `string` es texto, y `boolean` es `true` o `false`. Adicionalmente, JS tiene dos tipos para representar "nada": `undefined` (una variable existe pero no tiene valor asignado) y `null` (una ausencia de valor explícita e intencional).

**¿Para qué se usa?**
Para representar el estado básico de una aplicación. La distinción entre `null` y `undefined` es crucial: `undefined` suele ser el estado por defecto del motor de JS, mientras que `null` lo asigna el desarrollador para vaciar una variable deliberadamente.

**Ejemplo:**
```javascript
let edad; // undefined por defecto
const precio = 19.99; // number
const estaActivo = true; // boolean
const nombre = "Servidor"; // string
let usuarioActual = null; // null (ausencia explícita)

console.log(typeof edad); // "undefined"
console.log(typeof precio); // "number"
// Curiosidad histórica de JS: typeof null devuelve "object"
console.log(typeof usuarioActual); // "object"
```

**Errores comunes de principiante:**
- Confundir `undefined` con `null` al hacer validaciones; es mejor inicializar explícitamente variables vacías con `null`.
- El comportamiento peculiar de que `typeof null` devuelva `"object"`, lo cual es un bug histórico reconocido en JavaScript que no se corrigió por compatibilidad hacia atrás.

**Términos relacionados:** [`let` y `const`](#let-y-const), [`===` vs `==`](./02-control-de-flujo.md#-vs--igualdad-estricta-vs-débil)

---

### `console` (`log`, `error`, `table`)

**¿Qué es?**
`console` es un objeto global que provee acceso a la consola de depuración del entorno (ya sea el navegador web o Node.js). Aunque `console.log()` es el más famoso, el objeto tiene muchos otros métodos útiles como `.error()`, `.warn()`, `.table()` o `.time()`.

**¿Para qué se usa?**
Es la herramienta principal para "print debugging" (depuración por impresión). Se usa para inspeccionar el valor de variables, estructuras de datos, o el flujo de ejecución de un programa en tiempo real, antes de recurrir a depuradores más complejos.

**Ejemplo:**
```javascript
const usuarios = [
    { id: 1, nombre: "Ana", rol: "Admin" },
    { id: 2, nombre: "Luis", rol: "User" }
];

// Impresión normal
console.log("Iniciando sistema...");

// Impresión de errores (suele salir en rojo en navegadores)
console.error("Fallo de conexión a la base de datos simulado");

// Imprimir arrays de objetos como una tabla (muy útil)
console.table(usuarios);
```

**Errores comunes de principiante:**
- Dejar decenas de `console.log()` en el código de producción, lo cual ensucia la terminal del servidor o expone información interna en la consola del navegador del cliente.
- Usar `console.log(objeto)` en un bucle infinito, lo que puede causar fugas de memoria severas en el navegador porque mantiene referencias a los objetos impidiendo que el Garbage Collector los elimine.

**Términos relacionados:** [Tipos Primitivos](#tipos-primitivos-string-number-boolean-null-undefined), [JSON](./07-archivos-y-entrada-salida.md#json-javascript-object-notation)

---

### Template Strings

**¿Qué es?**
Son cadenas de texto literales (introducidas en ES6) delimitadas por comillas invertidas (backticks `` ` ``) en lugar de comillas simples o dobles. Permiten la interpolación de variables y expresiones matemáticas usando la sintaxis `${expresion}`, y soportan texto multilínea de forma nativa.

**¿Para qué se usa?**
Para construir cadenas de texto dinámicas de forma mucho más legible. Reemplazan a la antigua y propensa a errores concatenación de strings mediante el operador de suma (`+`). Son ideales para generar HTML dinámico, construir URLs o formatear mensajes.

**Ejemplo:**
```javascript
const producto = "Teclado Mecánico";
const precio = 120;
const impuesto = 0.21;

// Antes (Concatenación clásica)
// const mensajeViejo = "El producto " + producto + " cuesta $" + (precio + (precio * impuesto)) + ".";

// Ahora (Template String)
const mensajeNuevo = `El producto ${producto} cuesta $${precio + (precio * impuesto)}.`;

// Multilínea nativo
const html = `
  <div>
    <h2>${producto}</h2>
  </div>
`;

console.log(mensajeNuevo);
console.log(html);
```

**Errores comunes de principiante:**
- Intentar usar interpolación `${}` dentro de comillas simples `''` o dobles `""`, resultando en que se imprima el texto literal "${variable}" en lugar de su valor.
- Romper el sangrado o indentación en archivos de código, ya que los Template Strings respetan todos los espacios y saltos de línea literalmente tal y como están en el editor de código.

**Términos relacionados:** [`let` y `const`](#let-y-const), [Funciones](./03-funciones.md#function-funciones-declarativas)
