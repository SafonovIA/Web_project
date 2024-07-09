from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from config import db


class User_account(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), index=True, unique=True,
                         nullable=False)
    email = db.Column(db.String(50), index=True, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    role = db.Column(db.String(10), index=True)

    def __repr__(self) -> str:
        return f"User {self.user_name}, id {self.id}"

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    @property
    def is_admin(self):
        return self.role == 'admin'
