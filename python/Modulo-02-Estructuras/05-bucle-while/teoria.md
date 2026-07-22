# Teoría: El Bucle while — El guardia que no se mueve hasta que cambia algo

Imagina un guardia en la entrada de una sala VIP. Su instrucción es: **"Mientras la sala esté llena, no dejes entrar a nadie."** El guardia no sabe cuánto tiempo tardará en haber espacio; simplemente sigue revisando hasta que la condición cambie.

Eso es el `while`.

---

## Anatomía del `while`

```python
while condicion:
    accion_que_se_repite
```

Desglose:

- **`while`**: Palabra reservada. Significa "mientras".
- **`condicion`**: Una expresión que devuelve `True` o `False` (igual que en el `if` del Nivel 05). Mientras sea `True`, el bucle continúa. Cuando se vuelve `False`, el bucle se detiene.
- **`:`**: Los dos puntos obligatorios.
- **`    accion`**: El bloque indentado (4 espacios) que se repite.

---

## Ejemplo básico: la cuenta regresiva

```python
contador = 5

while contador > 0:
    print(contador)
    contador = contador - 1

print("¡Despegue!")
```

**Lo que pasa vuelta por vuelta:**

| Vuelta | `contador` | ¿`contador > 0`? | Acción |
|--------|-----------|-----------------|--------|
| 1ª | `5` | `True` | Imprime `5`, luego `contador` pasa a `4` |
| 2ª | `4` | `True` | Imprime `4`, luego `contador` pasa a `3` |
| ... | ... | ... | ... |
| 5ª | `1` | `True` | Imprime `1`, luego `contador` pasa a `0` |
| Fin | `0` | `False` | El bucle se detiene. Se imprime `"¡Despegue!"` |

---

## La trampa mortal: el bucle infinito

Si la condición del `while` **nunca se vuelve `False`**, el programa se queda atrapado para siempre. A esto se llama **bucle infinito** y es el error más peligroso del `while`:

```python
# PELIGRO: bucle infinito. contador nunca cambia.
contador = 5
while contador > 0:
    print(contador)
    # FALTA: contador = contador - 1
```

Si ejecutas esto por accidente, presiona `Ctrl + C` en la terminal para detener el programa a la fuerza.

**Regla de oro:** Siempre asegúrate de que algo dentro del `while` modifique la variable de la condición para que eventualmente se vuelva `False`.

---

## `for` vs `while` — ¿Cuándo usar cada uno?

| Situación | Usa... |
|---|---|
| Sé exactamente cuántas veces necesito repetir (recorrer una lista, un rango) | **`for`** |
| No sé cuántas veces se repetirá; depende de una condición que puede cambiar | **`while`** |

---

## ¿Qué pasa si me equivoco?

- **Bucle infinito**: El programa se congela. Usa `Ctrl + C` para salir.
- **Olvidar actualizar el contador**: El error más común del `while`. La condición nunca cambia → bucle infinito.
- **Olvidar el `:`**: `SyntaxError`, igual que en el `if` y el `for`.
