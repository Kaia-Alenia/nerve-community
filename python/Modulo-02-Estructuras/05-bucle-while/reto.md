# Reto 10: El Reactor Nuclear 🔋

Debes programar el sistema de control de un reactor. El reactor tiene combustible y debes gestionar cuántas veces puede operar antes de agotarse.

## Instrucciones

Crea tu archivo en `solucion/` con el nombre `tu-usuario-10.py` y sigue los pasos:

1. Crea una variable `combustible` con el valor `100` (entero).
2. Crea una variable `ciclos_completados` con el valor `0` (entero).
3. Escribe un bucle `while` que se ejecute **mientras** `combustible` sea **mayor que** `0`.
4. Dentro del bucle:
   - Resta `35` al `combustible` en cada ciclo.
   - Suma `1` a `ciclos_completados`.
   - Usa un `if` para revisar si `combustible > 0`. Si sí: imprime el valor actual de `combustible`. Si no: imprime `"Combustible agotado."`.
5. Fuera del bucle, imprime el total de `ciclos_completados`.
6. Usa un `if` para revisar si `ciclos_completados` es mayor o igual a `3`. Si sí: imprime `"El reactor operó de forma estable."`; si no: `"El reactor necesita más combustible."`.

**Resultado esperado en tu terminal:**
```text
--- Estado del Reactor ---
--- Ciclo 1 ---
65
--- Ciclo 2 ---
30
--- Ciclo 3 ---
Combustible agotado.
--- Total de ciclos ---
3
--- Diagnóstico ---
El reactor operó de forma estable.
```

> **Pista:** Para imprimir el número de ciclo dentro del bucle (`--- Ciclo 1 ---`, etc.), necesitas imprimir `ciclos_completados` después de haberle sumado `1`. Esto es perfectamente válido con lo que ya sabes.

Ejecuta desde la raíz del proyecto:
- **macOS / Linux:** `python3 python/Modulo-02-Estructuras/05-bucle-while/solucion/tu-usuario-10.py`
- **Windows:** `python python/Modulo-02-Estructuras/05-bucle-while/solucion/tu-usuario-10.py`
