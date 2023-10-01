from flask_wtf import FlaskForm
from wtforms import StringField,validators,SelectField,TextAreaField,DateTimeField,DateField,RadioField,FileField,SubmitField,PasswordField,TimeField

#admin Sign Up
class AdminSignUp(FlaskForm):
    first_name=StringField("Frist Name: ")
    last_name=StringField("Last Name: ")
    email=StringField("Email: ")
    password=PasswordField("Password: ")
    confirm_password=PasswordField("Confirm Password: ")
    ati=StringField("ATI: ")
    possition=SelectField("Possision: ",choices=['Office','HOD'])
    submit=SubmitField("Submit")
