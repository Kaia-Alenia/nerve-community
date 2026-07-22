# Reto 11: La Calculadora de Estadísticas 📊

Vas a crear un conjunto de funciones que calculen estadísticas básicas de una lista de números.

## Instrucciones

Crea tu archivo en `solucion/` con el nombre `tu-usuario-11.py` y sigue los pasos:

1. Define una función llamada `mostrar_titulo` sin parámetros que imprima una línea decorativa con el texto `"=== Calculadora de Estadísticas ==="`.

2. Define una función llamada `obtener_maximo` que reciba una **lista** como parámetro. Dentro, usa un bucle `for` y una variable auxiliar `maximo` (inicialízala con el primer elemento de la lista, `lista[0]`) para encontrar el número más grande: en cada vuelta del `for`, si el elemento actual es mayor que `maximo`, actualiza `maximo`. Al final, usa `return` para devolver `maximo`.

3. Define una función llamada `calcular_total` que reciba una **lista** como parámetro. Usa un bucle `for` y una variable `total = 0` para sumar todos los elementos. Devuelve `total` con `return`.

4. Al final del archivo (fuera de las funciones), define una lista `puntuaciones = [45, 82, 17, 96, 63, 51]`.

5. Llama a `mostrar_titulo()`.
6. Llama a `obtener_maximo(puntuaciones)`, guarda el resultado en `puntaje_maximo` e imprímelo.
7. Llama a `calcular_total(puntuaciones)`, guarda el resultado en `suma_total` e imprímelo.

**Resultado esperado en tu terminal:**
```text
--- Iniciando calculadora ---
=== Calculadora de Estadísticas ===
--- Puntuación máxima ---
96
--- Suma total ---
354
```

Ejecuta desde la raíz del proyecto:
- **macOS / Linux:** `python3 python/Modulo-03-Exterior/01-funciones/solucion/tu-usuario-11.py`
- **Windows:** `python python/Modulo-03-Exterior/01-funciones/solucion/tu-usuario-11.py`
