from producto import Producto
from orden import Orden


producto1=Producto('camisa',2)
producto2=Producto('media',5)
producto3=Producto('mouse',6)
producto4=Producto('vestido',8)


productos1=[producto1,producto2]
productos2=[producto3,producto4]
 
orden1=Orden(productos1)
#AGREGAR producto
orden1.agregar_productos(producto3)
orden1.agregar_productos(producto4)
print(orden1)
print(f'TOTAL: {orden1.calcular_total()}')

orden2=Orden(productos2)
print(orden2)
print(f'TOTAL: {orden2.calcular_total()}')