# Teoría: Condicionales — Enseñarle a tu programa a tomar decisiones

Imagina un guardia de seguridad en la puerta de un club. Su trabajo es muy simple:

- **SI** el visitante tiene más de 18 años → lo deja pasar.
- **Si NO** → le dice que no puede entrar.

Esa lógica de "SI esto... entonces aquello... si no... lo otro" es exactamente lo que hace un `if` / `else` en Python.

---

## Anatomía del `if`

La estructura básica es:

```python
if condicion:
    accion_si_es_verdad
```

Desglosemos cada pieza:

- **`if`**: Es una palabra reservada de Python que significa "SI". Nunca la uses como nombre de variable.
- **`condicion`**: Es cualquier expresión que resulte en `True` o `False`. Aquí es donde usamos los operadores de comparación del Nivel 04 (`==`, `>`, `<`, etc.).
- **`:`** (dos puntos): Símbolo obligatorio al final de la línea del `if`. Le dice a Python: "aquí termina la pregunta, lo que sigue es la respuesta".
- **`    accion`** (4 espacios adelante): A esto se le llama **indentación**. Es el bloque de código que Python ejecuta **solo si** la condición es `True`. Los espacios no son decoración: son **obligatorios** y deben ser exactamente 4 espacios (o 1 Tab).

---

## Anatomía del `if` / `else`

El `else` captura el caso contrario, cuando la condición es `False`:

```python
if condicion:
    accion_si_es_verdad
else:
    accion_si_es_falso
```

- **`else`**: Significa "SI NO" o "de lo contrario". No lleva condición propia.
- **`:`** (dos puntos): También obligatorio después del `else`.
- El bloque del `else` también debe estar **indentado** con 4 espacios.

---

## Anatomía del `if` / `elif` / `else`

¿Y si hay más de dos caminos? Usamos `elif` (abreviación de "else if", o sea "si no, si..."):

```python
if condicion_1:
    accion_1
elif condicion_2:
    accion_2
else:
    accion_si_ninguna_anterior_fue_verdad
```

Python revisa las condiciones de arriba hacia abajo y ejecuta **solo la primera** que encuentre verdadera.

---

## ¡EL ENEMIGO NÚMERO UNO: LA INDENTACIÓN!

Este es el error más común y frustrante para los principiantes en Python.

```python
# CORRECTO: La acción está indentada con 4 espacios.
if True:
    print("Este código es correcto")

# ERROR: IndentationError. Falta la indentación.
if True:
print("Este código va a fallar")
```

Si ves un error `IndentationError` o `SyntaxError` al correr tu código, la primera sospecha siempre es la indentación.

**Regla de oro:** Todo lo que está "dentro" de un `if`, `elif` o `else` debe tener exactamente 4 espacios al inicio.

---

## ¿Qué pasa si me equivoco?

- **Olvidar el `:`**: Python lanzará un `SyntaxError: expected ':'`. Es la queja más común.
- **Mala indentación**: `IndentationError`. Cuenta tus espacios.
- **Usar `=` en lugar de `==` dentro del `if`**: El programa probablemente no funcione como esperas. Recuerda: `=` guarda, `==` compara.
