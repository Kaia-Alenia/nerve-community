# Teoría: Tuplas — La colección con candado

Imagina que grabas un acta notarial: una vez firmada y sellada, nadie puede cambiar ni una coma. Los datos son permanentes e inmutables. Eso es una tupla.

---

## Anatomía de una Tupla

La diferencia visual con la lista es solo un símbolo: en lugar de `[ ]` (corchetes), usamos `( )` (paréntesis):

```python
dias_semana = ("Lunes", "Martes", "Miércoles", "Jueves", "Viernes")
```

Desglose:

- `dias_semana`: El nombre de la variable.
- `=`: Asignación/guardado.
- `(`: Abre la tupla.
- `"Lunes"`, `"Martes"`, ...: Los elementos, separados por `,`.
- `)`: Cierra la tupla.

---

## Acceder a elementos: igual que las listas

Los índices funcionan exactamente igual — Python sigue contando desde cero:

```python
dias_semana = ("Lunes", "Martes", "Miércoles", "Jueves", "Viernes")

primer_dia = dias_semana[0]   # "Lunes"
ultimo_dia = dias_semana[4]   # "Viernes"
total_dias = len(dias_semana) # 5
```

`len()` también funciona con tuplas.

---

## La diferencia fundamental: inmutabilidad

La palabra **inmutable** significa "que no puede ser cambiado". Una vez que creas una tupla, no puedes:

- Añadirle elementos (no existe `.append()` en las tuplas).
- Eliminar elementos (no existe `.pop()` en las tuplas).
- Cambiar el valor de uno de sus elementos.

Si lo intentas, Python lanzará un `TypeError: 'tuple' object does not support item assignment`.

---

## ¿Cuándo usar Lista y cuándo Tupla?

| Pregunta | Usa... |
|---|---|
| ¿Los datos pueden cambiar? (ej. lista de usuarios) | **Lista** `[ ]` |
| ¿Los datos son fijos para siempre? (ej. días de la semana, coordenadas GPS) | **Tupla** `( )` |

La tupla también es más rápida de leer para la computadora porque sabe que nunca cambiará. Es una señal de intención: le dices al equipo "estos datos no deben modificarse".

---

## ¿Qué pasa si me equivoco?

- **Intentar modificar una tupla**: `TypeError`. Si necesitas modificar los datos, es señal de que debiste usar una Lista.
- **Tupla de un solo elemento**: `(42)` no es una tupla, Python lo interpreta como el número `42` entre paréntesis. Para crear una tupla de un solo elemento, debes poner una coma al final: `(42,)`. El `,` es la clave.
