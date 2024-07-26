from flask import Blueprint, render_template, flash, redirect, url_for
from users.model import User, User_address
from users.forms import LoginForm, RegistrationForm, UserProfileForm
from flask_login import login_user, logout_user, current_user, login_required
from config import db


blueprint = Blueprint('user', __name__, url_prefix='/users')


@blueprint.route("/login")
def login():
    if current_user.is_authenticated:
        return redirect(url_for('user.account'))
    login_form = LoginForm()
    return render_template("login.html", form=login_form)


@blueprint.route('/process-login', methods=['POST'])
def process_login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(
            username=form.username.data
            ).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            flash('Вы вошли на сайт')
            return redirect(url_for('user.account'))
    flash('Неправильное имя пользователя или пароль')
    return redirect(url_for('user.login'))


@blueprint.route('/logout', methods=['POST'])
def logout():
    logout_user()
    flash("Вы успешно вышли")
    return redirect(url_for('home_page.home_page'))


@blueprint.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    user = current_user
    address = User_address.query.filter_by(user_id=user.id).first()

    form = UserProfileForm(
        first_name=user.first_name,
        email=user.email,
        second_name=user.second_name,
        phone=user.phone_number,
        username=user.username,
        country=address.country if address else '',
        city=address.city if address else '',
        street=address.address if address else '',
        postal_code=address.postal_code if address else ''
    )

    if form.validate_on_submit():
        if (form.old_password.data and form.new_password.data and
                form.new_password2.data):
            if user.check_password(form.old_password.data):
                if form.new_password.data == form.new_password2.data:
                    user.set_password(form.new_password.data)
                else:
                    flash('Новые пароли не совпадают.')
                    return redirect(url_for('user.account'))
            else:
                flash('Старый пароль неверен.')
                return redirect(url_for('user.account'))

        user.first_name = form.first_name.data
        user.email = form.email.data
        user.second_name = form.second_name.data
        user.phone_number = form.phone.data
        user.username = form.username.data

        if address:
            address.country = form.country.data
            address.city = form.city.data
            address.address = form.street.data
            address.postal_code = form.postal_code.data
        else:
            if all([form.country.data, form.city.data, form.street.data,
                    form.postal_code.data]):
                address = User_address(
                    user_id=user.id,
                    address=form.street.data,
                    city=form.city.data,
                    postal_code=form.postal_code.data,
                    country=form.country.data
                )
                db.session.add(address)
            else:
                flash('Заполните все обязательные поля для адреса.')
                return redirect(url_for('user.account'))

        db.session.commit()
        flash('Данные успешно обновлены.')
        return redirect(url_for('user.account'))

    return render_template('account.html', form=form)


@blueprint.route('/register')
def register():
    if current_user.is_authenticated:
        return redirect(url_for('user.account'))
    reg_form = RegistrationForm()
    return render_template("registration.html", form=reg_form)


@blueprint.route('/process-reg', methods=['POST'])
def process_reg():
    form = RegistrationForm()
    if form.validate_on_submit():
        new_user = User(
            username=form.username.data,
            email=form.email.data,
            role='user'
            )
        new_user.set_password(form.password.data)
        db.session.add(new_user)
        db.session.commit()
        flash('Вы успешно зарегистрировались!')
        return redirect(url_for('user.login'))
    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash(
                    f'Ошибка в поле "{getattr(form, field).label.text}": \
                        - {error}'
                      )
        return redirect(url_for('user.register'))
