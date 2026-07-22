# Teoría: Variables (Cajas con etiquetas)

Imagina que estás organizando una mudanza. Para no perder tus cosas, las guardas en **cajas de cartón** y a cada caja le pones una **etiqueta** con un marcador para saber qué hay dentro.

En programación, una **variable** es exactamente eso: una "caja" en la memoria de la computadora donde guardamos un dato, a la cual le ponemos una "etiqueta" (un nombre) para poder usar ese dato más tarde.

## Anatomía de una variable y el símbolo `=`

Para crear nuestra caja en Python, la sintaxis (la regla) es así:

```python
nombre = "Kaia"
```

**Desmontaje de los símbolos:**

1. `nombre`: Es la etiqueta de tu caja.
2. `=`: **¡ATENCIÓN AQUÍ!** En matemáticas, el símbolo `=` significa "igualdad". Pero en programación, **significa ASIGNACIÓN (guardado)**. Léelo como: *"Agarra lo que está a la derecha (`"Kaia"`) y guárdalo dentro de la caja que está a la izquierda (`nombre`)"*.
3. `"Kaia"`: Es el texto que quieres guardar. 

Para ver lo que hay dentro de la caja, usamos nuestro comando estrella:

```python
print(nombre)
```
*Ojo: Cuando imprimimos una variable, NUNCA usamos comillas alrededor del nombre de la caja. Si pusieras `print("nombre")`, Python imprimiría literalmente la palabra "nombre" en lugar de ver qué hay dentro de la caja.*

## Reglas para etiquetar tus cajas

Python es muy ordenado y tiene reglas estrictas para nombrar cajas:
1. **Sin espacios:** No puedes llamar a tu caja `mi nombre`. Usa guiones bajos: `mi_nombre`.
2. **Sin números al inicio:** `1caja` es ilegal. `caja1` es correcto.

## ¿Qué pasa si me equivoco?

El error de "bebé" más común es pedirle a Python que abra una caja que aún no existe, o escribir mal la etiqueta. 
Si guardas un dato en `usuario` pero luego escribes `print(usuari)`, Python entrará en pánico y te mostrará un `NameError` (Error de Nombre). Si ves este error, respira y revisa tu ortografía: la computadora no adivina, obedece exactamente lo que escribes.
