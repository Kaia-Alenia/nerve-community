# Teoría: Input del Usuario — El programa que escucha

Hasta ahora tus programas eran monólogos: solo hablaban, nunca escuchaban. `input()` convierte tu programa en un diálogo.

Imagina un cajero automático: te muestra un mensaje ("Ingrese su PIN"), espera a que escribas, y luego actúa según lo que recibió.

---

## Anatomía de `input()`

```python
nombre = input("¿Cuál es tu nombre? ")
```

Desglose:

- **`nombre`**: La variable donde guardaremos lo que el usuario escriba.
- **`=`**: Asignación. El resultado de `input()` se guarda en esta variable.
- **`input`**: La herramienta de Python para escuchar al usuario.
- **`(...)`**: Los paréntesis le entregan a `input` el mensaje que mostrará al usuario.
- **`"¿Cuál es tu nombre? "`**: El mensaje (texto entre comillas) que aparece en la terminal antes de que el usuario escriba. El espacio al final es cosmético: evita que el cursor quede pegado al texto.

Cuando Python llega a esta línea:
1. Imprime `¿Cuál es tu nombre? ` en la terminal.
2. El programa se **pausa** completamente.
3. El usuario escribe y presiona **Enter**.
4. Python guarda lo escrito como texto (`str`) en la variable `nombre`.

---

## ¡TRAMPA CRÍTICA! `input()` SIEMPRE devuelve texto (`str`)

Esta es la trampa más importante de este nivel. No importa si el usuario escribe `42` o `3.14`: Python siempre lo trata como texto (`str`).

```python
edad = input("¿Cuántos años tienes? ")
# Si el usuario escribe 20, 'edad' guarda el texto "20", no el número 20.
```

Si intentas hacer matemáticas con ese texto, obtendrás un `TypeError`.

### Solución: convertir el tipo de dato

Para convertir el texto a número entero, envolvemos `input()` con `int()`:

```python
edad = int(input("¿Cuántos años tienes? "))
```

- **`int(...)`**: Convierte lo que está dentro a un número entero. Si el usuario escribe `"20"`, `int("20")` devuelve el número `20`.
- **`float(...)`**: Convierte a número con decimales. `float("3.14")` → `3.14`.

### Anatomía de la conversión:

```
edad = int( input("¿Cuántos años tienes? ") )
  ^      ^        ^
  |      |        └── input() captura texto del usuario: "20"
  |      └─────────── int() convierte ese texto al número: 20
  └────────────────── = guarda el número en 'edad'
```

---

## ¿Qué pasa si me equivoco?

- **No convertir a `int` cuando necesitas número**: `TypeError` al intentar sumar el texto con un número.
- **El usuario escribe texto cuando esperabas número**: Si usas `int(input(...))` y el usuario escribe `"hola"`, Python lanzará un `ValueError: invalid literal for int()`. El Nivel 13 (Manejo de Errores) resolverá esto.
- **Olvidar el espacio al final del mensaje**: Es válido, pero el cursor del usuario quedará pegado al texto, viéndose feo.
