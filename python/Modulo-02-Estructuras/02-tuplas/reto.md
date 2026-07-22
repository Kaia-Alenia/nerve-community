# Reto 07: El Sistema de Coordenadas 🗺️

Vas a modelar la información de una tienda usando la estructura de datos correcta en cada caso.

## Instrucciones

Crea tu archivo en `solucion/` con el nombre `tu-usuario-07.py` y sigue los pasos:

1. Crea una **tupla** llamada `coordenadas_tienda` con dos números enteros que representen latitud y longitud (usa `19` y `-99` como valores de ejemplo). Las coordenadas de una tienda nunca cambian.
2. Crea una **lista** llamada `productos_disponibles` con 3 productos de texto (los que quieras). El inventario sí puede cambiar.
3. Imprime la tupla de coordenadas.
4. Imprime la lista de productos.
5. La tienda recibe un nuevo producto: añádelo a `productos_disponibles` con `.append()`.
6. Imprime el número total de productos con `len()`.
7. Imprime el primer producto de la lista (índice `0`).
8. Usa un `if` para preguntar si el total de productos (resultado de `len()`) es mayor a `3`. Si sí, imprime `"Inventario amplio"`; si no, imprime `"Inventario básico"`.

**Resultado esperado en tu terminal:**
```text
--- Coordenadas de la Tienda ---
(19, -99)
--- Productos Disponibles ---
['Manzanas', 'Pan', 'Leche']
--- Nuevo producto añadido. Total: ---
4
--- Primer producto ---
Manzanas
--- Estado del inventario ---
Inventario amplio
```

Ejecuta desde la raíz del proyecto:
- **macOS / Linux:** `python3 python/Modulo-02-Estructuras/02-tuplas/solucion/tu-usuario-07.py`
- **Windows:** `python python/Modulo-02-Estructuras/02-tuplas/solucion/tu-usuario-07.py`
