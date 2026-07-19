# 🐍 06 - Manejo de errores

### `try/except/finally`

**¿Qué es?**
El bloque de código que atrapa y maneja errores para evitar que el programa se estrelle.

**¿Para qué se usa?**
Le dices a Python: 'Intenta hacer esto (try). Si falla, haz esto otro (except). Y pase lo que pase, al final ejecuta esto (finally)'.

**Ejemplo:**
```python
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("No dividas por cero")
finally:
    print("Esto siempre se ejecuta")
```

**Errores comunes de principiante:**
- Usar un `except:` genérico que atrapa CUALQUIER error, lo que oculta bugs de sintaxis y hace imposible depurar el programa.

**Términos relacionados:** [`raise`](#raise)

### `raise`

**¿Qué es?**
La palabra clave para generar o 'lanzar' un error intencionalmente.

**¿Para qué se usa?**
Cuando tu código detecta una situación inválida (ej. edad negativa) y quieres avisarle al resto del programa que algo salió mal.

**Ejemplo:**
```python
edad = -5
try:
    if edad < 0:
        raise ValueError("La edad no puede ser negativa")
except ValueError:
    pass
```

**Errores comunes de principiante:**
- Lanzar un `Exception` genérico en lugar de un error específico (`ValueError`, `TypeError`), lo que dificulta atraparlo limpiamente más arriba.

**Términos relacionados:** [`try/except/finally`](#tryexceptfinally)

### `excepciones comunes`

**¿Qué es?**
Los tipos de errores más frecuentes que verás en Python, como `ValueError` (valor incorrecto), `TypeError` (tipo de dato incorrecto), `FileNotFoundError` (archivo no encontrado).

**¿Para qué se usa?**
Son las alarmas del lenguaje. Conocerlas te permite saber exactamente qué falló.

**Ejemplo:**
```python
try:
    int("hola") # Causa ValueError
except ValueError:
    pass
```

**Errores comunes de principiante:**
- Asustarse por el texto rojo en la consola. El error siempre te dice en qué línea falló y por qué, ¡solo hay que leerlo!

**Términos relacionados:** [`try/except/finally`](#tryexceptfinally)


### `assert`

**¿Qué es?**
Una instrucción para afirmar que una condición debe ser verdadera. Si es falsa, el programa lanza un error de tipo `AssertionError` y se detiene.

**¿Para qué se usa?**
Principalmente para hacer chequeos internos o pruebas de que el código funciona como se espera (sanity checks). No se recomienda para manejar errores de usuarios.

**Ejemplo:**
```python
def aplicar_descuento(precio, descuento):
    assert 0 <= descuento <= 1, "El descuento debe estar entre 0 y 1"
    return precio * (1 - descuento)
```

**Errores comunes de principiante:**
- Usar `assert` para validar la entrada del usuario en producción; los asserts pueden ser desactivados (usando `python -O`), por lo que esa validación se perdería.

**Términos relacionados:** [`raise`](#raise)

