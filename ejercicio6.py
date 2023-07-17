class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def actualizar_cantidad(self, nombre_producto, cantidad):
        for producto in self.productos:
            if producto.nombre == nombre_producto:
                producto.cantidad += cantidad

class Venta:
    def __init__(self):
        self.productos_vendidos = []

    def agregar_producto_vendido(self, producto):
        self.productos_vendidos.append(producto)

    def actualizar_cantidad(self, nombre_producto, cantidad):
        for producto in self.productos_vendidos:
            if producto.nombre == nombre_producto:
                producto.cantidad += cantidad

inventario = Inventario()
venta = Venta()

producto1 = Producto("Producto 1", 10.0, 100)
producto2 = Producto("Producto 2", 20.0, 200)

inventario.agregar_producto(producto1)
inventario.agregar_producto(producto2)

venta.agregar_producto_vendido(producto1)
venta.actualizar_cantidad("Producto 1", -10)

print("Inventario:")
for producto in inventario.productos:
    print(f"{producto.nombre}: {producto.cantidad}")

print("Ventas:")
for producto in venta.productos_vendidos:
    print(f"{producto.nombre}: {producto.cantidad}")

producto3 = Producto("Producto 3", 30.0, 300)
inventario.agregar_producto(producto3)

producto_vendido = Producto("Producto 1", 10.0, 10)
venta.agregar_producto_vendido(producto_vendido)
inventario.actualizar_cantidad("Producto 1", -10)
