resultado=None
a=1
b=0


try:
    resultado=a/b
except Exception as e:
    print(f'Ocurrio un error {e} , {type(e)}')
except ZeroDivisionError as e: #se puede poner varias excepcciones 
    print(f'Ocurrio un error {e}')
else:#si no se arroja inguna excepcion 
    print('no se arrojó ninguna excepción')
finally: #siempre se ejecuta sin importar excepcion o no 
    print('ejecucion finally')

print('continuamos...')

#--------------Excepcion personalizada----------------------
class Numeros_identicos(Exception):
    def __init__(self,mensaje):
        self.message=mensaje

try:
    if a==b:
        raise Numeros_identicos('numeros identicoss') #raise para excepcion personalizada
except Exception as e:
    print(f'Ocurrio un error {e} , {type(e)}')