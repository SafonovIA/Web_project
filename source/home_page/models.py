from config import db
from sqlalchemy import Enum


gender_enum = Enum(
    'мужской', 'женский', 'детский', name='gender_enum', schema='public'
    )


class Tshirt(db.Model):
    __tablename__ = "tshirts"
    id = db.Column(db.Integer, primary_key=True)
    type_item = db.Column(db.String(25), nullable=False)
    picture = db.Column(db.Text)
    brand = db.Column(db.String(50), nullable=False)
    gender = db.Column(gender_enum, nullable=False)
    size = db.Column(db.Text, nullable=False)
    material = db.Column(db.Text)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    discount = db.Column(db.Integer)
    amount = db.Column(db.Integer)
    review_id = db.Column(db.Integer, db.ForeignKey("reviews.id"))
    created_at = db.Column(
        db.DateTime, nullable=False, server_default=db.func.now()
        )
    modified_at = db.Column(db.DateTime)
    deleted_at = db.Column(db.DateTime)

    order_id = db.Column(db.Integer, db.ForeignKey("orders.id"))

    def __repr__(self):
        return f"Tshirt: {self.id}, created: {self.created_at}"


class Sweatwear(db.Model):
    __tablename__ = "sweatwears"
    id = db.Column(db.Integer, primary_key=True)
    type_item = db.Column(db.String(25), nullable=False)
    picture = db.Column(db.Text)
    brand = db.Column(db.String(50), nullable=False)
    gender = db.Column(gender_enum, nullable=False)
    size = db.Column(db.Text, nullable=False)
    material = db.Column(db.Text)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    discount = db.Column(db.Integer)
    amount = db.Column(db.Integer)
    review_id = db.Column(db.Integer, db.ForeignKey("reviews.id"))
    created_at = db.Column(
        db.DateTime, nullable=False, server_default=db.func.now()
        )
    modified_at = db.Column(db.DateTime)
    deleted_at = db.Column(db.DateTime)

    order_id = db.Column(db.Integer, db.ForeignKey("orders.id"))

    def __repr__(self):
        return f"Sweatwear: {self.id}, created: {self.created_at}"


class Outwear(db.Model):
    __tablename__ = "outwears"
    id = db.Column(db.Integer, primary_key=True)
    type_item = db.Column(db.String(25), nullable=False)
    picture = db.Column(db.Text)
    brand = db.Column(db.String(50), nullable=False)
    gender = db.Column(gender_enum, nullable=False)
    size = db.Column(db.Text, nullable=False)
    material = db.Column(db.Text)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    discount = db.Column(db.Integer)
    amount = db.Column(db.Integer)
    review_id = db.Column(db.Integer, db.ForeignKey("reviews.id"))
    created_at = db.Column(
        db.DateTime, nullable=False, server_default=db.func.now()
        )
    modified_at = db.Column(db.DateTime)
    deleted_at = db.Column(db.DateTime)

    order_id = db.Column(db.Integer, db.ForeignKey("orders.id"))

    def __repr__(self):
        return f"Outwear: {self.id}, created: {self.created_at}"


class Shoes(db.Model):
    __tablename__ = "shoes"
    id = db.Column(db.Integer, primary_key=True)
    type_item = db.Column(db.String(25), nullable=False)
    picture = db.Column(db.Text)
    brand = db.Column(db.String(50), nullable=False)
    gender = db.Column(gender_enum, nullable=False)
    size = db.Column(db.Text, nullable=False)
    material = db.Column(db.Text)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    discount = db.Column(db.Integer)
    amount = db.Column(db.Integer)
    review_id = db.Column(db.Integer, db.ForeignKey("reviews.id"))
    created_at = db.Column(
        db.DateTime, nullable=False, server_default=db.func.now()
        )
    modified_at = db.Column(db.DateTime)
    deleted_at = db.Column(db.DateTime)

    order_id = db.Column(db.Integer, db.ForeignKey("orders.id"))

    def __repr__(self):
        return f"Shoes: {self.id}, created: {self.created_at}"


class Trousers(db.Model):
    __tablename__ = "trousers"
    id = db.Column(db.Integer, primary_key=True)
    type_item = db.Column(db.String(25), nullable=False)
    picture = db.Column(db.Text)
    brand = db.Column(db.String(50), nullable=False)
    gender = db.Column(gender_enum, nullable=False)
    size = db.Column(db.Text, nullable=False)
    material = db.Column(db.Text)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    discount = db.Column(db.Integer)
    amount = db.Column(db.Integer)
    review_id = db.Column(db.Integer, db.ForeignKey("reviews.id"))
    created_at = db.Column(
        db.DateTime, nullable=False, server_default=db.func.now()
        )
    modified_at = db.Column(db.DateTime)
    deleted_at = db.Column(db.DateTime)

    order_id = db.Column(db.Integer, db.ForeignKey("orders.id"))

    def __repr__(self):
        return f"Trousers: {self.id}, created: {self.created_at}"


class Accessories(db.Model):
    __tablename__ = "accessories"
    id = db.Column(db.Integer, primary_key=True)
    type_item = db.Column(db.String(25), nullable=False)
    picture = db.Column(db.Text)
    brand = db.Column(db.String(50), nullable=False)
    gender = db.Column(gender_enum, nullable=False)
    size = db.Column(db.Text, nullable=False)
    material = db.Column(db.Text)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    discount = db.Column(db.Integer)
    amount = db.Column(db.Integer)
    review_id = db.Column(db.Integer, db.ForeignKey("reviews.id"))
    created_at = db.Column(
        db.DateTime, nullable=False, server_default=db.func.now()
        )
    modified_at = db.Column(db.DateTime)
    deleted_at = db.Column(db.DateTime)

    order_id = db.Column(db.Integer, db.ForeignKey("orders.id"))

    def __repr__(self):
        return f"Accessory: {self.id}, created: {self.created_at}"


class Socks(db.Model):
    __tablename__ = "socks"
    id = db.Column(db.Integer, primary_key=True)
    type_item = db.Column(db.String(25), nullable=False)
    picture = db.Column(db.Text)
    brand = db.Column(db.String(50), nullable=False)
    gender = db.Column(gender_enum, nullable=False)
    size = db.Column(db.Text, nullable=False)
    material = db.Column(db.Text)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    discount = db.Column(db.Integer)
    amount = db.Column(db.Integer)
    review_id = db.Column(db.Integer, db.ForeignKey("reviews.id"))
    created_at = db.Column(
        db.DateTime, nullable=False, server_default=db.func.now()
        )
    modified_at = db.Column(db.DateTime)
    deleted_at = db.Column(db.DateTime)

    order_id = db.Column(db.Integer, db.ForeignKey("orders.id"))

    def __repr__(self):
        return f"Socks: {self.id}, created: {self.created_at}"
