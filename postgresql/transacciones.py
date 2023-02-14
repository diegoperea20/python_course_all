import psycopg2 as bd

conexion = bd.connect(
    user="postgres", 
    password="admin",
     host="127.0.0.1", 
     port="5432",
      database="test_db")

# print(conexion) PARA SABER SI ESTA CONECTADO

#---------------------TRANSACCION con WITH--------------------------- MEJOR Y LA BUENA PRACTICA

try:
     with conexion:
        with conexion.cursor() as cursor:
            sentencia='INSERT INTO persona(nombre,apellido,email) VALUES(%s,%s,%s)'
            valores=('jinni','kim','jini@gmail.com')
            cursor.execute(sentencia,valores)

            sentencia='UPDATE  persona SET nombre=%s,apellido=%s,email=%s WHERE id_persona=%s'
            valores=('so','min','so@gmail.com',1)
            cursor.execute(sentencia,valores)

except Exception as e:
    print(f"Ocurrio un error, rollback: {e}")
finally:
    conexion.close()  
print('termina la transaccion')


#---------------------TRANSACCION SIN WITH---------------------------

""" try:
    conexion.autocommit=False
    cursor=conexion.cursor()
    sentencia='INSERT INTO persona(nombre,apellido,email) VALUES(%s,%s,%s)'
    valores=('mariaa','elena','ma@gmail.com')
    cursor.execute(sentencia,valores)

    sentencia='UPDATE  persona SET nombre=%s,apellido=%s,email=%s WHERE id_persona=%s'
    valores=('juan','juarez','f@gmail.com',1)
    cursor.execute(sentencia,valores)

    conexion.commit()
    print('termina la transaccion')
except Exception as e:
    conexion.rollback()
    print(f"Ocurrio un error, rollback: {e}")
finally:
    conexion.close()   """