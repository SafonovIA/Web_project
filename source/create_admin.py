from getpass import getpass
import sys
from users.model import User_account
from config import db, app


with app.app_context():
    username = input('Введите имя пользователя: ')

    if User_account.query.filter(User_account.username == username).count():
        print('Такой пользователь уже есть')
        sys.exit(0)

    password = getpass('Введите пароль: ')
    password2 = getpass('Повторите пароль: ')
    if not password == password2:
        print("Разные пароли")
        sys.exit(0)

    new_user = User_account(username=username, role='admin')
    new_user.set_password(password)

    db.session.add(new_user)
    db.session.commit()
    print(f"Пользователь с именем {username} создан")
