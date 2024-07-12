from flask import Blueprint, render_template, flash, redirect, url_for
from users.model import User_account
from users.forms import LoginForm, RegistrationForm
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
        user = User_account.query.filter_by(
            username=form.username.data
            ).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            flash('Вы вошли на сайт')
            return redirect(url_for('user.account'))
    flash('Неправильное имя пользователя или пароль')
    return redirect(url_for('user.login'))


@blueprint.route('/logout')
def logout():
    logout_user()
    flash("Вы успешно вышли")
    return redirect(url_for('home_page.home_page'))


@blueprint.route('/account')
@login_required
def account():
    return render_template("account.html")


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
        new_user = User_account(username=form.username.data,
                                email=form.email.data, role='user')
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

