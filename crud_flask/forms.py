from flask_wtf import FlaskForm
from wtforms import SubmitField,StringField
from wtforms.validators import DataRequired

class PersonaForm(FlaskForm):
    nombre= StringField('Nombre',validators=[DataRequired()])
    apellido=StringField('Apellido')
    email=StringField('Email', validators=[DataRequired()])
    enviar=SubmitField('Enviar')