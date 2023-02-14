class Figura_geometrica:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto


class Color:
    def __init__(self, color):
        self.color = color


class Cuadrado(Figura_geometrica, Color):  # SiemPre las clases  comienzan en mayuscula
    def __init__(self, lado, color):
        # super().__init__(ancho, alto,color)  ESTO NO SE HACE DEBIDO A QUE SON DOS CLASES
        Figura_geometrica.__init__(self, lado,lado)
        Color.__init__(self, color)

    def calcular_area(self):
        return self.alto * self.ancho

cuadrado1=Cuadrado(5,'rojo')
print(cuadrado1.ancho)
print(cuadrado1.calcular_area())
print(Cuadrado.mro()) #secuenccia de donde se van a ejecutar las clases