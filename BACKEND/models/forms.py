
from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, EqualTo

class RegistrationForm(FlaskForm):
    """ class for modelling the registration form"""

    name = StringField(validators=[DataRequired(), Length(min=3, max=20)])
    email = EmailField(validators=[DataRequired()])
    password = PasswordField(validators=[DataRequired()])
    password_again = PasswordField(validators=[EqualTo('password', message='Enter correct password')])
    remember_me = BooleanField(default=False)
    submit = SubmitField()


class LoginForm(FlaskForm):
    """ class for modelling the login form"""

    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    remember_me = BooleanField('remember me', default=False)
    submit = SubmitField('submit')

class EditPostForm(FlaskForm):
    content = TextAreaField('content of post', validators=[DataRequired()]) 
    submit = SubmitField('submit post')
