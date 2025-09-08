from flask_wtf import FlaskForm
from wtforms import StringField , SubmitField
from wtforms.validators import Optional , Length , Regexp

class AddressFormClass(FlaskForm):
    PostalCode = StringField(
        'Código Postal:', 
        validators = [
            Optional(),
            Regexp(
                r'^\d{5}$',
                message='Solo se permiten cinco números en el código postal',
            )
        ],
        render_kw = {
            'placeholder': 'Ej: 58048',
            'pattern': '[0-9]{5}',
            'size': '30',
        },
        id = 'PostalCode'
    )

    Location = StringField(
        'Colonia/Asentamiento:',
        validators = [Optional()],
        render_kw = {
            'placeholder': 'Ej: Colonia Manuel Villalongín',
            'size': '30',
        },
        id = 'Location',
    )

    City = StringField(
        'Ciudad:',
        validators = [Optional()],
        render_kw = {
            'placeholder': 'Ej: Morelia',
            'size': '30',
        },
        id = 'City',
    )

    District = StringField(
        'Municipio:',
        validators = [Optional()],
        render_kw = {
            'placeholder': 'Ej: Morelia',
            'size': '30',
        },
        id = 'District',
    )

    State = StringField(
        'Estado:',
        validators = [Optional()],
        render_kw = {
            'placeholder': 'Ej: Michoacán',
            'size': '30',
        },
        id = 'State',
    )

    AutocompleteButton = SubmitField('Autocompletar')
    CleanButton = SubmitField('Limpiar Resultado')