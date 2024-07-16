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


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    second_name = db.Column(db.String(50), nullable=False)
    phone_number = db.Column(db.BigInteger)
    created_at = db.Column(
        db.DateTime, nullable=False, server_default=db.func.now()
        )
    deleted_at = db.Column(db.DateTime)

    def __repr__(self):
        return f"User id: {self.id}, second_name: {self.second_name}"


class User_address(db.Model):
    __tablename__ = "users_address"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    address = db.Column(db.Text, nullable=False)
    city = db.Column(db.Text, nullable=False)
    postal_code = db.Column(db.String(6), nullable=False)
    country = db.Column(db.String(26), nullable=False)

    def __repr__(self):
        return f"User_address: {self.id}, address: {self.adress}"
