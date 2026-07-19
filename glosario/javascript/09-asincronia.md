# 🟨 09 - Asincronía

### `Event Loop (Bucle de Eventos)`

**¿Qué es?**
El mecanismo arquitectónico subyacente que permite a JavaScript ser "no bloqueante" a pesar de ser un lenguaje de un solo hilo (single-threaded). Supervisa el *Call Stack* y el *Callback Queue*.

**¿Para qué se usa?**
No es algo que uses directamente como desarrollador, sino el modelo mental que debes comprender para saber en qué orden se ejecutarán tus tareas asíncronas, temporizadores y llamadas a la red.

**Ejemplo:**
```javascript
console.log("1. Inicio");
setTimeout(() => console.log("3. Tarea asíncrona"), 0);
console.log("2. Fin");
// Imprime 1, luego 2, y por último 3.
```

**Errores comunes de principiante:**
- Asumir que `setTimeout(fn, 0)` se ejecutará instantáneamente en el orden del código. El Event Loop siempre terminará el hilo principal (síncrono) antes de procesar la cola asíncrona.

**Términos relacionados:** [`setTimeout`](#settimeout--setinterval), [`Asincronía`](#promesas-promises)

### `setTimeout / setInterval`

**¿Qué es?**
Funciones globales provistas por el entorno (navegador o Node.js) para programar la ejecución de un callback (función) después de un retraso de tiempo o en intervalos periódicos.

**¿Para qué se usa?**
Para retrasar acciones, crear animaciones simples, hacer polling a un servidor periódicamente o diferir operaciones pesadas para evitar congelar la interfaz gráfica.

**Ejemplo:**
```javascript
const timer = setTimeout(() => {
  console.log("Pasaron 2 segundos");
}, 2000);

// setInterval repite infinitamente
const intervalo = setInterval(() => {
  console.log("Latido...");
}, 1000);

// Para cancelarlos
clearTimeout(timer);
clearInterval(intervalo);
```

**Errores comunes de principiante:**
- Olvidar almacenar el ID retornado por `setInterval` y omitir llamar a `clearInterval`, creando bucles infinitos "fantasma" que consumen memoria o corrompen el estado visual (memory leaks).

**Términos relacionados:** [`Event Loop`](#event-loop-bucle-de-eventos)

### `Promesas (Promises)`

**¿Qué es?**
Objetos especiales de JavaScript que representan el resultado eventual (éxito o fracaso) de una operación asíncrona. Pueden estar en tres estados: pendiente (*pending*), resuelta (*fulfilled*) o rechazada (*rejected*).

**¿Para qué se usa?**
Para estructurar peticiones a red o lecturas de disco sin caer en el infierno de callbacks anidados (*Callback Hell*). Permiten encadenar lógicas mediante métodos `.then()` y manejar fallos en `.catch()`.

**Ejemplo:**
```javascript
fetch("https://api.github.com/users")
  .then((respuesta) => respuesta.json())
  .then((datos) => console.log("Usuarios cargados", datos))
  .catch((error) => console.error("Error de red:", error));
```

**Errores comunes de principiante:**
- Olvidar retornar la promesa en el interior de un `.then()`, rompiendo la cadena y causando errores sutiles de sincronización.
- Olvidar el `.catch()`, causando excepciones "Unhandled Promise Rejection" que rompen aplicaciones Node.

**Términos relacionados:** [`async / await`](#async--await)

### `async / await`

**¿Qué es?**
Azúcar sintáctico moderno introducido en ES8 (2017) que se asienta directamente sobre las Promesas, permitiendo que el código asíncrono se lea de forma imperativa y síncrona.

**¿Para qué se usa?**
Para evitar el uso de cadenas de `.then()`, logrando un código más limpio, legible y fácil de debugear. `await` pausa la ejecución visual de la función (sin bloquear el hilo) hasta que la Promesa resuelve.

**Ejemplo:**
```javascript
async function cargarUsuarios() {
  try {
    const respuesta = await fetch("https://api.github.com/users");
    const datos = await respuesta.json();
    console.log(datos);
  } catch (error) {
    console.error("Algo falló al cargar", error);
  }
}
```

**Errores comunes de principiante:**
- Usar la palabra `await` en una función que no fue marcada explícitamente con `async` (error de sintaxis).
- Olvidar envolver la lógica en un bloque `try/catch` para manejar errores asíncronos cuando fallan, ya que no hay `.catch()` encadenado.

**Términos relacionados:** [`Promesas`](#promesas-promises), [`try/catch`](../javascript/06-manejo-de-errores.md#try--catch--finally)
