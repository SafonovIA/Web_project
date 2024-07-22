from flask_wtf import FlaskForm
from wtforms import (
    StringField, PasswordField, SubmitField, BooleanField, ValidationError
    )
from wtforms.validators import DataRequired, EqualTo
from users.model import User


class LoginForm(FlaskForm):
    username = StringField(
        'Имя пользователя',
        validators=[DataRequired()],
        render_kw={"class": "form-control"}
        )
    password = PasswordField(
        'Пароль',
        validators=[DataRequired()],
        render_kw={"class": "form-control"}
        )
    submit = SubmitField('Войти', render_kw={"class": "btn btn-primary"})
    remember_me = BooleanField(
        "Запомнить меня",
        default=True,
        render_kw={"class": "form-check-input"}
        )


class RegistrationForm(FlaskForm):
    username = StringField(
        'Имя пользователя',
        validators=[DataRequired()],
        render_kw={"class": "form-control"}
        )
    email = StringField(
        'Email',
        validators=[DataRequired()],
        render_kw={"class": "form-control"}
        )
    password = PasswordField(
        'Пароль',
        validators=[DataRequired()],
        render_kw={"class": "form-control"}
        )
    password2 = PasswordField(
        'Повторите пароль',
        validators=[DataRequired(), EqualTo("password")],
        render_kw={"class": "form-control"}
        )
    submit = SubmitField(
        'Зарегистрироваться',
        render_kw={"class": "btn btn-success"}
        )

    def validate_username(self, username):
        count = User.query.filter_by(username=username.data).count()
        if count > 0:
            raise ValidationError(
                'Пользователь с таким именем уже зарегистрирован'
                )

    def validate_email(self, email):
        count = User.query.filter_by(email=email.data).count()
        if count > 0:
            raise ValidationError(
                'Пользователь с такой электронной почтой уже зарегистрирован'
            )
