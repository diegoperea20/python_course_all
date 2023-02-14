
def factorial(numeros):
 lista=[]
 resultado=1
 while numeros !=1:
    lista.append(numeros)
    numeros=numeros-1
 print(lista)
 for numero in lista:
    
    resultado=resultado*numero

 print("Terminado", resultado)           
        
 
numeros=int(input("ingresa un numero: "))
factorial(numeros)