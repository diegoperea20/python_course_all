
#SE ENCAPSULA POR SEGURIDAD Y PARA QUE SOLO LA CLASE ACCEDA A LOS PARAMETOS 
class Persona:
    def __init__(self, nombre, apellidoi, edad):  # constructor y parametros
        self._nombre = nombre  # self._atributo=parametro ENCAPSULANDO
        #self.__nombre=nombre   SE HACE PARA QUE NO SE PUEDA MODIFICAR  
        self.apellido = apellidoi
        self._edad = edad

    @property  # METODO GET  obtener/recuperar
    def nombre(self):
        return self._nombre

    @nombre.setter  # METODO SET  colocar/modificar
    def nombre(self, nombre):
        self._nombre = nombre

    @property  # METODO GET  obtener/recuperar
    def edad(self):
        return self._edad

    @edad.setter  # METODO SET  colocar/modificar
    def edad(self, edad):
        if self._validar_edad(edad):
            self._edad = edad
        else:
            print(f'Valor erroneo edad: {edad}')

    def mostrar_detalle(self):
        print(f"Persona metodo: {self._nombre} ,{self.apellido} ,{self._edad}")
        # dentro de las clases podemos utilizar self

    def _validar_edad(self,valor):
        return True if 0 < valor < 150 else False


persona1 = Persona("juan", "perez", 30)  # Un objeto

print(persona1.nombre)  # metodo get

persona1.nombre = "juan carlos"  # metodo set

print(persona1.nombre)

print('comprobacion de metodo encapsulado'.center(50,'-'))
persona1.edad=-10
