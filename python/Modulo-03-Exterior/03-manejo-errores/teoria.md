# Teoría: Manejo de Errores — El cinturón de seguridad del código

Imagina que conduces un coche. Sabes que podría haber un accidente. No conduces más despacio (eso sería evitar el error); llevas puesto el cinturón (eso es manejarlo). Si hay un accidente, el cinturón te protege. Si no lo hay, el cinturón no molestó a nadie.

El `try / except` es el cinturón de seguridad de tu código.

---

## Anatomía de `try / except`

```python
try:
    codigo_que_puede_fallar
except NombreDelError:
    codigo_que_se_ejecuta_si_falla
```

Desglose:

- **`try`**: Palabra reservada. Significa "intenta esto". Python ejecuta el código dentro de este bloque.
- **`:`**: Dos puntos obligatorios.
- **`    codigo_que_puede_fallar`**: El bloque indentado que Python intentará ejecutar.
- **`except`**: Palabra reservada. Significa "excepto si ocurre este error". Si el bloque `try` falla, Python salta aquí en lugar de explotar.
- **`NombreDelError`**: El tipo de error que queremos capturar. Los más comunes:
  - `ValueError`: Cuando un dato tiene el formato incorrecto (ej. `int("hola")`).
  - `ZeroDivisionError`: Cuando divides entre cero.
  - `IndexError`: Cuando el índice está fuera del rango de una lista.
  - `KeyError`: Cuando la clave no existe en un diccionario.
- **`    codigo_si_falla`**: El bloque indentado que se ejecuta solo si ocurrió el error.

---

## Ejemplo paso a paso

```python
try:
    numero = int(input("Escribe un número: "))
    print(numero)
except ValueError:
    print("Eso no es un número válido.")
```

**Escenario A** — El usuario escribe `42`:
1. `try` se ejecuta: `int("42")` → `42`. Éxito.
2. `except` se ignora por completo.

**Escenario B** — El usuario escribe `"hola"`:
1. `try` falla: `int("hola")` → `ValueError`.
2. Python salta al `except ValueError`.
3. Se imprime `"Eso no es un número válido."`.
4. El programa **continúa** en lugar de morir.

---

## El bloque `else` y `finally` (opcional)

```python
try:
    numero = int(input("Escribe un número: "))
except ValueError:
    print("Error: eso no es un número.")
else:
    # Se ejecuta SOLO si el try tuvo éxito (no hubo error).
    print("Número recibido correctamente.")
finally:
    # Se ejecuta SIEMPRE, haya error o no.
    print("Proceso terminado.")
```

- **`else`**: Bloque que corre solo cuando `try` fue exitoso.
- **`finally`**: Bloque que corre sin importar qué pasó. Ideal para tareas de limpieza (ej. cerrar un archivo).

---

## ¿Qué pasa si me equivoco?

- **No especificar el tipo de error (`except:` desnudo)**: Captura absolutamente todos los errores, incluso los que no esperabas. Esto puede ocultar bugs graves. Siempre especifica el error que esperas capturar.
- **Código después del error en el `try`**: Si la línea que falla está en medio del bloque `try`, el resto del bloque `try` se salta. El control pasa directamente al `except`.
