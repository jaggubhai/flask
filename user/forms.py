from flask_wtf import Form
from wtforms import validators, StringField, PasswordField
from wtforms.fields.html5 import EmailField
from wtforms.validators import ValidationError



class RegisterForm(Form):
    first_name = StringField('First name', [validators.Required()]) #if these fields are empty it will ask user to mention them
    last_name = StringField('Last name', [validators.Required()])
    email = EmailField('Email address', [
        validators.DataRequired(),
        validators.Email()
        ])
    username = StringField('Username', [
        validators.Required(),
        validators.length(min=4, max=25)
        ])
    password = PasswordField('New Password', [
        validators.Required(),
        validators.EqualTo('confirm', message='passwords must match'),
        validators.length(min=8, max=15)
        ])
    confirm = PasswordField('Repeat Password')



 
