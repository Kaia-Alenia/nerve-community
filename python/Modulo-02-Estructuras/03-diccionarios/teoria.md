# Teoría: Diccionarios — El fichero de datos etiquetado

Imagina la ficha de un paciente en un hospital: tiene campos etiquetados como "Nombre:", "Edad:", "Tipo de sangre:". Para saber la edad, buscas la etiqueta "Edad", no tienes que contar cuál es el tercer renglón.

En Python, un **Diccionario** funciona igual: cada dato tiene una **clave** (la etiqueta) y un **valor** (el dato).

---

## Anatomía de un Diccionario

Usamos **llaves** `{ }` para crear un diccionario:

```python
usuario = {
    "nombre": "Kaia",
    "edad": 25,
    "activo": True
}
```

Desglose de cada símbolo:

- `usuario`: El nombre de la variable.
- `=`: Asignación/guardado.
- `{`: Abre el diccionario.
- `"nombre"`: La **clave** (siempre texto, entre comillas).
- `:`: El símbolo que **separa** la clave de su valor. Léelo como "tiene el valor de...".
- `"Kaia"`: El **valor** asociado a la clave `"nombre"`. Puede ser cualquier tipo de dato (`str`, `int`, `bool`, etc.).
- `,`: Separa un par clave-valor del siguiente.
- `}`: Cierra el diccionario.

---

## Acceder a un valor: usar la clave entre corchetes

Para obtener un valor, en lugar de un índice numérico, usamos el nombre de la clave entre corchetes `[ ]`:

```python
nombre_del_usuario = usuario["nombre"]   # "Kaia"
edad_del_usuario   = usuario["edad"]     # 25
```

---

## Modificar un valor existente

La sintaxis es la misma que para asignar a una variable, pero apuntando a la clave:

```python
usuario["edad"] = 26
# El diccionario ahora tiene "edad": 26
```

---

## Añadir una clave nueva

Si usas una clave que no existía, Python la crea automáticamente:

```python
usuario["email"] = "kaia@ejemplo.com"
# El diccionario ahora tiene una nueva clave "email"
```

---

## Eliminar una clave: `.pop()`

```python
usuario.pop("activo")
# La clave "activo" y su valor desaparecen del diccionario.
```

---

## ¿Qué pasa si me equivoco?

- **Clave que no existe**: Si pides `usuario["telefono"]` y esa clave no existe, Python lanzará un `KeyError`. Siempre asegúrate de que la clave exista antes de pedirla.
- **Olvidar los dos puntos `:`**: `"nombre" "Kaia"` sin los dos puntos causará `SyntaxError`.
- **Claves duplicadas**: Si escribes la misma clave dos veces, Python solo guarda la última. `{"color": "rojo", "color": "azul"}` resultará en `{"color": "azul"}`. Cada clave debe ser única.
