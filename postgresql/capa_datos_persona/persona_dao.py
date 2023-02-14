from conexion import *
from persona import *
from logger_base import log
from cursor_del_pool import *


class PersonaDao:
    # DAO DATA ACCESS OBJECT

    _SELECCIONAR='SELECT * FROM persona ORDER BY id_persona'
    _INSERTAR='INSERT INTO persona(nombre,apellido,email) VALUES (%s,%s,%s)'
    _ACTUALIZAR='UPDATE persona SET nombre=%s , apellido=%s , emial=%s WHERE id_persona=%s'
    _ELIMINAR='DELETE FROM persona WHERE id_persona=%s'

    @classmethod
    def seleccionar(cls):
       with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros =cursor.fetchall()
            personas=[]
            for registro in registros:
                persona=Persona(registro[0],registro[1],registro[2],registro[3])
                personas.append(persona)
            return personas
        
    @classmethod
    def insertar(cls,persona):
        with CursorDelPool() as cursor:
            valores = (persona.nombre, persona.apellido, persona.email)
            cursor.execute(cls._INSERTAR,valores)
            log.debug(f'Persona a insertar: {persona}')
            return cursor.rowcount

    @classmethod
    def actualizar(cls,persona):
        with CursorDelPool() as cursor:
            valores = (persona.nombre, persona.apellido, persona.email,persona.id_persona)
            cursor.execute(cls._ACTUALIZAR,valores)
            log.debug(f'Persona actualizada: {persona}')
            return cursor.rowcount
    @classmethod
    def eliminar(cls,persona):
        with CursorDelPool() as cursor:  
            valores = (persona.id_persona,)
            cursor.execute(cls._ELIMINAR,valores)
            log.debug(f'Persona eliminada: {persona}')
            return cursor.rowcount


#prueba eliminar

persona1=Persona(id_persona=20)
personas_eliminadas=PersonaDao.actualizar(persona1)
log.debug(f'PERSONAS eliminadas: {personas_eliminadas}')


#prueba actualizar 
persona1=Persona(1,'pedro' ,'najera','ejem@gmail.com')
personas_actualizada=PersonaDao.actualizar(persona1)
log.debug(f'PERSONAS actualizadas: {personas_actualizada}')


#prueba insertar registro
persona1=Persona(nombre='pedro' , apellido='najera',email='ejem@gmail.com')
personas_insertadas=PersonaDao.insertar(persona1)
log.debug(f'PERSONAS insertadas: {personas_insertadas}')

#prueba seleccionar objetos
personas=PersonaDao.seleccionar()
for persona in personas:
    log.debug(persona)