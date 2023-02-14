from logger_base import log
import psycopg2
from  psycopg2 import pool
import sys

class Conexion:
    _DATABASE='test_db'
    _USERNAME='postgres'
    _PASSWORD='admin'
    _DB_PORT='5432'
    _HOST='127.0.0.1'
    _MIN_CON=1 #minimo de conexiones
    _MAX_CON=5 #maximo de conexiones
    _pool=None

    @classmethod
    def obtenerPool(cls):
        if cls._pool is None:
            try:
                    cls._pool=pool.SimpleConnectionPool(cls._MIN_CON,cls._MAX_CON,host=cls._HOST,user=cls._USERNAME,password=cls._PASSWORD,port=cls._DB_PORT,database=cls._DATABASE)
                    log.debug(f'creacion del pool exitosa:{cls._pool}') 
                    return cls._pool
            except Exception as e:
                log.error(f'Ocurrio un error en el pool {e}')
                sys.exit()
        else:
            return cls._pool

    @classmethod
    def obtenerConexion(cls):
        conexion=cls.obtenerPool().getconn()
        log.debug(f'CONEXION DE POOL {conexion}')
        return conexion

    @classmethod
    def liberarConexion(cls,conexion):
        cls.obtenerPool().putconn(conexion)
        log.debug(f'Regresamos  la conexion pool: {conexion}')

    @classmethod
    def cerrarConexiones(cls):
        cls.obtenerPool().closeall()
        


# OPCION ANTIGUA NO NO RECOMENDADA
    """ @classmethod
    def obtenerConexion(cls):
        if cls._conexion is None:
            try:
                cls._conexion= bd.connect(host=cls._HOST,
                                          user=cls._USERNAME,
                                          password=cls._PASSWORD,
                                          port=cls._DB_PORT,
                                          database=cls._DATABASE)
                log.debug(f'Conexion exitosa: {cls._conexion}')
                return cls._conexion
            except Exception as e:
                    log.debug(f'Ocurrio una excepcion en conexion : {e}')
                    sys.exit()#termina todo el programa
        else:
            return cls._conexion

    @classmethod
    def obtenerCursor(cls):
        if cls._cursor is None:
            try:
                cls._cursor=cls.obtenerConexion().cursor()
                log.debug(f'se abrio correctamente el cursor: {cls._cursor}')
                return cls._cursor
            except Exception as e:
                log.error(f'Ocurrio una excepcion en cursor : {e}')
                sys.exit()
        else:
            return cls._cursor
 """


#prueba
conexion1= Conexion.obtenerConexion()
Conexion.liberarConexion(conexion1)
conexion2= Conexion.obtenerConexion()