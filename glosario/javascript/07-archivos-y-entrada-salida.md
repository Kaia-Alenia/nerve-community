# 07 - Archivos y entrada/salida

### `Módulo fs (File System)`

**¿Qué es?**
El módulo central nativo de Node.js diseñado para interactuar con el sistema de archivos del sistema operativo (lectura, escritura, borrado y metadatos de archivos y directorios).

**¿Para qué se usa?**
Para cualquier operación de disco en aplicaciones backend o scripts de terminal. No existe en el entorno del navegador por razones de seguridad. Se recomienda usar su versión basada en promesas (`fs/promises`).

**Ejemplo:**
```javascript
const fs = require('fs/promises');

async function leerConfig() {
  try {
    const contenido = await fs.readFile('config.txt', 'utf-8');
    console.log(contenido);
  } catch (error) {
    console.error("No se pudo leer el archivo");
  }
}
```

**Errores comunes de principiante:**
- Usar los métodos síncronos (como `fs.readFileSync`) en el hilo principal de un servidor web, lo cual bloquea a todos los demás usuarios conectados mientras el disco responde.

**Términos relacionados:** [`Módulo path`](#módulo-path)

### `Módulo path`

**¿Qué es?**
Una utilidad nativa de Node.js que proporciona herramientas para trabajar y manipular rutas de archivos y directorios de forma segura y cruzada (cross-platform).

**¿Para qué se usa?**
Para construir rutas absolutas o relativas que funcionen igual en Windows (donde se usan contrabarras `\`) que en Linux/macOS (donde se usan barras `/`), evitando rutas hardcodeadas (ej. `"carpeta/archivo.txt"`).

**Ejemplo:**
```javascript
const path = require('path');

// Construye una ruta segura usando el directorio actual
const rutaSegura = path.join(__dirname, 'archivos', 'datos.json');
console.log(rutaSegura);
// Extracción de la extensión
console.log(path.extname('foto.jpg')); // ".jpg"
```

**Errores comunes de principiante:**
- Concatenar strings a mano (ej. `__dirname + '/' + 'archivo.txt'`) en vez de usar `path.join()`, lo que inevitablemente causa bugs al correr el código en diferentes sistemas operativos.

**Términos relacionados:** [`Módulo fs`](#módulo-fs-file-system)

### `JSON (JavaScript Object Notation)`

**¿Qué es?**
Un formato de texto ligero y estandarizado para el intercambio de datos. Aunque su sintaxis se deriva de los objetos literales de JavaScript, es un string puramente basado en texto.

**¿Para qué se usa?**
Es el estándar de facto para enviar datos desde una API backend a un cliente frontend, o para guardar configuraciones. Requiere `JSON.parse()` para convertir texto a objeto JS, y `JSON.stringify()` para convertir de objeto JS a texto.

**Ejemplo:**
```javascript
// Objeto en memoria
const usuario = { nombre: "Ana", edad: 30 };

// Serializar a texto JSON para guardar/enviar
const jsonTexto = JSON.stringify(usuario);

// Deserializar de vuelta a un objeto JS
const objetoRestaurado = JSON.parse(jsonTexto);
```

**Errores comunes de principiante:**
- Intentar acceder a las propiedades de un string JSON directamente (ej. `respuesta.nombre`) sin haberlo pasado antes por `JSON.parse()`.

**Términos relacionados:** [`Objetos`](../javascript/04-estructuras-de-datos.md#objetos-literales)

### `Streams (Flujos de datos)`

**¿Qué es?**
Una abstracción de Node.js que permite leer o escribir información de forma secuencial, dividiendo los datos en fragmentos pequeños (chunks) en lugar de cargar todo en memoria a la vez.

**¿Para qué se usa?**
Son vitales para procesar archivos muy grandes o transferencias de red pesadas (como descargas o streaming de video) donde cargar un archivo de 5GB saturaría la RAM del servidor.

**Ejemplo:**
```javascript
const fs = require('fs');
fs.writeFileSync('archivo_gigante.txt', 'Simulación de archivo gigante');

// Leer un archivo gigante pedazo por pedazo
const readStream = fs.createReadStream('archivo_gigante.txt', 'utf-8');

readStream.on('data', (chunk) => {
  console.log('Se recibió un fragmento de:', chunk.length, 'caracteres');
});
```

**Errores comunes de principiante:**
- Usar `fs.readFile` (que lee el archivo entero en la RAM) para servir videos o archivos pesados en un backend de Express, tumbando el servidor por falta de memoria.

**Términos relacionados:** [`Módulo fs`](#módulo-fs-file-system)
