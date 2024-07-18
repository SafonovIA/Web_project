from config import db
from sqlalchemy import Enum


status_enum = Enum(
    'active', "inactive", name='status_enum', schema='public'
    )


class Order(db.Model):
    __tablename__ = "orders"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    price = db.Column(db.Float, nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    created_at = db.Column(
        db.DateTime, nullable=False, server_default=db.func.now()
        )
    modified_at = db.Column(db.DateTime)
    deleted_at = db.Column(db.DateTime)

    t_shirts = db.relationship("Tshirt", backref="order_tshirt", lazy=True)
    sweatwear = db.relationship(
        "Sweatwear", backref="order_sweatwear", lazy=True
        )
    outwear = db.relationship("Outwear", backref="order_outwear", lazy=True)
    shoes = db.relationship("Shoes", backref="order_shoes", lazy=True)
    trousers = db.relationship("Trousers", backref="order_trousers", lazy=True)
    accessory = db.relationship(
        "Accessories", backref="order_accessory", lazy=True
        )
    socks = db.relationship("Socks", backref="order_socks", lazy=True)

    user = db.relationship('User', backref='orders')
    status = db.Column(status_enum, nullable=False)

    def __repr__(self):
        return f"Order: {Order.id}, created: {self.created_at}"
