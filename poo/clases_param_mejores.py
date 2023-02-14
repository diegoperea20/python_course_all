#para importar funciones de archivos es-.  from nombre_archivo import *

class Persona:
    def __init__(self, nombre, apellidoi, edad ,*valores,**terminos):  # constructor y parametros , 
        """los *valores son variables de tubla indifinidos y **terminos son diccionarios indefinidos"""
        self.nombre = nombre  # self.atributo=parametro
        self.apellido = apellidoi
        self.edad = edad
        self.valores=valores
        self.terminos=terminos

    def mostrar_detalle(self):
        print(f"Persona metodo : {self.nombre} ,{self.apellido} ,{self.edad} ,{self.valores}, {self.terminos}")
        # dentro de las clases podemos utilizar self


persona1 = Persona("juan", "perez", 30, '765432',2,3,4,m='manzana',p='pera')  # Un objeto

persona1.mostrar_detalle()

persona2 = Persona("haweon", "kim", 32)
print(f"objeto persona 2: nombre: {persona2.nombre} , apellido : {persona2.apellido} ,edad: {persona2.edad}")

# llamada de metodo
persona2.mostrar_detalle()  # forma 1

#agregar nuevo atributo exclusivo de persona 2
persona2.telefono='54'
print(f'nuevo atributo:{persona2.telefono}')

""" Persona.mostrar_detalle(persona2) """  # forma 2 no comun 
