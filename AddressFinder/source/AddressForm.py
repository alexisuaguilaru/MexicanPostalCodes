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
        },
        id = 'PostalCode'
    )

    Location = StringField(
        'Colonia/Asentamiento:',
        validators = [Optional()],
        render_kw = {'placeholder': 'Ej: Colonia Manuel Villalongín'},
        id = 'Location',
    )

    City = StringField(
        'Ciudad:',
        validators = [Optional()],
        render_kw = {'placeholder': 'Ej: Morelia'},
        id = 'City',
    )

    District = StringField(
        'Municipio:',
        validators = [Optional()],
        render_kw = {'placeholder': 'Ej: Morelia'},
        id = 'District',
    )

    State = StringField(
        'Estado:',
        validators = [Optional()],
        render_kw = {'placeholder': 'Ej: Michoacán'},
        id = 'State',
    )

    AutocompleteButton = SubmitField('Autocompletar')
    CleanButton = SubmitField('Limpiar Resultados')