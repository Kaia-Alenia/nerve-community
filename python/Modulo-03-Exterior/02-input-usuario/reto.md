# Reto 12: La Máquina de Descuentos 🏷️

Vas a crear un programa interactivo que calcule el precio final de un producto con descuento.

## Instrucciones

Crea tu archivo en `solucion/` con el nombre `tu-usuario-12.py` y sigue los pasos:

1. Define una función llamada `calcular_precio_final` que reciba dos parámetros: `precio_original` (número entero) y `porcentaje_descuento` (número entero). Dentro, calcula el descuento (`precio_original * porcentaje_descuento // 100`) y el precio final (`precio_original - descuento`). Devuelve el precio final con `return`.

2. Fuera de la función, usa `input()` para pedirle al usuario:
   - El nombre del producto (texto, sin convertir).
   - El precio original (conviértelo a `int`).
   - El porcentaje de descuento (conviértelo a `int`).

3. Llama a `calcular_precio_final()` con los datos del usuario y guarda el resultado.

4. Usa un `if / elif / else` para evaluar el precio final:
   - Si el precio final es mayor a `500`: imprime `"Producto premium con descuento."`.
   - Si el precio final es mayor a `100`: imprime `"Buen precio."`.
   - Si no: imprime `"¡Oferta increíble!"`.

5. Imprime el resumen completo.

**Resultado esperado en tu terminal** (si el usuario escribe `Teclado`, `800` y `25`):
```text
--- Datos del producto ---
Teclado
--- Precio con 25% de descuento ---
600
--- Clasificación ---
Producto premium con descuento.
```

Ejecuta desde la raíz del proyecto:
- **macOS / Linux:** `python3 python/Modulo-03-Exterior/02-input-usuario/solucion/tu-usuario-12.py`
- **Windows:** `python python/Modulo-03-Exterior/02-input-usuario/solucion/tu-usuario-12.py`
