from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Email, Length, InputRequired


class LoginForm(FlaskForm):
    username = StringField('username', validators=[Length(min=5, max=20), InputRequired()])
    password = PasswordField('password', validators=[Length(min=8, max=50), InputRequired()])
    remember_me = BooleanField('remember me')
    submit = SubmitField()

    # ...
    def __init__(self,):
        pass








