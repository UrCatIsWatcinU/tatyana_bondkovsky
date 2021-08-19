from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email

required_field = DataRequired(message='Обязательное поле')

class LoginForm(FlaskForm):
    login = StringField('Логин', validators=[required_field])
    password = PasswordField('Пароль', validators=[required_field])
    remember_me = BooleanField('Запомнить меня')
    send = SubmitField('Войти')

class CallRequestForm(FlaskForm):
    email = StringField('E-mail', validators=[Email(message='Некореректный email')])