"""
para crear entornos virtuales python hacer todos estos pasos , aunque NO TOCA INSTALAR
GPEDIT , PERO SI NO FUNCIONA O SE REINICIA ANTES DE LLEGAR A ESTE PASO PUES DECARGALO 
TAL CUAL ESTA EN EL VIDEO

https://www.youtube.com/watch?v=SoRS763Uho8

SI DE CASUALIDAD NO FUNCIONA , (AUNQUE ME FUNCIONÓ)
VER ESTE :
https://www.youtube.com/watch?v=W2LCF3YYpIY

------------------------------------
EN ENTORNO VIRTUAL
------------------------
COMANDOS:
------------
python -m pip install django  :INSTALA DJANGO
django-admin startproject sap : COMIENZA PROYECTO
python .\manage.py runserver : INICIA SERVIDOR (TIENE QUE ESTAR DENTRO DE CARPETA PROYECTO)
python .\manage.py startapp webapp :CREAR APP(TIENE QUE ESTAR DENTRO DE CARPETA PROYECTO) se pued eliminar todos menos init y views

python -m pip install psycopg2: INSTALAT BIBLIOTECAS EN ENTORNO VIRTUAL 

python manage.py showmigrations : CUANDO YA ESTE CREADA Y CONFIG BASE DE DATOS  
python manage.py migrate : SINCRONIZACION CON BASE DE DATOS 
python manage.py makemigrations : modelo para base de datos
python manage.py sqlmigrate personas 0001  :PARA QUE EJECUTE SQL COMANDO    DE MODELS

python manage.py createsuperuser : CREAR USUARIO DE ADMIN 
"""