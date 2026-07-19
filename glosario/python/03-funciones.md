# 🐍 03 - Funciones

### `def`

**¿Qué es?**
La palabra clave para definir (crear) una función, que es un bloque de código reutilizable al que le pones un nombre.

**¿Para qué se usa?**
Para no repetir el mismo código en varias partes. Escribes la lógica una vez y la llamas cuantas veces quieras.

**Ejemplo:**
```python
def saludar():
    print("Hola")
```

**Errores comunes de principiante:**
- Olvidar los paréntesis `()` o los dos puntos `:` al final de la línea `def`.

**Términos relacionados:** [`return`](#return), [`argumentos`](#argskwargs)

### `parámetros por defecto`

**¿Qué es?**
Valores iniciales que se le dan a las variables de una función para que, si el usuario no las envía al llamarla, la función no falle y use el valor por defecto.

**¿Para qué se usa?**
Para hacer funciones más flexibles y fáciles de usar.

**Ejemplo:**
```python
def saludar(nombre="Amigo"):
    print(f"Hola {nombre}")
saludar() # Imprime "Hola Amigo"
```

**Errores comunes de principiante:**
- Usar tipos de datos mutables (como una lista vacía `[]`) como valor por defecto, lo que causa que la lista se comparta entre todas las llamadas a la función.

**Términos relacionados:** [`def`](#def)

### `*args/**kwargs`

**¿Qué es?**
Sintaxis especial para funciones que pueden recibir cualquier cantidad de argumentos. `*args` agrupa los argumentos sin nombre en una tupla, y `**kwargs` agrupa los argumentos con nombre (clave=valor) en un diccionario.

**¿Para qué se usa?**
Para funciones muy dinámicas donde no sabes cuántos datos te va a pasar el usuario.

**Ejemplo:**
```python
def sumar_todos(*args):
    return sum(args)
print(sumar_todos(1, 2, 3, 4)) # 10
```

**Errores comunes de principiante:**
- Ponerlos en el orden incorrecto al definir la función. El orden debe ser: parámetros normales, `*args`, parámetros con nombre, `**kwargs`.

**Términos relacionados:** [`def`](#def)

### `return`

**¿Qué es?**
La palabra que le indica a la función qué valor debe "escupir" o entregar de vuelta al código que la llamó, terminando la ejecución de la función.

**¿Para qué se usa?**
Para que el resultado de un cálculo pueda guardarse en una variable y usarse después.

**Ejemplo:**
```python
def sumar(a, b):
    return a + b
resultado = sumar(2, 3)
```

**Errores comunes de principiante:**
- Usar `print()` en lugar de `return`. `print` solo muestra en pantalla, pero devuelve `None`, rompiendo el programa si intentas sumar ese resultado después.
- Poner código debajo del `return`; nunca se ejecutará.

**Términos relacionados:** [`def`](#def)

### `lambdas`

**¿Qué es?**
Funciones anónimas de una sola línea. No usan `def` ni tienen nombre.

**¿Para qué se usa?**
Para hacer funciones pequeñitas de usar y tirar, muy comunes cuando otra función te pide una función como argumento (ej. ordenar una lista).

**Ejemplo:**
```python
sumar = lambda a, b: a + b
print(sumar(2, 3))
```

**Errores comunes de principiante:**
- Intentar poner múltiples líneas o lógicas complejas dentro de un lambda. Para eso, usa un `def` normal.

**Términos relacionados:** [`def`](#def)


### `Función pura`

| 🔍 ¿Qué es? | 🎯 ¿Para qué se usa? | 💻 Ejemplo de código | ⚠️ Errores comunes | 🔗 Términos relacionados |
| :--- | :--- | :--- | :--- | :--- |
| Una función sin efectos secundarios | Una función que solo depende de sus argumentos y siempre devuelve el mismo resultado para los mismos datos. Ideal para lógica de negocio y conversiones sin modificar estado global. | ```python
def celsius_a_fahrenheit(c):
    return c * 9/5 + 32
``` | Modificar una variable global o un objeto mutable pasado como argumento dentro de la función, rompiendo la pureza. | [`funciones`](#def) |
