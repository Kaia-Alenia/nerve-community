# Teoría: Archivos — El cuaderno que recuerda todo

Un programa que no puede guardar datos es como un empleado con amnesia: olvida todo al terminar el día. Los archivos son el cuaderno donde ese empleado anota sus apuntes para consultarlos mañana.

---

## La función `open()` y los modos

Para trabajar con un archivo, lo abrimos con `open()`:

```python
archivo = open("mi_archivo.txt", "w")
```

Desglose:

- **`open`**: La herramienta de Python para abrir archivos.
- **`"mi_archivo.txt"`**: El nombre del archivo. Si no existe, Python lo crea (en modo escritura). La ruta es relativa a donde ejecutas el script.
- **`"w"`**: El **modo** de apertura. Le dice a Python qué quieres hacer:

| Modo | Significado | ¿Qué hace si el archivo ya existe? |
|------|-------------|-----------------------------------|
| `"r"` | Read (leer) | Lo abre para leer. Error si no existe. |
| `"w"` | Write (escribir) | Lo crea o lo **borra y reemplaza** si ya existía. |
| `"a"` | Append (añadir) | Añade al final sin borrar lo que había. |

---

## La forma correcta: `with open(...)`

En lugar de abrir y cerrar manualmente el archivo, Python ofrece la instrucción `with`, que lo cierra automáticamente al terminar:

```python
with open("mi_archivo.txt", "w") as archivo:
    archivo.write("Hola desde Python.\n")
```

Desglose:

- **`with`**: Palabra reservada. Gestiona el ciclo de vida del archivo automáticamente.
- **`open(...)`**: Abre el archivo.
- **`as archivo`**: Le da un nombre temporal a la conexión con el archivo. Puedes llamarlo como quieras.
- **`:`**: Dos puntos obligatorios.
- **`    archivo.write(...)`**: Dentro del bloque indentado, escribimos en el archivo.
- **`"\n"`**: El símbolo de **salto de línea**. Es como presionar Enter dentro del archivo. Sin él, todo se escribiría en una sola línea.

---

## Escribir: `.write()`

```python
with open("notas.txt", "w") as f:
    f.write("Primera línea.\n")
    f.write("Segunda línea.\n")
```

---

## Leer todo el contenido: `.read()`

```python
with open("notas.txt", "r") as f:
    contenido = f.read()
    print(contenido)
```

---

## Leer línea por línea con `for`

El `for` también funciona sobre archivos: itera línea por línea.

```python
with open("notas.txt", "r") as f:
    for linea in f:
        print(linea)
```

---

## Añadir sin borrar: modo `"a"`

```python
with open("notas.txt", "a") as f:
    f.write("Tercera línea añadida después.\n")
```

---

## ¿Qué pasa si me equivoco?

- **Leer un archivo que no existe**: `FileNotFoundError`. Usa `try / except FileNotFoundError` para manejarlo.
- **Olvidar el `\n`**: Todo el texto aparece en una sola línea en el archivo. No es un error de Python, pero es un error de formato.
- **Usar modo `"w"` cuando querías `"a"`**: Borrarás accidentalmente el contenido del archivo. Siempre verifica el modo antes de abrir.
