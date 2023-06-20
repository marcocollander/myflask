from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email


class NameForm(FlaskForm):
    number_of_hits = StringField("Ilość trafień", validators=[DataRequired()])
    number_of_attempts = StringField("Ilość prób", validators=[DataRequired()])
    hit_percentage = StringField("Procent trafień", validators=[DataRequired()])
    submit = SubmitField("Wyślij")


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[Email()])
    password = PasswordField("Hasło", validators=[DataRequired()])
    submit = SubmitField("Zaloguj się")


class RegisterForm(FlaskForm):
    name = StringField("Imię", validators=[DataRequired()])
    email = StringField("Email", validators=[Email()])
    password = PasswordField("Hasło", validators=[DataRequired()])
    submit = SubmitField("Zarejestruj się")
