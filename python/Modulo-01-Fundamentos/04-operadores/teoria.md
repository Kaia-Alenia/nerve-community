# Teoría: Operadores — Los verbos de las matemáticas y las preguntas

Ya sabes guardar datos en cajas (variables). Ahora aprenderás a **hacer cosas** con esos datos.

---

## Familia 1: Operadores Aritméticos

Imagina una calculadora de bolsillo. Los operadores aritméticos son exactamente esos botones que ya conoces, pero con alguna sorpresa.

| Símbolo | Nombre | Qué hace | Ejemplo | Resultado |
|---------|--------|----------|---------|-----------|
| `+` | Suma | Suma dos números | `10 + 3` | `13` |
| `-` | Resta | Resta el derecho del izquierdo | `10 - 3` | `7` |
| `*` | Multiplicación | **Ojo:** no es la `x` del cuaderno, es el asterisco | `10 * 3` | `30` |
| `/` | División | Divide. El resultado **siempre** tiene decimales | `10 / 3` | `3.333...` |
| `//` | División Entera | Divide y **descarta** los decimales, solo devuelve la parte entera | `10 // 3` | `3` |
| `%` | Módulo (Residuo) | Divide y te da el **sobrante** | `10 % 3` | `1` |

### Anatomía: el operador `%` (módulo)

Este es el más raro para los principiantes. Piensa en él como la respuesta a: *"Si reparto 10 galletas entre 3 amigos, ¿cuántas galletas sobran?"*. La respuesta es `1` (3+3+3=9, sobra 1). El `%` da esa galleta sobrante.

---

## Familia 2: Operadores de Comparación

Aquí Python hace algo muy interesante: en lugar de calcular un número, responde una **pregunta de Verdadero o Falso**. El resultado siempre es un **Booleano** (`True` o `False`), que ya conocemos del Nivel 03.

| Símbolo | Pregunta que hace | Ejemplo | Resultado |
|---------|------------------|---------|-----------|
| `==` | ¿Son iguales? | `5 == 5` | `True` |
| `!=` | ¿Son diferentes? | `5 != 3` | `True` |
| `>` | ¿El izquierdo es mayor? | `10 > 3` | `True` |
| `<` | ¿El izquierdo es menor? | `3 < 10` | `True` |
| `>=` | ¿Mayor o igual? | `5 >= 5` | `True` |
| `<=` | ¿Menor o igual? | `3 <= 10` | `True` |

### ¡TRAMPA MORTAL! El `=` vs el `==`

Este es el error que comete **todo principiante** al menos una vez:

- **`=`** (un solo igual): Es la **asignación**. Le dice a Python "guarda este valor en esta caja". Lo conocemos del Nivel 02.
- **`==`** (dos iguales juntos): Es la **comparación**. Le pregunta a Python "¿estos dos valores son idénticos?".

```python
# GUARDAR un valor en una caja:
puntos = 100

# PREGUNTAR si dos valores son iguales (resultado: True o False):
puntos == 100
```

Usa un `=` cuando quieres guardar. Usa `==` cuando quieres preguntar.

---

## ¿Qué pasa si me equivoco?

- **Dividir por cero**: Si escribes `10 / 0`, Python lanzará un `ZeroDivisionError`. La computadora no puede dividir entre nada, igual que en matemáticas.
- **Operar tipos distintos**: Aún no puedes mezclar texto con números directamente. `"hola" + 5` generará un `TypeError`. El operador `+` con texto funciona diferente (lo veremos en un nivel futuro).
