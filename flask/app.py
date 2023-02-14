from flask import Flask, request, render_template, url_for, jsonify, session
from werkzeug.exceptions import abort
from werkzeug.utils import redirect


#http://localhost:5000/
app = Flask(__name__)

#llave cookie secreta 
app.secret_key='mi_llave_secreta'


#'/' es pagina inicio o index
@app.route('/')
def Hola():
    if 'username' in session:
         return f'el usuario ya ha hecho login{session["username"]}'
    return 'Hola Mundo Flask no has hecho login'

@app.route('/login',methods={'GET','POST'})
def login():
    if request.method == 'POST':
        #OMITIDO
        usuario=request.form['username']
        #agregar usuario a la session
        session['username']=usuario
        return redirect(url_for('Hola'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username')
    return redirect(url_for('Hola'))

@app.route('/saludar/<nombre>')
def saludo(nombre):
    return f'Saludos {nombre}'


@app.route('/edad/<int:edad>')
def edad(edad):
    return f'edad : {edad}'

@app.route('/mostrar/<nombre>', methods=['GET','POST'])
def nombrito(nombre):
    return render_template('mostrar.html',nom=nombre)

#pagina de redireccion 
@app.route('/redireciona')
def redireccionar():
    return redirect(url_for('nombrito',nombre='diego'))

#REST en JSON
@app.route('/api/mostrar/<nombre>')
def mostrar_json(nombre):
 valores={'nombre':nombre}
 return valores



#comando en terminal:
"""
    flask run : inicia servidor
    set FLASK_APP=nombre_archivo.py :modo desarrolador windows
    set FLASK_ENV=development  : AUNQUE SE PUEDE USAR 'python nombre_archivo.py'
    con este codigo al final
    
    if __name__ == '__main__':
    app.run()


    set FLASK_ENV=production
    export FLASK_APP=nombre_archivo.py :modo desarrolador linux
    flask db init : creacion migrates carpeta
    flask db migrate  :ejecuta archivo migrate
    flask db upgrade : actualiza y crea las tablas correspondientes en la base de datos
    flask db stamp head : actualiza version migrate
"""