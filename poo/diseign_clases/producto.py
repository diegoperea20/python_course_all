class Producto:
    contador_productos = 0

    def __init__(self, nombre, precio):
        Producto.contador_productos += 1
        self._id_producto = Producto.contador_productos
        self._nombre = nombre
        self._precio = precio
    
    @property
    def precio(self):
        return self._precio

    def __str__(self):
        return f"ID producto: {self._id_producto}, Nombre: {self._nombre} , Precio: {self._precio}"


""" producto1=Producto('hola',2)
print(producto1)
producto2=Producto('hoa',5)
print(producto2)  """
