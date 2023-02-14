from dominio.pelicula import *
from servicio.catalogo_peliculas import CatalogoPeliculas as cp


opcion=None
while opcion != 4:
    try:
        print('Opciones:')
        print('1. Agrear Pelicula')
        print('2. Listar Pelicula')
        print('3. Eliminar Pelicula')
        print('4.  Salir')
        opcion=int(input('Escribe tu opcion (1-4): '))

        if opcion ==1:
            nombre_pelicula=input('Proporciona nombre pelicula: ')
            pelicula=Pelicula(nombre_pelicula)
            cp.agregar_pelicula(pelicula)
        elif opcion == 2:
            cp.listar_peliculas()
        elif opcion ==3:
            cp.eliminar_peliculas()
            
    except Exception as e:
        print(f'Ocurrio un error: {e}')
        opcion=None
else: 
    print('salimos del programa...')