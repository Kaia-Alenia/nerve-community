# Reto Final: Módulo 02 — Estructuras 🏆

Llegaste al final del Módulo 02. Este reto integra **todo** lo aprendido: listas, tuplas, diccionarios, `for` y `while`.

No hay instrucciones paso a paso. Solo el enunciado y el resultado esperado. Tú decides el camino.

---

## El Problema: Sistema de Inventario de una Nave Espacial 🚀

Eres el programador de una nave espacial. Tu misión es gestionar el inventario de suministros, analizar los datos y emitir un reporte de estado.

### Datos iniciales (define estos valores al inicio de tu archivo):

- Una **tupla** llamada `nombre_nave` con dos elementos: el nombre `"Apolo-7"` y el año de lanzamiento `2031`. (Los datos de identidad de la nave nunca cambian.)
- Una **lista** llamada `suministros` con los siguientes 4 elementos de texto: `"Agua"`, `"Comida"`, `"Oxígeno"`, `"Combustible"`.
- Un **diccionario** llamado `estado_nave` con las siguientes claves:
  - `"escudos"`: `100` (entero)
  - `"tripulantes"`: `6` (entero)
  - `"en_orbita"`: `True` (booleano)

### Lógica que debes programar:

1. **Sección Identidad**: Imprime el nombre de la nave (índice `0` de la tupla) y el año de lanzamiento (índice `1`).

2. **Sección Inventario**: Usa un bucle `for` para imprimir cada elemento de la lista `suministros`.

3. **Sección Baja de suministro**: La nave consume `"Combustible"`. Elimínalo de la lista con `.pop()` usando el índice `3`. Luego imprime la lista actualizada.

4. **Sección Estado**: Imprime los valores de `"escudos"` y `"tripulantes"` del diccionario.

5. **Sección Daño**: La nave recibió impactos. Usa un bucle `while` que reste `30` a `"escudos"` mientras `estado_nave["escudos"]` sea **mayor que** `0`. En cada vuelta imprime el valor actual de escudos (si es mayor a 0) o `"Escudos destruidos."` si llega a 0 o menos.

6. **Sección Veredicto**: Usa un `if` sobre el valor final de `estado_nave["escudos"]`:
   - Si los escudos son menores a `0`: imprime `"La nave ha sido destruida."`.
   - Si son exactamente `0`: imprime `"La nave sobrevivió por los pelos."`.
   - Si son mayores a `0`: imprime `"La nave está operativa."`.

---

## Resultado esperado en tu terminal

```text
--- Identidad de la Nave ---
Apolo-7
2031
--- Inventario Actual ---
Agua
Comida
Oxígeno
Combustible
--- Inventario tras consumir Combustible ---
['Agua', 'Comida', 'Oxígeno']
--- Estado de la Nave ---
100
6
--- Impactos recibidos ---
70
40
10
Escudos destruidos.
--- Veredicto ---
La nave ha sido destruida.
```

---

## Criterios de éxito ✓

- [ ] El código corre sin ningún error.
- [ ] Usaste una tupla para la identidad de la nave.
- [ ] Usaste una lista para los suministros y la modificaste con `.pop()`.
- [ ] Usaste un diccionario para el estado de la nave.
- [ ] Usaste `for` para recorrer la lista de suministros.
- [ ] Usaste `while` para simular los impactos.
- [ ] El veredicto final coincide con el resultado del bucle `while`.

Crea tu archivo en `solucion/` con el nombre `tu-usuario-final.py`.

Ejecuta desde la raíz del proyecto:
- **macOS / Linux:** `python3 python/Modulo-02-Estructuras/RETO-FINAL-MOD-2/solucion/tu-usuario-final.py`
- **Windows:** `python python/Modulo-02-Estructuras/RETO-FINAL-MOD-2/solucion/tu-usuario-final.py`

¡Si logras esto, dominas las estructuras de datos de Python. El Módulo 03 te espera!
