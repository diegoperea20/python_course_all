import psycopg2

conexion = psycopg2.connect(
    user="postgres", 
    password="admin",
     host="127.0.0.1", 
     port="5432",
      database="test_db")

# print(conexion) PARA SABER SI ESTA CONECTADO

#-----------------ELIMINAR  VARIOS REGISTROS ----------------
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = "DELETE FROM  persona WHERE id_persona IN %s"
            entrada = input('Proporciona los id_persona a eliminar (separados por coma):')
            valores=(tuple(entrada.split(',')),)
            cursor.execute(sentencia,valores)
            registros_eliminados = cursor.rowcount
            print(f'Registros eliminado: {registros_eliminados}')
except Exception as e:
    print(f"Ocurrio un error: {e}")
finally:
    conexion.close()  

#-----------------ELIMINAR  UN REGISTRO ----------------
""" try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = "DELETE FROM  persona WHERE id_persona=%s"
            valores=(7,)#de esta forma para que sea una tupla de valores 
            cursor.execute(sentencia,valores)
            registros_eliminados = cursor.rowcount
            print(f'Registros eliminado: {registros_eliminados}')
except Exception as e:
    print(f"Ocurrio un error: {e}")
finally:
    conexion.close()   """


#-----------------ACTUALIZAR  VARIOS REGISTROS ----------------
""" try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = "UPDATE persona SET nombre=%s, apellido=%s,email=%s WHERE id_persona=%s"
            valores=(
                ('gigi','laura','sl@gmail.com',1),
                ('gogo','laura','sl@gmail.com',2)
                
                )#donde este ultimo 1 es el id_persona
            cursor.executemany(sentencia,valores)
            registros_actualizados = cursor.rowcount
            print(f'Registros actualizao: {registros_actualizados}')
except Exception as e:
    print(f"Ocurrio un error: {e}")
finally:
    conexion.close()  """
#-----------------ACTUALIZAR  UN REGISTRO ----------------
""" try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = "UPDATE persona SET nombre=%s, apellido=%s,email=%s WHERE id_persona=%s"
            valores=('sana','laura','sl@gmail.com',1)#donde este ultimo 1 es el id_persona
            cursor.execute(sentencia,valores)
            registros_actualizados = cursor.rowcount
            print(f'Registros actualizao: {registros_actualizados}')
except Exception as e:
    print(f"Ocurrio un error: {e}")
finally:
    conexion.close()  """



#-----------------INSERTAR VARIOS REGISTROS----------------
""" try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = "INSERT INTO  persona(nombre,apellido,email) VALUES(%s,%s,%s)"
            valores=(
                ('marco','goz','eja@gmail.com'),
                ('di','gez','ej@gmsail.com'),
                ('ca','ga','ej@gmaisl.com')  
                )
            cursor.executemany(sentencia,valores)
            #conexion.commit() #para que guerde los cambios pero como estamos utilizando with no es necesario
            registrps_insertados = cursor.rowcount
            print(f'Registros insertados: {registrps_insertados}')
except Exception as e:
    print(f"Ocurrio un error: {e}")
finally:
    conexion.close() """



#-----------------INSERTAR UN REGISTRO ----------------
""" try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = "INSERT INTO  persona(nombre,apellido,email) VALUES(%s,%s,%s)"
            valores=('carlos','guz','ej@gmail.com')
            cursor.execute(sentencia,valores)
            #conexion.commit() #para que guerde los cambios pero como estamos utilizando with no es necesario
            registrps_insertados = cursor.rowcount
            print(f'Registros insertados: {registrps_insertados}')
except Exception as e:
    print(f"Ocurrio un error: {e}")
finally:
    conexion.close() """