# 04 - Estructuras de datos

### `listas`

**¿Qué es?**
Una colección ordenada de elementos que se puede modificar (agregar, quitar o cambiar elementos). Se define con corchetes `[]`.

**¿Para qué se usa?**
Para agrupar múltiples datos relacionados, como los nombres de los usuarios o los puntajes de los niveles.

**Ejemplo:**
```python
frutas = ["manzana", "banana", "cereza"]
frutas.append("naranja")
```

**Errores comunes de principiante:**
- Intentar acceder a una posición que no existe (`IndexError: list index out of range`). Recuerda que empiezan a contar en 0.

**Términos relacionados:** [`tuplas`](#tuplas)

### `tuplas`

**¿Qué es?**
Similar a una lista, pero INMUTABLE (no se puede modificar una vez creada). Se define con paréntesis `()`.

**¿Para qué se usa?**
Para datos que no deben cambiar nunca durante la ejecución del programa (ej: las coordenadas GPS de una ciudad). Son más rápidas y seguras que las listas.

**Ejemplo:**
```python
coordenadas = (4.6097, -74.0817)
```

**Errores comunes de principiante:**
- Intentar usar `.append()` o modificar un valor (ej: `coordenadas[0] = 5`), lo que causará un `TypeError`.

**Términos relacionados:** [`listas`](#listas)

### `diccionarios (dicts)`

**¿Qué es?**
Una colección de datos en pares de 'clave: valor'. Se definen con llaves `{}`.

**¿Para qué se usa?**
Para estructurar información donde cada dato tiene una etiqueta que lo identifica, muy similar al formato JSON.

**Ejemplo:**
```python
persona = {"nombre": "Ana", "edad": 30}
print(persona["nombre"])
```

**Errores comunes de principiante:**
- Usar listas como claves del diccionario (las claves deben ser inmutables).
- Intentar acceder a una clave que no existe, causando un `KeyError`. Es mejor usar `persona.get('peso', 0)`.

**Términos relacionados:** [`listas`](#listas)

### `sets`

**¿Qué es?**
Una colección desordenada de elementos únicos. No admite duplicados. Se definen con llaves `{}` pero sin los dos puntos `:` de los diccionarios.

**¿Para qué se usa?**
Para limpiar duplicados de una lista de forma instantánea o para ver rápidamente si un elemento existe dentro de un grupo muy grande (es súper rápido).

**Ejemplo:**
```python
numeros_unicos = {1, 2, 2, 3}
# números_unicos quedará como {1, 2, 3}
```

**Errores comunes de principiante:**
- Intentar acceder a un elemento por su posición (ej: `mi_set[0]`), ya que los sets no tienen orden ni posiciones.

**Términos relacionados:** [`listas`](#listas)

### `list comprehension (comprensión de listas)`

**¿Qué es?**
Una forma abreviada y elegante de crear una lista nueva a partir de otra colección en una sola línea.

**¿Para qué se usa?**
Para hacer el código más corto y rápido en lugar de escribir un bucle `for` tradicional con un `.append()` adentro.

**Ejemplo:**
```python
numeros = [1, 2, 3]
cuadrados = [n * n for n in numeros]
```

**Errores comunes de principiante:**
- Abusar de ellas haciéndolas tan largas y complejas que nadie entiende qué hacen. Si es difícil de leer, usa un `for` normal.

**Términos relacionados:** [`listas`](#listas), [`for`](../python/02-control-de-flujo.md#for)

