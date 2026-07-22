# Reto 09: El Marcador de Goles ⚽

Vas a procesar los goles de un torneo usando bucles y condicionales.

## Instrucciones

Crea tu archivo en `solucion/` con el nombre `tu-usuario-09.py` y sigue los pasos:

1. Crea una lista llamada `goles_por_partido` con los siguientes 6 valores enteros: `[2, 0, 5, 1, 3, 0]`. Cada número representa los goles marcados en un partido.
2. Usa un bucle `for` para imprimir cada número de la lista, uno por línea.
3. Fuera del bucle anterior, usa `range()` para imprimir los números del `1` al `6` (simulando el número de partido).
4. Crea una variable `partidos_ganados` con valor `0` (entero). Luego usa un `for` con un `if` dentro para recorrer `goles_por_partido`: si los goles de ese partido son mayores a `1`, súmale `1` a `partidos_ganados` (usa `partidos_ganados = partidos_ganados + 1`). Al terminar el bucle, imprime `partidos_ganados`.
5. Usa un `if` para revisar si `partidos_ganados` es mayor o igual a `3`. Si sí: imprime `"Clasificado a la siguiente ronda"`; si no: `"Eliminado del torneo"`.

**Resultado esperado en tu terminal:**
```text
--- Goles por partido ---
2
0
5
1
3
0
--- Número de partidos ---
1
2
3
4
5
6
--- Partidos ganados (más de 1 gol) ---
3
--- Resultado del torneo ---
Clasificado a la siguiente ronda
```

Ejecuta desde la raíz del proyecto:
- **macOS / Linux:** `python3 python/Modulo-02-Estructuras/04-bucle-for/solucion/tu-usuario-09.py`
- **Windows:** `python python/Modulo-02-Estructuras/04-bucle-for/solucion/tu-usuario-09.py`
