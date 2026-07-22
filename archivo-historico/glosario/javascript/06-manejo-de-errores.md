# 06 - Manejo de errores

### `try / catch / finally`

**¿Qué es?**
La estructura fundamental para el control de excepciones en JavaScript. Permite ejecutar código que podría fallar (`try`), capturar y manejar el error de forma controlada (`catch`), y ejecutar instrucciones de limpieza sin importar el resultado (`finally`).

**¿Para qué se usa?**
Para evitar que un error no anticipado rompa el flujo de ejecución de la aplicación, permitiendo presentar mensajes amigables al usuario o registrar el fallo (log) para diagnóstico.

**Ejemplo:**
```javascript
try {
  const data = JSON.parse("invalid json"); // Esto lanzará un error
} catch (error) {
  console.error("Fallo al parsear datos:", error.message);
} finally {
  console.log("Limpieza de recursos: Ejecutado sí o sí.");
}
```

**Errores comunes de principiante:**
- Dejar el bloque `catch` completamente vacío, lo que silencia (swallows) el error y hace que diagnosticar problemas en producción sea casi imposible.

**Términos relacionados:** [`Objeto Error`](#objeto-error), [`throw`](#throw-lanzamiento-de-errores)

### `Objeto Error`

**¿Qué es?**
El prototipo base en JavaScript que representa una anomalía en la ejecución. Contiene propiedades estándar como `message` (descripción humana del fallo) y `stack` (traza de la pila de ejecución que muestra dónde ocurrió).

**¿Para qué se usa?**
Como el tipo de dato estandarizado para envolver información sobre fallos. JavaScript tiene subtipos nativos (como `TypeError` o `ReferenceError`) que heredan de él.

**Ejemplo:**
```javascript
const miError = new Error("El usuario no tiene permisos.");
console.log(miError.name);    // "Error"
console.log(miError.message); // "El usuario no tiene permisos."
```

**Errores comunes de principiante:**
- Lanzar strings directos en lugar de una instancia de Error (ej. `throw "Hubo un fallo"`), lo que impide capturar el stack trace para saber dónde falló.

**Términos relacionados:** [`throw`](#throw-lanzamiento-de-errores)

### `throw` (Lanzamiento de Errores)

**¿Qué es?**
La palabra clave utilizada para generar una excepción de manera intencional en cualquier punto del programa, interrumpiendo el flujo normal de ejecución hasta que es atrapada por un `catch` superior.

**¿Para qué se usa?**
Para validar lógica de negocio o parámetros de entrada, forzando un estado de error si el programa recibe datos con los que no puede o no debe trabajar.

**Ejemplo:**
```javascript
function procesarEdad(edad) {
  if (typeof edad !== 'number') {
    throw new TypeError("La edad debe ser un número.");
  }
  if (edad < 0) {
    throw new Error("La edad no puede ser negativa.");
  }
  return true;
}
```

**Errores comunes de principiante:**
- Usar `throw` para el control de flujo normal (ej. escapar de un bucle), lo cual degrada seriamente el rendimiento porque generar un stack trace es una operación costosa.

**Términos relacionados:** [`try / catch / finally`](#try--catch--finally)

### `Errores Personalizados (Custom Errors)`

**¿Qué es?**
Clases creadas por el desarrollador que extienden el objeto global `Error` nativo para representar escenarios de fallo muy específicos del dominio de la aplicación (ej. `ValidationError`, `DatabaseError`).

**¿Para qué se usa?**
Para permitir que los bloques `catch` identifiquen fácilmente qué tipo de error ocurrió usando el operador `instanceof` y apliquen lógica de recuperación distinta según el caso.

**Ejemplo:**
```javascript
class ValidationError extends Error {
  constructor(mensaje) {
    super(mensaje);
    this.name = "ValidationError";
  }
}

try {
  throw new ValidationError("Falta el email.");
} catch (error) {
  if (error instanceof ValidationError) {
    console.log("Error de validación capturado.");
  }
}
```

**Errores comunes de principiante:**
- Olvidar llamar a `super(mensaje)` dentro del constructor de la clase hija, lo que impide que la propiedad `message` y la traza de pila se inicialicen correctamente.

**Términos relacionados:** [`Objeto Error`](#objeto-error), [`POO básica`](../javascript/08-poo-basica.md#class-y-constructor)
