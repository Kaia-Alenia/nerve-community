# Teoría: El Bucle for — La cinta transportadora

Imagina la cinta de un supermercado: pones todos tus productos uno por uno, y el cajero los procesa de izquierda a derecha, uno a la vez, hasta que no quedan más. Eso es exactamente un bucle `for`.

---

## Anatomía del `for`

```python
for elemento in coleccion:
    accion_con_elemento
```

Desglose de cada pieza:

- **`for`**: Palabra reservada. Significa "para cada".
- **`elemento`**: Un nombre de variable que **tú inventas**. Python usará este nombre para guardar el elemento actual en cada vuelta del bucle. Puedes llamarlo como quieras (`fruta`, `nombre`, `item`, `x`).
- **`in`**: Palabra reservada. Significa "dentro de". Conecta la variable temporal con la colección.
- **`coleccion`**: La lista, tupla u otra colección que vas a recorrer.
- **`:`**: Los dos puntos obligatorios al final de la línea, igual que en el `if`.
- **`    accion`**: El bloque de código indentado (4 espacios) que se ejecuta en **cada vuelta**.

---

## Ejemplo básico

```python
frutas = ["manzana", "plátano", "uva"]

for fruta in frutas:
    print(fruta)
```

**Lo que pasa internamente, vuelta por vuelta:**

| Vuelta | `fruta` vale... | Se ejecuta |
|--------|----------------|-----------|
| 1ª | `"manzana"` | `print("manzana")` |
| 2ª | `"plátano"` | `print("plátano")` |
| 3ª | `"uva"` | `print("uva")` |
| Fin | La lista se acabó. El bucle termina. | — |

---

## `range()`: contar números sin crear una lista

¿Qué pasa si quieres repetir algo un número exacto de veces? `range()` genera una secuencia de números para ti:

```python
for numero in range(5):
    print(numero)
# Imprime: 0, 1, 2, 3, 4
```

- **`range(5)`**: Genera los números `0, 1, 2, 3, 4`. Empieza en 0 y llega **hasta antes** del número indicado (no incluye el 5).
- **`range(1, 6)`**: Genera `1, 2, 3, 4, 5`. El primer número es el inicio (incluido), el segundo es el tope (excluido).

---

## ¡El `for` también tiene indentación!

Al igual que el `if`, todo lo que quieras que se repita **debe ir con 4 espacios** dentro del bloque del `for`. Si olvidas la indentación, obtendrás un `IndentationError`.

---

## ¿Qué pasa si me equivoco?

- **No indentar**: `IndentationError`. El código "dentro" del `for` necesita sus 4 espacios.
- **Olvidar el `:`**: `SyntaxError`. Los dos puntos después de `in coleccion` son obligatorios.
- **Modificar la lista mientras la recorres**: Es una práctica peligrosa que puede causar comportamientos inesperados. Evítalo por ahora.
