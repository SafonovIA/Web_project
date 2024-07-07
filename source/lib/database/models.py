from config import db, app


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    second_name = db.Column(db.String(50), nullable=False)
    phone_number = db.Column(db.BigInteger)
    city = db.Column(db.Text, nullable=False)
    created_at = db.Column(
        db.DateTime, nullable=False, server_default=db.func.now()
        )
    deleted_at = db.Column(db.DateTime)

    def __repr__(self):
        return f"User id: {self.id}, second_name: {self.second_name}"


class User_adress(db.Model):
    __tablename__ = "users_adress"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    adress = db.Column(db.Text, nullable=False)
    city = db.Column(db.Text, nullable=False)
    postal_code = db.Column(db.String(6), nullable=False)
    country = db.Column(db.String(26), nullable=False)

    def __repr__(self):
        return f"User_adress: {self.id}, adress: {self.adress}"


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

    t_shirts = db.relationship("Tshirt", backref="order_tshirts", lazy=True)
    sweatwear = db.relationship(
        "Sweatwear", backref="order_sweatwer", lazy=True
        )
    outwear = db.relationship("Outwear", backref="order_outwear", lazy=True)
    shoes = db.relationship("Shoes", backref="order_shoes", lazy=True)
    trousers = db.relationship("Trousers", backref="order_trousers", lazy=True)
    accessory = db.relationship(
        "Accessories", backref="order_accessory", lazy=True
        )
    socks = db.relationship("Socks", backref="order_socks", lazy=True)

    user = db.relationship('User', backref='orders')

    def __repr__(self):
        return f"Order: {Order.id}, created: {self.created_at}"


class Review(db.Model):
    __tablename__ = "reviews"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    review = db.Column(db.Text)
    created_at = db.Column(
        db.DateTime, nullable=False, server_default=db.func.now()
        )
    modified_at = db.Column(db.DateTime)
    deleted_at = db.Column(db.DateTime)

    t_shirts = db.relationship("Tshirt", backref="review_tshirt", lazy=True)
    sweatwear = db.relationship(
        "Sweatwear", backref="review_sweatwear", lazy=True
        )
    outwear = db.relationship("Outwear", backref="review_outwear", lazy=True)
    shoes = db.relationship("Shoes", backref="review_shoes", lazy=True)
    trousers = db.relationship(
        "Trousers", backref="review_trouesers", lazy=True
        )
    accessory = db.relationship(
        "Accessories", backref="review_accessory", lazy=True
        )
    socks = db.relationship("Socks", backref="review_socks", lazy=True)

    user = db.relationship('User', backref='reviews')

    def __repr__(self):
        return f"Review: {self.id}, user: {self.user_id}, \
    created: {self.created_at}"


class Purchase_return(db.Model):
    __tablename__ = "purchase_returns"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    order_id = db.Column(
        db.Integer, db.ForeignKey("orders.id"), nullable=False
        )
    created_at = db.Column(
        db.DateTime, nullable=False, server_default=db.func.now()
        )
    modified_at = db.Column(db.DateTime)
    deleted_at = db.Column(db.DateTime)

    user = db.relationship('User', backref='purchase_returns')

    def __repr__(self):
        return f"Purchase_return: {self.id}, order: {self.order_id}, \
            created: {self.created_at}"


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
