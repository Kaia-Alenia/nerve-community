from Inventario import Invetario
from Productos import Producto

mi_inventario = Invetario()

p1 = Producto("Test", 10, 5)
p2 = Producto("Mouse", 25.0, 10)

mi_inventario.agregar_producto(p1)
mi_inventario.agregar_producto(p2)

mi_inventario.mostrar_inventario()

mi_inventario.actualizar_producto("Test", 10, 4)

mi_inventario.mostrar_inventario()

mi_inventario.eliminar_producto("Test")

mi_inventario.mostrar_inventario()
