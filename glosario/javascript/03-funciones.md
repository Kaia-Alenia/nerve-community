# 🟨 03 - Funciones

### `function` (Funciones Declarativas)

**¿Qué es?**
Es la forma tradicional de declarar un bloque de código reutilizable en JavaScript utilizando la palabra clave `function`. A diferencia de otras formas de crear funciones, estas son "alzadas" (hoisted) al inicio de su contexto de ejecución, lo que significa que pueden ser llamadas en líneas de código antes de donde fueron escritas.

**¿Para qué se usa?**
Para encapsular lógica que se repetirá en varias partes de la aplicación. Son ideales para métodos principales de un módulo o cuando necesitas explícitamente el uso de la palabra clave `this` (por ejemplo, en programación orientada a objetos basada en prototipos) o el objeto `arguments`.

**Ejemplo:**
```javascript
// La función puede ser llamada ANTES de ser declarada (Hoisting)
console.log(saludar("Mundo")); 

function saludar(nombre) {
    return `Hola, ${nombre}!`;
}

// También existen como Expresiones de Función (no tienen hoisting)
const despedir = function() {
    return "Adiós!";
};
```

**Errores comunes de principiante:**
- Olvidar usar la palabra clave `return`. A diferencia de lenguajes funcionales o de las Arrow Functions cortas, si no usas `return` explícitamente, la función devuelve `undefined`.
- Esperar que las Expresiones de Función (las asignadas a constantes con `const func = function()...`) tengan hoisting igual que las Funciones Declarativas.

**Términos relacionados:** [Arrow Functions](#arrow-functions-), [Parámetros y Rest Operator](#parámetros-por-defecto-y-rest-operator-args)

---

### Arrow Functions (`=>`)

**¿Qué es?**
Introducidas en ES6, las "funciones flecha" son una sintaxis más compacta para escribir funciones. Su característica más importante a nivel técnico (más allá de ser más cortas) es que **no tienen su propio contexto para `this`**, sino que lo heredan del ámbito (scope) superior en el que fueron creadas (lexical this).

**¿Para qué se usa?**
Son el estándar moderno para funciones cortas, anónimas y, especialmente, como callbacks (funciones pasadas como argumentos a otras funciones, como en `.map()` o `.filter()`). Su manejo predecible de `this` las hace indispensables en frameworks de UI como React.

**Ejemplo:**
```javascript
// Retorno implícito (no necesita llaves ni la palabra return)
const multiplicar = (a, b) => a * b;

// Con lógica extra (necesita llaves y return explícito)
const dividir = (a, b) => {
    if (b === 0) return 0;
    return a / b;
};

console.log(multiplicar(5, 2)); // 10
```

**Errores comunes de principiante:**
- Poner llaves `{}` en una Arrow Function de una sola línea y olvidar añadir `return`, lo cual hace que devuelva `undefined`. Si abres llaves, el retorno automático se desactiva.
- Intentar usar Arrow Functions como constructores (con `new`) o usarlas en métodos de objetos esperando que `this` apunte al objeto en sí (apuntará al scope global o window).

**Términos relacionados:** [`function`](#function-funciones-declarativas), [Callbacks](#callbacks-y-funciones-de-orden-superior)

---

### Parámetros por defecto y Rest Operator (`...args`)

**¿Qué es?**
Son características modernas (ES6) para el manejo de argumentos en funciones. 
- **Parámetros por defecto:** Permiten asignar un valor a un parámetro en caso de que no se pase ninguno en la llamada.
- **Rest Operator (`...`):** Permite agrupar un número indefinido de argumentos adicionales en un verdadero Array de JavaScript.

**¿Para qué se usa?**
- Los parámetros por defecto evitan que variables internas terminen siendo `undefined` si el usuario olvida un dato.
- El operador Rest reemplaza al antiguo y problemático objeto `arguments`, dándote un Array real sobre el que puedes usar métodos como `.map()` o `.reduce()`.

**Ejemplo:**
```javascript
// 'moneda' es un parámetro por defecto
function formatearPrecio(precio, moneda = "USD") {
    return `${precio} ${moneda}`;
}

// '...precios' agrupa todos los argumentos extra en un array
function sumarPrecios(descuento, ...precios) {
    // precios es un array real
    const total = precios.reduce((acc, val) => acc + val, 0);
    return total - descuento;
}

console.log(formatearPrecio(100)); // "100 USD"
console.log(sumarPrecios(10, 50, 50, 20)); // 110
```

**Errores comunes de principiante:**
- Poner el parámetro Rest al principio o en medio de la lista de parámetros (`function(...args, ultimo)`). El parámetro Rest **siempre** debe ser el último argumento de la función.
- Confundir el operador Rest (que junta argumentos en un array en la firma de la función) con el operador Spread (que esparce un array en elementos individuales). Tienen la misma sintaxis (`...`) pero hacen lo opuesto según dónde se usen.

**Términos relacionados:** [Arrow Functions](#arrow-functions-), [Métodos de Array](./04-estructuras-de-datos.md#métodos-de-array-map-filter-reduce)

---

### Callbacks y Funciones de Orden Superior

**¿Qué es?**
- Un **Callback** es simplemente una función que se pasa como argumento a otra función para que sea ejecutada ("llamada de vuelta") en algún momento posterior.
- Una **Función de Orden Superior** (High Order Function o HOF) es una función que recibe a otras funciones como parámetros, o que retorna una función como resultado.

**¿Para qué se usa?**
Es la base de la programación funcional y de la asincronía clásica en JavaScript. Se usa intensivamente para reaccionar a eventos de usuario (clicks), peticiones a servidores, o para procesar arreglos (como en `map` y `filter`).

**Ejemplo:**
```javascript
// HOF: Función que acepta otra función como argumento (el callback)
function procesarPago(monto, callbackNotificacion) {
    console.log(`Procesando $${monto}...`);
    // Simulamos que el proceso terminó, llamamos al callback
    callbackNotificacion("Pago exitoso");
}

// El callback en sí (una función simple)
function mostrarAlerta(mensaje) {
    console.log(`[ALERTA SISTEMA]: ${mensaje}`);
}

// Pasamos la función 'mostrarAlerta' SIN los paréntesis
procesarPago(50, mostrarAlerta);

// Usando una Arrow Function anónima directamente como callback
procesarPago(20, (msj) => console.log(`Email enviado: ${msj}`));
```

**Errores comunes de principiante:**
- Pasar el callback a la función ejecutándolo accidentalmente: `procesarPago(50, mostrarAlerta())`. Esto ejecuta `mostrarAlerta` inmediatamente y pasa su resultado (`undefined`) en lugar de pasar la función en sí.
- Anidar demasiados callbacks asíncronos uno dentro de otro, creando el temido "Callback Hell".

**Términos relacionados:** [Arrow Functions](#arrow-functions-), [Promesas](./09-asincronia.md#promesas-promises)
