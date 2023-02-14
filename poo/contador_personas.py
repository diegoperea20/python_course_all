class Persona:
    contador_personas=0
    #tambien se puede hacer con metodo de clase
    """  @classmethod
    def generar_siguiente_valor(cls):
        cls.contador_personas +=1
        return cls.contador_personas """

    def __init__(self,nombre,edad):
        Persona.contador_personas +=1
        self.id_persona=Persona.contador_personas
        self.nombre=nombre
        self.edad=edad
    
    def __str__(self):
        return f'Persona [{self.id_persona} {self.nombre} {self.edad}]'

persona1=Persona('Juan' ,28)
print(persona1)

persona2=Persona('hawon' ,30)
print(persona2)
