# 01 - Fundamentos

### `variables`

**¿Qué es?**
Contenedores en la memoria de la computadora donde guardamos un dato para usarlo después.

**¿Para qué se usa?**
Para almacenar información temporalmente, como el nombre de un usuario o el puntaje de un juego.

**Ejemplo:**
```python
nombre = "Ana"
edad = 30
```

**Errores comunes de principiante:**
- Usar nombres confusos (ej: `x = 10` en lugar de `vidas = 10`).
- Usar palabras reservadas del lenguaje (como `if` o `for`).

**Términos relacionados:** [`tipos de datos`](#tipos-de-datos-str-int-float-bool-none)

### `tipos de datos (str, int, float, bool, None)`

**¿Qué es?**
Clasificaciones de la información. `str` es texto, `int` son números enteros, `float` son números con decimales, `bool` es verdadero o falso, y `None` representa la ausencia de valor.

**¿Para qué se usa?**
Para saber qué operaciones podemos hacer. No puedes sumar un texto con un número sin convertirlos primero.

**Ejemplo:**
```python
texto = "Hola" # str
entero = 5 # int
decimal = 3.14 # float
activo = True # bool
vacio = None # None
```

**Errores comunes de principiante:**
- Dividir dos enteros en versiones viejas de Python daba un entero.
- Usar comas en lugar de puntos para decimales (`3,14` crea una tupla, no un float).

**Términos relacionados:** [`variables`](#variables)

### `operadores`

**¿Qué es?**
Símbolos especiales que realizan operaciones sobre variables y valores, como sumar (`+`), restar (`-`), comparar (`==`) o asignar (`=`).

**¿Para qué se usa?**
Para hacer cálculos matemáticos o tomar decisiones lógicas en el código.

**Ejemplo:**
```python
suma = 5 + 3
es_igual = (suma == 8) # Devuelve True
```

**Errores comunes de principiante:**
- Confundir `=` (asignación) con `==` (comparación).
- Olvidar que la división `/` siempre devuelve un float, incluso si el resultado es exacto.

**Términos relacionados:** [`variables`](#variables), [`if/elif/else`](../python/02-control-de-flujo.md#ifelifelse)

### `f-strings`

**¿Qué es?**
Una forma moderna y limpia de meter el valor de variables dentro de un texto (string). Se pone una `f` antes de las comillas y las variables van entre llaves `{}`.

**¿Para qué se usa?**
Para construir mensajes de forma fácil sin tener que concatenar (sumar) textos y convertir números manualmente.

**Ejemplo:**
```python
nombre = "Carlos"
print(f"Hola {nombre}, bienvenido.")
```

**Errores comunes de principiante:**
- Olvidar poner la `f` antes de las comillas, lo que hace que imprima literalmente `{nombre}`.
- Intentar usarlos en versiones de Python anteriores a 3.6.

**Términos relacionados:** [`tipos de datos (str)`](#tipos-de-datos-str-int-float-bool-none-str-int-float-bool-none)

### `comentarios`

**¿Qué es?**
Anotaciones en el código que la computadora ignora por completo. Empiezan con el símbolo `#`.

**¿Para qué se usa?**
Para explicar partes difíciles del código a otros humanos (o a ti mismo en el futuro).

**Ejemplo:**
```python
# Esto calcula el total con impuestos
precio = 100
total = precio * 1.16
```

**Errores comunes de principiante:**
- Escribir comentarios obvios (ej: `# suma 1 a x` encima de `x = x + 1`).
- Olvidar actualizar los comentarios cuando cambias el código, dejando mentiras en el texto.

**Términos relacionados:** [`variables`](#variables)

### `indentación`

**¿Qué es?**
Los espacios (o tabulaciones) al principio de una línea de código. En Python, estos espacios no son por estética, son obligatorios para agrupar bloques de código.

**¿Para qué se usa?**
Para decirle a Python qué código pertenece adentro de un `if`, un `for` o una función. Si no indentas correctamente, el código no funcionará.

**Ejemplo:**
```python
if True:
    print("Esto está adentro del if") # 4 espacios de indentación
print("Esto está afuera del if")
```

**Errores comunes de principiante:**
- Mezclar espacios y tabulaciones en el mismo archivo (Python 3 lanzará un error `TabError`).
- Olvidar indentar después de los dos puntos `:`.

**Términos relacionados:** [`if/elif/else`](../python/02-control-de-flujo.md#ifelifelse), [`funciones`](../python/03-funciones.md#def)

### `linter`

**¿Qué es?**
Una herramienta automática que analiza tu código en busca de errores estilísticos, malas prácticas o errores de sintaxis, antes de que lo ejecutes.

**¿Para qué se usa?**
Para mantener un código limpio, uniforme y fácil de leer, especialmente cuando trabajas en equipo. Te "regaña" de forma compasiva (como el Linter Compasivo del repo) para que mejores.

**Ejemplo:**
Herramientas como `flake8` actúan como linters.
```bash
# Ejecutar un linter en tu código
flake8 mi_script.py
```

**Errores comunes de principiante:**
- Ignorar las advertencias del linter pensando que "si funciona, está bien", acumulando deuda técnica (código sucio).

**Términos relacionados:** [`comentarios`](#comentarios)
