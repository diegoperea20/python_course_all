try:
    archivo=open('prueba.txt','w', encoding='utf8')#w es para escribir y utf8 deja acentos de español
    archivo.write('agregamos información al archivo\n')
    archivo.write('Adios')
except Exception as e:
    print(e)
finally:
    archivo.close()
    print('archivo cerrado')