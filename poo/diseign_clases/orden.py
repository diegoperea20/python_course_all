from producto import *


class Orden:
    contador_ordenes = 0

    def __init__(self,productos):
        Orden.contador_ordenes += 1
        self._id_orden=Orden.contador_ordenes
        self._productos=list(productos)

    def agregar_productos(self,producto):
        self._productos.append(producto)

    def calcular_total(self):
        total=0
        for producto in self._productos:
            total += producto.precio
        return total
    
    def __str__(self):
        productos_str=''
        for producto in self._productos:
            productos_str += producto.__str__() + '\n'
        return f'Orden: {self._id_orden}, \nProductos:\n{productos_str}'


""" producto1=Producto('camisa',2)
producto2=Producto('media',5)
productos1=[producto1,producto2]
orden1=Orden(productos1)
print(orden1) """