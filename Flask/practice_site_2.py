from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,PasswordField
from wtforms.validators import DataRequired, Email, Length

class RegistrationForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(message="Name is required!you can't leave it empty")])
    email = StringField('Email', validators=[DataRequired(message="Email is required!you can't leave it empty"), Email(message="Please enter a valid email address")])
    password = PasswordField('Password', validators=[DataRequired(message="Password is required!you can't leave it empty"), Length(min=6, message="Password must be at least 6 characters long")])
    submit = SubmitField('Register')