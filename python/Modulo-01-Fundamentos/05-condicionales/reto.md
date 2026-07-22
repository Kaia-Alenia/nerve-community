# Reto 05: El Semáforo del Programador 🚦

Vas a simular la lógica de un semáforo inteligente que evalúa la velocidad de un vehículo y decide qué hacer.

## Instrucciones

Dentro de la carpeta `solucion/` que está en `05-condicionales/`, crea tu archivo con el formato `tu-usuario-05.py` (por ejemplo, `kaia-05.py`). Luego sigue los pasos:

1. Crea una variable `velocidad_actual` y asígnale el valor `85` (un número entero que representa km/h).
2. Crea una variable `limite_velocidad` y asígnale el valor `80`.
3. Escribe una cadena de `if / elif / else` con la siguiente lógica:
   - **SI** `velocidad_actual` es menor a `60`: imprime `"Velocidad baja. Puedes acelerar."`
   - **SI NO, SI** `velocidad_actual` es menor o igual a `limite_velocidad`: imprime `"Velocidad correcta. Bien manejado."`
   - **SI NO** (cualquier otro caso, es decir, si va por encima del límite): imprime `"¡EXCESO DE VELOCIDAD! Reduce la marcha."`
4. Después del bloque `if/elif/else`, crea una variable llamada `excede_limite` que guarde el resultado de preguntar si `velocidad_actual > limite_velocidad`.
5. Imprime el valor de `excede_limite`.

**Resultado esperado en tu terminal** (con `velocidad_actual = 85`):
```text
--- Evaluación de Velocidad ---
¡EXCESO DE VELOCIDAD! Reduce la marcha.
--- ¿Excede el límite? ---
True
```

**Prueba adicional (opcional):** Cambia el valor de `velocidad_actual` a `55` y vuelve a ejecutar. Deberías ver:
```text
--- Evaluación de Velocidad ---
Velocidad baja. Puedes acelerar.
--- ¿Excede el límite? ---
False
```

Ejecuta desde la raíz del proyecto:
- **macOS / Linux:** `python3 python/Modulo-01-Fundamentos/05-condicionales/solucion/tu-usuario-05.py`
- **Windows:** `python python/Modulo-01-Fundamentos/05-condicionales/solucion/tu-usuario-05.py`

Si tu semáforo funciona correctamente para ambas pruebas, ¡estás listo para el Reto Final del Módulo!
