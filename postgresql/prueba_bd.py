import psycopg2

conexion = psycopg2.connect(
    user="postgres", 
    password="admin",
     host="127.0.0.1", 
     port="5432",
      database="test_db")

# print(conexion) PARA SABER SI ESTA CONECTADO

#----------------------FORMA CON VARIOS INDICES -------------------
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = "SELECT * FROM persona WHERE id_persona in  %s "  #%s es unparametro posicional
            entrada=input('proporciona los ids a buscar (separado por comas): ') #ejempl: 1,2,3
            llaves_primarias= (tuple(entrada.split(',')))                                         
            cursor.execute(sentencia,(llaves_primarias,))
            registros = cursor.fetchall()
            for registro in registros:
                print(registro)
except Exception as e:
    print(f"Ocurrio un error: {e}")
finally:
    conexion.close()




#-----------------------FORMA NORMAL-----------------------------
""" try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = "SELECT * FROM persona WHERE id_persona= %s "  #%s es unparametro posicional
            id_persona=input('proporciona el valor id_persona: ')                                          #espera al valor de la variable
            cursor.execute(sentencia,(id_persona,))
            registros = cursor.fetchall()
            print(registros)
except Exception as e:
    print(f"Ocurrio un error: {e}")
finally:
    conexion.close()
 """