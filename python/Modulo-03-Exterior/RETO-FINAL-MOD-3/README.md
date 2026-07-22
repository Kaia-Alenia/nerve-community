# Reto Final: Módulo 03 — El Exterior 🏆

Has aprendido a crear funciones, escuchar al usuario, sobrevivir a errores y persistir datos en archivos. Este reto los combina todos en un sistema real.

Sin instrucciones paso a paso. Solo el enunciado y el resultado esperado.

---

## El Problema: Sistema de Registro de Puntuaciones 🎮

Eres el programador de una arcade. Debes crear un sistema que registre las puntuaciones de los jugadores en un archivo, las cargue y muestre las mejores.

### Funciones que debes definir:

1. **`registrar_puntuacion(nombre_archivo, jugador, puntos)`**: Abre el archivo en modo añadir (`"a"`) y escribe una línea con el formato `jugador:puntos\n` (por ejemplo: `"Ana:1500\n"`).

2. **`cargar_puntuaciones(nombre_archivo)`**: Intenta abrir el archivo en modo lectura. Si no existe (`FileNotFoundError`), devuelve una lista vacía `[]`. Si existe, lee línea por línea y para cada línea:
   - Usa el método `.strip()` para eliminar el `\n` del final (es la primera vez que lo ves: `.strip()` sobre un texto elimina espacios y saltos de línea de los extremos).
   - Separa el nombre y los puntos usando `.split(":")` (también nuevo: `.split(":")` parte el texto en una lista usando `:` como separador; `"Ana:1500".split(":")` devuelve `["Ana", "1500"]`).
   - Convierte los puntos a `int`.
   - Añade un diccionario `{"nombre": nombre, "puntos": puntos}` a una lista.
   - Devuelve esa lista al final.

3. **`mostrar_ranking(lista_puntuaciones)`**: Recibe la lista de diccionarios. Usa un bucle `for` con un `if` para imprimir solo los jugadores con más de `1000` puntos. Imprímelos con su nombre y puntuación.

### Lógica principal (fuera de las funciones):

1. Registra 3 jugadores en `"puntuaciones.txt"` usando `registrar_puntuacion()`:
   - `"Kaia"`, `1800`
   - `"Bruno"`, `750`
   - `"Carla"`, `2100`

2. Carga las puntuaciones con `cargar_puntuaciones()` y guárdalas en una variable.

3. Imprime el número total de jugadores registrados usando `len()`.

4. Llama a `mostrar_ranking()` con la lista cargada.

---

## Resultado esperado en tu terminal

```text
--- Registrando jugadores ---
3 jugadores registrados.
--- Total de registros ---
3
--- Ranking (más de 1000 puntos) ---
Kaia
1800
Carla
2100
```

---

## Criterios de éxito ✓

- [ ] El código corre sin errores.
- [ ] Se crea el archivo `puntuaciones.txt` con las 3 entradas.
- [ ] `cargar_puntuaciones` devuelve una lista de diccionarios (no texto plano).
- [ ] `mostrar_ranking` filtra correctamente (Bruno con 750 NO aparece).
- [ ] Usaste `try / except` para el caso de archivo inexistente.

Crea tu archivo en `solucion/` con el nombre `tu-usuario-final.py`.

Ejecuta desde la raíz del proyecto:
- **macOS / Linux:** `python3 python/Modulo-03-Exterior/RETO-FINAL-MOD-3/solucion/tu-usuario-final.py`
- **Windows:** `python python/Modulo-03-Exterior/RETO-FINAL-MOD-3/solucion/tu-usuario-final.py`

¡Si logras esto, estás listo para el Módulo 04 — Nerve (el módulo del proyecto real)!
