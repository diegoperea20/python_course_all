# UTILIZAR WITH NO HAY NECESIDAD DE INDICAR EL CIERRE DEL ACHIVO , ESTE LO HACE AUTOMATICO

#-------abre y cierra normal----------------
""" with open('C:/Users/User/Desktop/curso_python_all/manejo_archivos/prueba.txt','r') as archivo:
    print(archivo.read()) """

#----------con manejo de clase cuando se abra y se cierre el archivo se usan en bases de datos--------
class Manejoarchivos:
    def __init__(self, nombre):
        self.nombre = nombre

    def __enter__(self):#se abre 
        print('obtenemos el recurso'.center(50,'-'))
        self.nombre=open(self.nombre,'r')
        return self.nombre
    
    def __exit__(self,tipo_excepcion,valor_excepcion,traza_error): #se cierra
        print('cerramos el recurso'.center(50,'-'))
        if self.nombre:
            self.nombre.close()


with Manejoarchivos('C:/Users/User/Desktop/curso_python_all/manejo_archivos/prueba.txt') as archivo:
    print(archivo.read())


