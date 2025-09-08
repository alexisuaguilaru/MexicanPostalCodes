from flask import Flask , request , jsonify , render_template , redirect , url_for
import os
from AddressFinder import *

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY_FLASK','012345')

ConnectionDatabase = SQLConnector(
    os.getenv('MARIADB_HOST','localhost'),
    os.getenv('MARIADB_USER','user_db'),
    os.getenv('MARIADB_PASSWORD','password_db'),
    os.getenv('MARIADB_DATABASE','PostalCodes'),
)


@app.route('/',methods=['GET', 'POST'])
def IndexHome():

    AddressForm = AddressFormClass()
    if AddressForm.validate_on_submit():
        if AddressForm.AutocompleteButton.data:
            AutocompleteFields(AddressForm,ConnectionDatabase)
        elif AddressForm.CleanButton.data:
            return redirect(url_for('IndexHome'))

    return render_template('index.html',Form=AddressForm)


if __name__ == '__main__':
    app.run(
        debug = True,
        port = 8080,
    )