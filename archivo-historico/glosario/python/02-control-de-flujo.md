# 02 - Control de flujo

### `if/elif/else`

**¿Qué es?**
Estructuras de control que le dicen al programa qué camino tomar dependiendo de una condición (si pasa esto, haz esto; si no, haz lo otro).

**¿Para qué se usa?**
Para tomar decisiones lógicas.

**Ejemplo:**
```python
edad = 20
if edad >= 18:
    print("Adulto")
elif edad >= 13:
    print("Adolescente")
else:
    print("Niño")
```

**Errores comunes de principiante:**
- Olvidar los dos puntos `:` al final de la línea.
- Indentar (tabular) mal el bloque de código de adentro.

**Términos relacionados:** [`operadores`](../python/01-fundamentos.md#operadores)

### `for`

**¿Qué es?**
Un bucle (loop) que repite un bloque de código una vez por cada elemento en una colección (como una lista o un rango de números).

**¿Para qué se usa?**
Para no escribir el mismo código muchas veces al procesar listas.

**Ejemplo:**
```python
for numero in [1, 2, 3]:
    print(numero)
```

**Errores comunes de principiante:**
- Intentar modificar la misma lista sobre la que se está iterando, causando comportamientos impredecibles.

**Términos relacionados:** [`while`](#while), [`listas`](../python/04-estructuras-de-datos.md#listas)

### `while`

**¿Qué es?**
Un bucle que repite un bloque de código *mientras* una condición sea verdadera.

**¿Para qué se usa?**
Para repetir acciones cuando no sabes de antemano cuántas veces lo harás (ej: esperar a que un usuario escriba la contraseña correcta).

**Ejemplo:**
```python
contador = 0
while contador < 5:
    print(contador)
    contador += 1
```

**Errores comunes de principiante:**
- Crear un bucle infinito al olvidar actualizar la condición (como olvidar poner `contador += 1`).

**Términos relacionados:** [`for`](#for), [`break/continue`](#breakcontinue)

### `break/continue`

**¿Qué es?**
Palabras clave que alteran el flujo de un bucle. `break` detiene y sale del bucle por completo. `continue` salta a la siguiente repetición ignorando el código que queda.

**¿Para qué se usa?**
Para salir rápido de un bucle si ya encontraste lo que buscabas (`break`), o para ignorar elementos que no te interesan (`continue`).

**Ejemplo:**
```python
for num in range(10):
    if num == 5:
        break # Se detiene en el 5
```

**Errores comunes de principiante:**
- Usarlos fuera de un bucle (causa error de sintaxis).
- Abusar de ellos y hacer que el flujo de tu programa sea un laberinto difícil de leer.

**Términos relacionados:** [`for`](#for), [`while`](#while)

### `match`

**¿Qué es?**
Estructura introducida en Python 3.10 que permite comparar un valor contra muchos patrones distintos, de forma más limpia que usar muchos `elif` seguidos.

**¿Para qué se usa?**
Para manejar casos específicos de forma elegante (similar al `switch` en otros lenguajes).

**Ejemplo:**
```python
comando = "ayuda"
match comando:
    case "salir":
        print("Adiós")
    case "ayuda":
        print("Aquí tienes ayuda")
    case _: # El caso por defecto (como el else)
        print("Comando no reconocido")
```

**Errores comunes de principiante:**
- Intentar usarlo en versiones de Python anteriores a 3.10.
- Olvidar el caso por defecto `case _:` cuando es necesario.

**Términos relacionados:** [`if/elif/else`](#ifelifelse)

