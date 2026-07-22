# Reto 08: La Ficha del Héroe 🦸

Vas a crear y administrar la ficha de un superhéroe usando un diccionario.

## Instrucciones

Crea tu archivo en `solucion/` con el nombre `tu-usuario-08.py` y sigue los pasos:

1. Crea un diccionario llamado `heroe` con las siguientes claves y valores:
   - `"nombre"`: el nombre de tu héroe (texto).
   - `"poder"`: su superpoder (texto).
   - `"energia"`: `80` (número entero).
   - `"derrotado"`: `False` (booleano).
2. Imprime el diccionario completo.
3. Imprime solo el valor de `"nombre"` usando su clave.
4. El héroe usa su poder y pierde 30 de energía. Modifica la clave `"energia"` restándole `30` (usa el operador `-` del Nivel 04).
5. Imprime el nuevo valor de `"energia"`.
6. Añade una nueva clave `"ciudad"` con la ciudad que protege tu héroe.
7. Usa un `if` para revisar si la `"energia"` del héroe es menor a `60`. Si sí: imprime `"El héroe necesita descansar."`; si no: imprime `"El héroe puede seguir luchando."`.
8. Imprime el diccionario final completo.

**Resultado esperado en tu terminal:**
```text
--- Ficha del Héroe ---
{'nombre': 'Vulcano', 'poder': 'Control del fuego', 'energia': 80, 'derrotado': False}
--- Nombre ---
Vulcano
--- Energía tras usar el poder ---
50
--- Estado del héroe ---
El héroe necesita descansar.
--- Ficha Final ---
{'nombre': 'Vulcano', 'poder': 'Control del fuego', 'energia': 50, 'derrotado': False, 'ciudad': 'Guadalajara'}
```

Ejecuta desde la raíz del proyecto:
- **macOS / Linux:** `python3 python/Modulo-02-Estructuras/03-diccionarios/solucion/tu-usuario-08.py`
- **Windows:** `python python/Modulo-02-Estructuras/03-diccionarios/solucion/tu-usuario-08.py`
