
#float puede recibir int y str

a= 3.0
a=float(10)
a=float('10')
print(f'{a:.2f}')# dos decimales

#si se hace una convrsion de booleano si es vacio dará false y sino true
valor={}
valore=bool(valor)
print(f'boleano: {valore}')

valori=5
valorei=bool(valori)
print(f'boleano: {valorei}')

#SYMBOLOS UNICODE
print(f'Unicode😘:')
print(f'Unicode con :\U0001F618')


#desempaquetando
valore1,valores2,valores3=1,2,3
print(valore1,valores2,valores3)

#con *args
valore1,valores2,*valores3=1,2,3,4,5,6,7
print(valore1,valores2,valores3)