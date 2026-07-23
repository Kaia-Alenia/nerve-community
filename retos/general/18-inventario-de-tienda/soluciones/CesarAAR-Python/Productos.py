# Clase Producto
# Validaciones:
"""
Nombre:
- El campo no debe estar vacio.
- Minimo de caracteres: 3

Precio:
- El campo no debe de estar vacio.
- Precio mayor o igual a 0.

Cantidad:
- El campo no debe de estar vacio.
- La cantidad debe de ser >= 0.
"""

# NOTA:
"""
No se agregó el deleter porque no le vi la logica de agregarlo.
Bajo la logica de un negocio, el dueño no elimina el nombre|precio|cantidad, si va a eliminar algo es el producto completo,
o si es el caso, solo actualizaría.
"""


class Producto:
    def __init__(self, nombre: str, precio: float, cantidad: int):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, new_nombre):
        if new_nombre.strip():
            if len(new_nombre) >= 3:
                self.__nombre = new_nombre
            else:
                raise ValueError("Nombre debe de tener al menos 3 caracteres.")
        else:
            raise ValueError("Campo NOMBRE vacío")

    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def precio(self, new_precio):
        if new_precio is None:

            raise ValueError("Campo Precio vacío")
        if new_precio < 0:
            raise ValueError("Precio debe de ser mayor o igual a 0")

        self.__precio = new_precio

    @property
    def cantidad(self):
        return self.__cantidad

    @cantidad.setter
    def cantidad(self, new_cantidad):
        if new_cantidad is None:
            raise ValueError("Campo Cantidad vacío")

        if new_cantidad < 0:
            raise ValueError("Cantidad debe de ser mayor o igual a 0.")

        self.__cantidad = new_cantidad

    def mostrar_producto(self):
        print(
            f"Nombre: {self.nombre}\nPrecio: {self.precio}\nCantidad Actual: {self.cantidad}"
        )
