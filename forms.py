from wtforms import Form
from wtforms import StringField, IntegerField, PasswordField, RadioField
from wtforms import EmailField, validators

class UserForm2(Form):
    id=IntegerField('Id',[
        validators.DataRequired(message="El campo es requerido"),
        validators.NumberRange(min=10, max=1000, message="Ingrese un valor válido")
    ])
    nombre=StringField('Nombre', [
        validators.DataRequired(message="El campo es requerido"),
        validators.length(min=3, max=10, message="Ingrese un nombre válido")
    ])
    apaterno=StringField('Apaterno', [
        validators.DataRequired(message="El campo es requerido")
    ])
    email=StringField('email', [
        validators.Email(message="Ingrese un correo válido")
    ])


