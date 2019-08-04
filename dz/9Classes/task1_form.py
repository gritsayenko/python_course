import re
from wtforms import Form, StringField, validators
class UserForm(Form):
	login = StringField('Login', [validators(pattern = r"^([a-z0-9])")])
"""password = StringField('Password', [validators(pattern = r"^([0-9a-zA-Z])(?=.*[a-z])(?=.*[A-Z])")])
    first_name = StringField(pattern=r"^([a-zA-Z])")
    last_name = StringField(pattern=r"^([a-zA-Z])")"""


login = StringField('City11')
 
