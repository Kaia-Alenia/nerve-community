# Teoría: Listas — El vagón de tren de los datos

Imagina una lista de compras en papel: está escrita en orden, puedes añadir cosas al final, tachar cosas del medio, y siempre sabes cuántos artículos hay contando los renglones.

En Python, una **Lista** funciona exactamente igual.

---

## Anatomía de una Lista

Para crear una lista, usamos **corchetes** `[ ]` y separamos cada elemento con una **coma** `,`:

```python
frutas = ["manzana", "plátano", "uva"]
```

Desglose de cada símbolo:

- `frutas`: El nombre de la variable (la "etiqueta" de la caja, del Nivel 02).
- `=`: El símbolo de asignación/guardado (del Nivel 02). Guarda la lista en la variable.
- `[`: Abre la lista. Le dice a Python "aquí empieza la colección".
- `"manzana"`, `"plátano"`, `"uva"`: Los elementos de la lista. Cada uno es un dato (en este caso, texto `str` del Nivel 03).
- `,`: La coma **separa** un elemento del siguiente. Sin coma, Python pensaría que es todo un único elemento.
- `]`: Cierra la lista.

---

## Cómo acceder a un elemento: el Índice

Cada elemento de la lista tiene una **posición numérica** llamada **índice**. La regla más importante:

> **Python empieza a contar desde CERO, no desde UNO.**

```python
frutas = ["manzana", "plátano", "uva"]
#            ^índice 0   ^índice 1  ^índice 2
```

Para obtener un elemento, escribimos el nombre de la lista seguido del índice entre corchetes:

```python
primera_fruta = frutas[0]   # Guarda "manzana"
segunda_fruta = frutas[1]   # Guarda "plátano"
```

- `frutas`: El nombre de la lista.
- `[0]`: El índice entre corchetes. Le dice a Python "dame el elemento en la posición 0".

---

## Operaciones básicas

### Conocer el tamaño: `len()`

`len()` es una herramienta que Python ya tiene lista para ti. Le pasas una lista y te dice cuántos elementos tiene:

```python
total = len(frutas)   # total = 3
```

- `len`: El nombre de la herramienta (la aprenderás a profundidad en módulos futuros).
- `(frutas)`: Los paréntesis le "entregan" la lista a `len` para que la cuente.

### Añadir un elemento al final: `.append()`

```python
frutas.append("naranja")
# La lista ahora es: ["manzana", "plátano", "uva", "naranja"]
```

- `.append(...)`: Un punto seguido de `append` y los datos entre paréntesis. El punto significa "hazle esto **a** la lista `frutas`". Por ahora memorízalo como la acción de "añadir al final".

### Eliminar un elemento por posición: `.pop()`

```python
frutas.pop(1)
# Elimina el elemento en la posición 1 ("plátano")
# La lista ahora es: ["manzana", "uva", "naranja"]
```

---

## ¿Qué pasa si me equivoco?

- **Índice fuera de rango**: Si tu lista tiene 3 elementos (índices 0, 1, 2) y pides `frutas[5]`, Python lanzará un `IndexError: list index out of range`. Siempre verifica que el índice que pides exista.
- **Olvidar las comas**: `["manzana" "plátano"]` sin coma causará un `SyntaxError`. La coma es el separador obligatorio.
- **Confundir `( )` con `[ ]`**: Los paréntesis son para otras cosas. Para crear listas y acceder a elementos, siempre se usan corchetes `[ ]`.
