from flask_wtf import FlaskForm
from wtforms import (
    StringField, PasswordField, SubmitField, BooleanField, ValidationError
    )
from wtforms.validators import DataRequired, EqualTo, Email
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


class UserProfileForm(FlaskForm):
    first_name = StringField(
        'Имя',
        validators=[DataRequired()],
        render_kw={"class": "form-control"}
    )
    email = StringField(
        'Email',
        validators=[DataRequired(), Email()],
        render_kw={"class": "form-control"}
    )
    second_name = StringField(
        'Фамилия',
        validators=[DataRequired()],
        render_kw={"class": "form-control"}
    )
    phone = StringField(
        'Номер телефона',
        validators=[DataRequired()],
        render_kw={"class": "form-control"}
    )
    username = StringField(
        'Логин',
        validators=[DataRequired()],
        render_kw={"class": "form-control"}
    )
    old_password = PasswordField(
        'Старый пароль',
        render_kw={"class": "form-control"}
    )
    new_password = PasswordField(
        'Новый пароль',
        render_kw={"class": "form-control"}
    )
    new_password2 = PasswordField(
        'Повторите новый пароль',
        render_kw={"class": "form-control"}
    )
    country = StringField(
        'Страна',
        validators=[DataRequired()],
        render_kw={"class": "form-control"}
    )
    city = StringField(
        'Город',
        validators=[DataRequired()],
        render_kw={"class": "form-control"}
    )
    street = StringField(
        'Улица',
        validators=[DataRequired()],
        render_kw={"class": "form-control"}
    )
    postal_code = StringField(
        'Почтовый индекс',
        validators=[DataRequired()],
        render_kw={"class": "form-control"}
    )
    submit = SubmitField(
        'Обновить данные',
        render_kw={"class": "btn btn-primary"}
    )