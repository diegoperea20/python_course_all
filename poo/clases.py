class Persona:
    variable_clase='comparte info a todas las clases' #no hay necesidad de crear un objeto para acceder a esta variable

    def __init__(self, nombre, apellidoi, edad):  # constructor y parametros
        self.nombre = nombre  # self.atributo=parametro
        self.apellido = apellidoi
        self.edad = edad

    def mostrar_detalle(self):#metodo instancia
        print(f"Persona metodo: {self.nombre} ,{self.apellido} ,{self.edad}")
        # dentro de las clases podemos utilizar self

    @staticmethod #metodo estatico no pueden acceder atibuto y meodos de instancia a self
                    #NO SE RELACIONA CON LA CLASE , ESTO SIRVE EJ PARA HACER CALCULOS    
    def metodo_estatico():
        print(Persona.variable_clase)



    @classmethod #Accede a variables de clase y metodos de clase
    def metodo_clase(cls):
        print(cls.variable_clase)

persona1 = Persona("juan", "perez", 30)  # Un objeto

# imprimir de forma normal
print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad)

# modificacion de parametro
persona1.nombre = "juan carlos"
print(f"objeto persona 1:{persona1.nombre} ,{persona1.apellido} ,{persona1.edad}")

persona2 = Persona("haweon", "kim", 32)
print(f"objeto persona 2: nombre: {persona2.nombre} , apellido : {persona2.apellido} ,edad: {persona2.edad}")

# llamada de metodo
persona2.mostrar_detalle()  # forma 1

#agregar nuevo atributo exclusivo de persona 2
persona2.telefono='54'
print(f'nuevo atributo:{persona2.telefono}')

""" Persona.mostrar_detalle(persona2) """  # forma 2 no comun 

#variable de la clase compartida
print(persona2.variable_clase)


#Persona.metodo_estatico()