"""
r  = leer
a = anexar 
w = escribir
x = crear 
t= texto
b= binario(imagenes)
"""

archivo=open('C:/Users/User/Desktop/curso_python_all/manejo_archivos/prueba.txt','r')
print(archivo.read())
#print(archivo.read(5)) leer 5(n°) caracteres

#leer linea completas
#print(archivo.readline())

#iterar archivo
""" for linea in archivo:
    print(linea) """

#leer todad las lineas dando una lista
#print(archivo.readlines())


#anexar
archivo2=open('copia.txt','a')
archivo2.write(archivo.read())
archivo.close()
archivo2.close()