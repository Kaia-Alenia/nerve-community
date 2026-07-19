# 🐍 08 - POO básica

### `class`

**¿Qué es?**
La palabra clave para definir una Clase. Una clase es como un 'molde' o 'plano' para crear objetos en la Programación Orientada a Objetos (POO).

**¿Para qué se usa?**
Para agrupar variables (atributos) y funciones (métodos) que pertenecen a un mismo concepto.

**Ejemplo:**
```python
class Perro:
    pass

mi_perro = Perro()
```

**Errores comunes de principiante:**
- Escribir el nombre de la clase en minúsculas (la convención en Python es usar PascalCase, como `MiClaseGenial`).

**Términos relacionados:** [`__init__`](#__init__)

### `__init__`

**¿Qué es?**
El método constructor. Es la función especial que se ejecuta automáticamente cuando creas un objeto nuevo a partir de una clase.

**¿Para qué se usa?**
Para configurar los valores iniciales (atributos) del objeto.

**Ejemplo:**
```python
class Perro:
    def __init__(self, nombre):
        self.nombre = nombre
```

**Errores comunes de principiante:**
- Escribir `_init_` (con un solo guion bajo) en lugar de `__init__` (con dos a cada lado), lo que hace que Python lo ignore.

**Términos relacionados:** [`class`](#class), [`self`](#self)

### `self`

**¿Qué es?**
Una referencia al objeto mismo que está ejecutando la función. Se debe poner como primer parámetro de todos los métodos dentro de una clase.

**¿Para qué se usa?**
Para que la clase sepa qué objeto específico debe modificar. (Ej: 'modifica MI nombre, no el del otro perro').

**Ejemplo:**
```python
class Perro:
    def ladrar(self):
        print(f"{self.nombre} dice guau!")
```

**Errores comunes de principiante:**
- Olvidar poner `self` en los parámetros de un método. Al llamarlo fallará diciendo que se pasaron 1 argumentos pero la función pide 0.

**Términos relacionados:** [`__init__`](#__init__)

### `herencia básica`

**¿Qué es?**
Un concepto de la POO donde una clase 'hija' hereda todo lo que sabe y hace una clase 'padre'.

**¿Para qué se usa?**
Para reutilizar código. Si tienes la clase `Vehículo`, la clase `Coche` puede heredar de ella y no tener que reescribir cosas como `moverse()`.

**Ejemplo:**
```python
class Vehiculo:
    pass

class Coche(Vehiculo):
    pass
```

**Errores comunes de principiante:**
- Crear jerarquías de herencia súper profundas y complejas, lo que hace el código un dolor de cabeza de mantener.

**Términos relacionados:** [`class`](#class)

### `decoradores`

**¿Qué es?**
Una función que envuelve a otra función para modificar o extender su comportamiento sin cambiar su código original. Se usan con un arroba `@`.

**¿Para qué se usa?**
Muy usados en frameworks web (como Flask o FastAPI) para decirle a una función 'solo ejecútate si el usuario está logueado' o 'ejecútate cuando entren a esta URL'.

**Ejemplo:**
```python
# Simulando un decorador
def login_requerido(func):
    return func

@login_requerido
def ver_perfil():
    pass
```

**Errores comunes de principiante:**
- Olvidar qué hace realmente el decorador por debajo, viéndolo como 'magia negra' en lugar de simple código Python.

**Términos relacionados:** [`funciones`](../python/03-funciones.md#def)

