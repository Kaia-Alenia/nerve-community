# Reto 13: El Validador de Contraseña 🔐

Vas a crear un sistema de validación de contraseña que no se caiga ante entradas incorrectas.

## Instrucciones

Crea tu archivo en `solucion/` con el nombre `tu-usuario-13.py` y sigue los pasos:

1. Define una función llamada `validar_pin` que reciba un parámetro `intento_texto` (texto `str`). Dentro de la función:
   - Usa un bloque `try / except / else` para intentar convertir `intento_texto` a `int`.
   - En el `except ValueError`: devuelve con `return` el texto `"Error: el PIN debe ser un número."`.
   - En el `else` (conversión exitosa): usa un `if` para revisar si el número es exactamente `1234`. Si sí: devuelve `"Acceso concedido."`. Si no: devuelve `"PIN incorrecto."`.

2. Fuera de la función, crea una lista llamada `intentos` con los siguientes 3 valores de texto: `["abc", "9999", "1234"]`.

3. Usa un bucle `for` para recorrer `intentos`. En cada vuelta, llama a `validar_pin()` con el elemento actual y guarda el resultado. Luego imprímelo.

**Resultado esperado en tu terminal:**
```text
--- Validando intentos ---
Error: el PIN debe ser un número.
PIN incorrecto.
Acceso concedido.
```

Ejecuta desde la raíz del proyecto:
- **macOS / Linux:** `python3 python/Modulo-03-Exterior/03-manejo-errores/solucion/tu-usuario-13.py`
- **Windows:** `python python/Modulo-03-Exterior/03-manejo-errores/solucion/tu-usuario-13.py`
