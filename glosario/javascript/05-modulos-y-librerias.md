# 🟨 05 - Módulos y librerías

### ES Modules (`import` / `export`)

**¿Qué es?**
Es el sistema de módulos oficial y nativo de JavaScript. Permite dividir el código en múltiples archivos aislando el alcance (scope) de las variables, exportando explícitamente solo lo que se necesita compartir e importándolo en otros archivos.

**¿Para qué se usa?**
Para estructurar aplicaciones grandes, mantener los archivos pequeños, fomentar la reutilización de código y evitar la contaminación del objeto global (window o globalThis). Es el estándar absoluto en el frontend moderno (React, Vue, Angular) y el estándar recomendado en las versiones recientes de Node.js.

**Ejemplo:**
```javascript
// Archivo: math.js
export const PI = 3.14159;
export function calcularArea(radio) {
    return PI * radio * radio;
}

// Archivo: app.js
import { PI, calcularArea } from './math.js';

console.log(`El área con radio 5 es: ${calcularArea(5)}`);
```

**Errores comunes de principiante:**
- En el navegador: olvidar añadir el atributo `type="module"` a la etiqueta `<script>` en el HTML, lo que provoca un error de sintaxis al leer la palabra `import`.
- En Node.js: olvidar configurar `"type": "module"` en el archivo `package.json`, o no usar la extensión `.mjs`.
- Olvidar la extensión del archivo (`.js`) al importar usando módulos nativos en el navegador, ya que a diferencia de los bundlers (como Vite), el navegador necesita la ruta exacta.

**Términos relacionados:** [CommonJS](#commonjs-require--moduleexports)

---

### CommonJS (`require` / `module.exports`)

**¿Qué es?**
Es el sistema de módulos original y tradicional de Node.js. Fue creado antes de que JavaScript tuviera un sistema de módulos oficial (ES Modules). A diferencia de los ES Modules, la importación mediante `require` es síncrona, lo que significa que el hilo de ejecución se bloquea hasta que el módulo es cargado (ideal para el servidor en tiempo de inicio, pero no para el navegador).

**¿Para qué se usa?**
Principalmente para el desarrollo backend con versiones antiguas o código legacy de Node.js. Aunque Node.js está transicionando lentamente hacia ES Modules, CommonJS sigue siendo inmensamente prevalente en el ecosistema de paquetes npm.

**Ejemplo:**
```javascript
// Archivo: utilidades.js (simulado para el ejemplo)
require('fs').writeFileSync('utilidades.js', `
function generarId() {
    return Math.floor(Math.random() * 1000);
}
module.exports = { generarId };
`);

// Importamos el módulo
const { generarId } = require('./utilidades.js');
const fs = require('fs'); // Módulo nativo de Node.js

console.log(`Tu nuevo ID es: ${generarId()}`);
```

**Errores comunes de principiante:**
- Intentar usar `require` directamente en el navegador sin usar una herramienta de empaquetado (como Webpack o Browserify); el navegador lanzará un error porque `require` no existe de forma nativa en la web.
- Mezclar la sintaxis moderna `export` con la sintaxis antigua `require` en el mismo archivo de Node.js sin una configuración de compilación avanzada.

**Términos relacionados:** [ES Modules](#es-modules-import--export)

---

### `npm` y `package.json`

**¿Qué es?**
- **npm (Node Package Manager):** Es el gestor de paquetes por defecto para Node.js y el registro de software más grande del mundo.
- **package.json:** Es un archivo de configuración en formato JSON que reside en la raíz de tu proyecto. Actúa como el "documento de identidad" de tu app, detallando metadatos (nombre, versión) y, lo más importante, la lista exacta de librerías externas de las que depende tu código.

**¿Para qué se usa?**
Para instalar, actualizar y gestionar dependencias de terceros (como Express, React o Lodash) mediante el comando `npm install <paquete>`. Permite que otros desarrolladores clonen tu proyecto e instalen todo lo necesario ejecutando un simple `npm install`.

**Ejemplo:**
```json
// Ejemplo del contenido de un archivo package.json
{
  "name": "mi-proyecto-increible",
  "version": "1.0.0",
  "description": "Una API de prueba",
  "main": "index.js",
  "type": "module", // Habilita ES Modules en Node.js
  "scripts": {
    "start": "node index.js",
    "dev": "nodemon index.js"
  },
  "dependencies": {
    "express": "^4.18.2" // Código de producción
  },
  "devDependencies": {
    "nodemon": "^3.0.1" // Herramientas solo para desarrollo
  }
}
```

**Errores comunes de principiante:**
- Subir la pesadísima y auto-generada carpeta `node_modules` al repositorio (ej. GitHub). Esta carpeta SIEMPRE debe estar ignorada en el archivo `.gitignore`.
- Instalar herramientas globales (como `nodemon` o `jest`) sin guardarlas en el `package.json`, haciendo que el proyecto funcione en tu computadora pero falle en la de tus compañeros.

**Términos relacionados:** [CommonJS](#commonjs-require--moduleexports)

---

### Herramientas de Empaquetado (Bundlers como Vite o Webpack)

**¿Qué es?**
Son herramientas de construcción (build tools) que toman todo el código de tu aplicación (archivos JS, CSS, imágenes, módulos npm) y lo "empaquetan" o compilan en un conjunto muy reducido de archivos estáticos altamente optimizados que el navegador puede entender y descargar rápidamente.

**¿Para qué se usa?**
Para llevar proyectos frontend modernos a producción. Solucionan el problema de que los navegadores no pueden resolver importaciones del tipo `import React from 'react'` (los navegadores necesitan rutas relativas o absolutas, no nombres de paquetes) y permiten usar características avanzadas (como TypeScript o JSX) compilándolas a JavaScript estándar.

**Ejemplo:**
```javascript
// Esto es código válido en un proyecto con Vite o Webpack, 
// pero lanzaría error si se ejecuta directamente en un navegador sin empaquetar, 
// ya que el navegador no sabe dónde buscar la librería "canvas-confetti".

import confetti from 'canvas-confetti';
import './estilos-principales.css'; // ¡Importar CSS dentro de JS!

const boton = document.getElementById("celebrar");
boton.addEventListener("click", () => {
    confetti({
        particleCount: 100,
        spread: 70
    });
});
```

**Errores comunes de principiante:**
- Tratar de abrir el archivo `index.html` de un proyecto de React/Vite haciendo "doble clic" directo desde el explorador de archivos. Estos proyectos requieren ser servidos mediante un servidor local de desarrollo (`npm run dev`) para que el bundler haga su magia en tiempo real.
- Confundir el código fuente (`src/`) que escribes tú, con el código compilado (`dist/` o `build/`) que genera el bundler y es el que finalmente se sube al servidor web de producción.

**Términos relacionados:** [`npm` y `package.json`](#npm-y-packagejson)
