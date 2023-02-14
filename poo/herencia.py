class Persona:
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad
    
    def __str__(self): #sobreescribiento de la clase para que cuando se llame
                       #a la clase no de el numero de memoria si no que muestre info de parametros
                       #esro se veen el archivo cliente_sobreescritura.py
        return f'Persona: {self.nombre}  {self.edad}'
        

class Empleado(Persona):
    def __init__(self,nombre,edad,sueldo): #Poner mismo parametros de clase heredada
       super().__init__(nombre,edad) #para acceder al metodo(constructor) de la clase PERSONA
       self.sueldo=sueldo

    def __str__(self):#sobreescribimiento para acceder a clase empleado 
                  #se pone super para heredar el metodo y en este caso el sobreescribiento str
        return f'{super().__str__() }  sueldo:{self.sueldo}'

empleado1=Empleado('juan',28,5000)
print(empleado1.nombre)
    
