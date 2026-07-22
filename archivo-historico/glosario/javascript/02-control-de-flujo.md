# 02 - Control de flujo

### `if` / `else` / `switch`

**¿Qué es?**
Son las estructuras condicionales fundamentales de JavaScript. `if` y `else` evalúan si una expresión es verdadera (truthy) o falsa (falsy) para bifurcar la ejecución del código. `switch` es una alternativa más limpia cuando se necesita comparar una misma variable contra múltiples valores específicos.

**¿Para qué se usa?**
Para tomar decisiones lógicas. A diferencia de lenguajes como Python, en JavaScript las condiciones SIEMPRE deben ir entre paréntesis `()` y los bloques de código entre llaves `{}`.

**Ejemplo:**
```javascript
const edad = 18;
const rol = "admin";

// if / else tradicional
if (edad >= 18) {
    console.log("Acceso permitido");
} else if (edad >= 13) {
    console.log("Acceso con supervisión");
} else {
    console.log("Acceso denegado");
}

// switch para múltiples opciones específicas
switch (rol) {
    case "admin":
        console.log("Panel de control completo");
        break; // Crucial: si olvidas el break, se ejecuta el siguiente caso
    case "user":
        console.log("Panel de usuario");
        break;
    default:
        console.log("Rol no reconocido");
}
```

**Errores comunes de principiante:**
- Olvidar el `break` al final de cada caso en un bloque `switch`, lo cual causa un "fall-through" (caída libre) ejecutando el código de los casos posteriores de forma involuntaria.
- Asignar una variable dentro de un if accidentalmente: `if (esAdmin = true)` en lugar de evaluar `if (esAdmin === true)`.

**Términos relacionados:** [`===` vs `==`](#-vs--igualdad-estricta-vs-débil)

---

### `===` vs `==` (Igualdad estricta vs débil)

**¿Qué es?**
Son operadores para comparar valores.
- `===` (Estricto): Compara tanto el **valor** como el **tipo de dato**. No intenta convertir nada.
- `==` (Débil): Compara el valor pero, si los tipos de dato son diferentes, **fuerza una conversión automática** (type coercion) antes de compararlos.

**¿Para qué se usa?**
Para evaluar igualdad en condiciones. En la web moderna, la regla absoluta de la industria es **usar siempre `===`** para evitar bugs sutiles e impredecibles derivados de las extrañas reglas de conversión de tipos de JavaScript.

**Ejemplo:**
```javascript
const numero = 1;
const texto = "1";

// Igualdad estricta (Recomendado)
console.log(numero === texto); // false (Number no es String)

// Igualdad débil (¡Peligroso!)
console.log(numero == texto); // true (JS convierte el texto a número y luego compara)

// Las extrañas reglas de la igualdad débil:
console.log(0 == false);      // true
console.log("" == false);     // true
console.log([] == false);     // true
console.log(null == undefined); // true
```

**Errores comunes de principiante:**
- Usar `==` por costumbre viniendo de otros lenguajes (como C o Python donde `==` es seguro) y terminar con bugs donde arreglos vacíos o cadenas vacías dan falsos positivos al compararlos.
- Usar `!=` (desigualdad débil) en lugar del seguro `!==` (desigualdad estricta).

**Términos relacionados:** [Tipos Primitivos](./01-fundamentos.md#tipos-primitivos-string-number-boolean-null-undefined), [`if` / `else`](#if--else--switch)

---

### Bucles clásicos (`for` / `while`)

**¿Qué es?**
Las estructuras de repetición procedimentales estándar presentes en casi todos los lenguajes tipo C. 
- `for`: Tiene una inicialización, una condición de parada y un incremento.
- `while`: Repite un bloque mientras una condición sea verdadera.

**¿Para qué se usa?**
Para ejecutar un bloque de código múltiples veces. Se usan cada vez menos en JavaScript moderno (gracias a los métodos de arreglos y `for...of`), pero son útiles cuando se necesita control absoluto sobre el contador (por ejemplo, saltar índices de dos en dos) o si se desconoce de antemano el número exacto de iteraciones (`while`).

**Ejemplo:**
```javascript
// Bucle for tradicional
const limite = 3;
for (let i = 0; i < limite; i++) {
    console.log(`Iteración for: ${i}`);
}

// Bucle while
let vidas = 2;
while (vidas > 0) {
    console.log(`Jugando... vidas restantes: ${vidas}`);
    vidas--; // Decremento crucial
}
console.log("Game Over");
```

**Errores comunes de principiante:**
- Declarar el contador del `for` con `const` en lugar de `let` (`for (const i = 0...)`), lo cual causa un error al intentar incrementar `i++`.
- Olvidar actualizar la condición dentro de un `while`, resultando en un bucle infinito que colgará la pestaña del navegador.

**Términos relacionados:** [Iteradores modernos](#iteradores-modernos-forof--forin), [Métodos de Array](./04-estructuras-de-datos.md#métodos-de-array-map-filter-reduce)

---

### Iteradores modernos (`for...of` / `for...in`)

**¿Qué es?**
Son sintaxis especializadas más legibles para recorrer colecciones.
- `for...of`: Recorre los **valores** de estructuras iterables (Arrays, Strings, Sets, Maps).
- `for...in`: Recorre las **claves** (keys o índices) enumerables de un Objeto literal.

**¿Para qué se usa?**
Para iterar de forma declarativa y segura sin tener que lidiar manualmente con contadores (`i++`) o longitudes de arreglos (`.length`). 

**Ejemplo:**
```javascript
// 1. for...of (Perfecto para Arrays o Strings)
const colores = ["rojo", "verde", "azul"];
console.log("Valores (for...of):");
for (const color of colores) {
    console.log(color);
}

// 2. for...in (Perfecto para Objetos literales)
const usuario = {
    nombre: "Ana",
    rol: "Admin",
    edad: 28
};
console.log("\nClaves (for...in):");
for (const clave in usuario) {
    // Usamos corchetes para acceder al valor usando la clave variable
    console.log(`${clave}: ${usuario[clave]}`);
}
```

**Errores comunes de principiante:**
- Intercambiarlos: intentar usar `for...of` en un objeto literal (`{}`) causará un error porque los objetos no son iterables por defecto.
- Usar `for...in` para recorrer un Array. Aunque "funciona", iterará sobre los índices como *strings* (`"0"`, `"1"`) en lugar de los valores, y puede incluir accidentalmente propiedades heredadas del prototipo del Array, causando bugs muy difíciles de rastrear.

**Términos relacionados:** [Objetos](./04-estructuras-de-datos.md#objetos-literales), [Bucles clásicos](#bucles-clásicos-for--while)
