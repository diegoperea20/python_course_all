from flask import Flask, render_template, request, url_for
from werkzeug.utils import redirect
from flask_migrate import Migrate
from forms import PersonaForm


from database import db
from models import Persona


app = Flask(__name__)
app.debug=True
#configuracion de la base de datos
USER_DB='postgres'
PASS_DB='admin'
URL_DB='localhost'
NAME_DB='sap_flask_db'
FULL_URL_DB=f'postgresql://{USER_DB}:{PASS_DB}@{URL_DB}/{NAME_DB}'

app.config['SQLALCHEMY_DATABASE_URI']=FULL_URL_DB
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
#INICIACION del objeto de base de datos de sqlalchemy
#db=SQLAlchemy(app) da error por que es circular y 
# se aregla con db.init_app(app) e importacion de database y models
#configurar flask-migrate
db.init_app(app)

migrate=Migrate()
migrate.init_app(app,db)

#configuracion de flask-wtf
app.config['SECRET_KEY']='llave_secreta'







@app.route('/')
@app.route('/index')
@app.route('/index.html')
def inicio():
    #listado de personas
    #personas = Persona.query.all()
    personas = Persona.query.order_by('id')
    total_personas=Persona.query.count()
    app.logger.debug(f'listado Personas:{personas}')
    app.logger.debug(f'Total Personas:{total_personas}')
    return render_template('index.html', personas=personas, totali_personas=total_personas)


@app.route('/ver/<int:id>')
def ver_detalle(id):
    #recuperar la ersona segun id
    persona=Persona.query.get_or_404(id)
    app.logger.debug(f'Ver persona: {persona}')
    return render_template('detalle.html',persona=persona)

@app.route('/agregar',methods=['GET','POST'])
def agregar():
    persona = Persona()
    personaForm = PersonaForm(obj=persona)
    if request.method == 'POST':
        if personaForm.validate_on_submit():
           personaForm.populate_obj(persona)
           app.logger.debug(f'Persona a insertar: {persona}')
           #Insertamos el nuevo registro
           db.session.add(persona)
           db.session.commit()
           return redirect(url_for('inicio'))
    return render_template('agregar.html', forma = personaForm)

@app.route('/editar/<int:id>', methods=['GET','POST'])
def editar(id):
    #Recuperamos el objeto persona a editar
    persona = Persona.query.get_or_404(id)
    personaForma = PersonaForm(obj=persona)
    if request.method == 'POST':
        if personaForma.validate_on_submit():
            personaForma.populate_obj(persona)
            app.logger.debug(f'Persona a actualizar: {persona}')
            db.session.commit()
            return redirect(url_for('inicio'))
    return render_template('editar.html', forma = personaForma)

@app.route('/eliminar/<int:id>')
def eliminar(id):
    persona = Persona.query.get_or_404(id)
    app.logger.debug(f'Persona a eliminar: {persona}')
    db.session.delete(persona)
    db.session.commit()
    return redirect(url_for('inicio'))




if __name__ == '__main__':
    app.run()