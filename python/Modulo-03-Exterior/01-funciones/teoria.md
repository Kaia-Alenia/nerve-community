# Teoría: Funciones — La receta de cocina reutilizable

Imagina que eres chef y tienes una receta de guacamole. En lugar de escribir todos los pasos cada vez que alguien pide guacamole, tienes la receta en una tarjeta. Cuando la necesitas, la sacas, la sigues, y listo. La receta es tu **función**.

---

## Anatomía: Definir una función

Para crear una función, usamos la palabra reservada `def`:

```python
def saludar():
    print("¡Hola! Bienvenido.")
```

Desglose de cada pieza:

- **`def`**: Palabra reservada. Significa "define". Le dice a Python "estoy creando una función".
- **`saludar`**: El nombre que le damos a nuestra función. Las mismas reglas que las variables: sin espacios, sin números al inicio.
- **`()`**: Los paréntesis son **obligatorios** al definir una función. Por ahora estarán vacíos; más adelante tendrán datos adentro.
- **`:`**: Los dos puntos de siempre. Indican que el bloque de código comienza.
- **`    print(...)`**: El código **dentro** de la función, indentado con 4 espacios.

> **Importante:** Definir una función NO la ejecuta. Es como escribir la receta sin cocinar nada aún. Solo la guarda para usarla después.

---

## Anatomía: Llamar (ejecutar) una función

Para ejecutar la función, la **llamamos** escribiendo su nombre seguido de paréntesis:

```python
saludar()
```

- **`saludar`**: El nombre de la función que queremos ejecutar.
- **`()`**: Los paréntesis le dicen a Python "ejecuta esto ahora". Sin paréntesis, Python solo mira la función, no la corre.

---

## Funciones con parámetros: recetas con ingredientes

Una función puede recibir **datos** para trabajar con ellos. Esos datos se llaman **parámetros** y se ponen dentro de los paréntesis al definir la función:

```python
def saludar_a(nombre):
    print("¡Hola,")
    print(nombre)
```

- **`nombre`**: Es el parámetro. Es como una variable temporal que solo existe dentro de la función. Cuando llamas a la función, le pasas el valor real.

Para llamar esta función y darle el dato:

```python
saludar_a("Kaia")
saludar_a("Bruno")
```

Cada llamada es independiente. La primera vez `nombre` vale `"Kaia"`, la segunda vez vale `"Bruno"`.

---

## Funciones que devuelven un resultado: `return`

Una función también puede **calcular algo y devolverte el resultado** para que lo uses:

```python
def sumar(numero_a, numero_b):
    resultado = numero_a + numero_b
    return resultado
```

- **`return`**: Palabra reservada. Significa "devuelve este valor a quien me llamó". Cuando Python llega al `return`, la función termina y entrega el valor.

Para capturar lo que devuelve:

```python
total = sumar(10, 5)
print(total)   # Imprime 15
```

---

## ¿Qué pasa si me equivoco?

- **Olvidar los paréntesis al llamar**: Si escribes `saludar` sin `()`, Python no la ejecuta. Solo muestra que es un objeto función, no corre su código.
- **Usar una variable de dentro de la función desde afuera**: Las variables creadas dentro de una función solo existen dentro de ella. Si intentas usarlas afuera, obtendrás un `NameError`.
- **Llamar la función antes de definirla**: Python lee el código de arriba a abajo. Si llamas `saludar()` en la línea 1 y la defines en la línea 10, obtendrás un `NameError`. Define siempre primero, llama después.
