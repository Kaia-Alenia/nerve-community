#Clase Inventario que hereda de Producto
"""
Funciones:
- Ver Lista producto
- Crear Producto
- Ver Producto
- Actualizar Producto
- Eliminar Producto

"""

from Productos import Producto

class Invetario():
    def __init__(self):
        self.__productos = {}

    def agregar_producto(self, producto:Producto):
        if producto.nombre in self.__productos:
            raise ValueError("Ya existe ese producto en el inventario")
        self.__productos[producto.nombre] = producto
        print(f"Producto Insertado -> {producto.nombre} ")

    def buscar_producto(self, nombre):
        producto_b = self.__productos.get(nombre,None)

        if producto_b is None:
            print("Producto no encontrado.")
            return None
        else:
            print(f"Producto buscado: {nombre}")
            producto_b.mostrar_producto()
            return producto_b
    
    def mostrar_inventario(self):
        if not self.__productos:
            print("Inventario Vacio")
            return
        for prod in self.__productos.values():
            print(f"- {prod.nombre}: ${prod.precio} (Stock: {prod.cantidad})")

    def actualizar_producto(self, nombre, new_precio= None, new_cantidad = None):
        producto = self.buscar_producto(nombre)
        if producto == "Producto no encontrado":
            raise KeyError("Producto no encontrado")
        
        if new_precio is not None:
            producto.precio = new_precio
        if new_cantidad is not None:
            producto.cantidad = new_cantidad
        print(f"Producto: {nombre} -> Actualizado")

    def eliminar_producto(self,nombre):
        if nombre in self.__productos:
            del self.__productos[nombre]
            print(f"Producto: {nombre} -> Eliminado")
        else:
            raise KeyError("Producto no Encontrado")