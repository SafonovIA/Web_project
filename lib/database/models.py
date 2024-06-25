from models import db
from sqlalchemy import Enum

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    second_name = db.Column(db.String(50), nullable=False)
    phone_number = db.Column(db.BigInteger)
    city = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.func.now())
    deleted_at = db.Column(db.DateTime)
    
    user_adress = db.relationship("users_adress", backref="user", lazy=True)
    review = db.relationship("reviews", backref="user", lazy=True)
    order = db.relationship("orders", backref="user", lazy=True)
    purchase_return = db.relationship("purchase_returns", backref="user", lazy=True)
    
    def __repr__(self):
        return f'User id: {self.id}, second_name: {self.second_name}'
    
class User_adress(db.Model):
    __tablename__ = 'users_adress'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    adress = db.Column(db.Text, nullable=False)
    city = db.Column(db.Text, nullable=False)
    postal_code = db.Column(db.String(6), nullable=False)
    country = db.Column(db.String(26), nullable=False)
    
    def __repr__(self):
        return f'User_adress: {self.id}, adress: {self.adress}'
    
class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    price = db.Column(db.Float, nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.func.now())
    modified_at = db.Column(db.DateTime)
    deleted_at = db.Column(db.DateTime)
    
    t_shirts = db.relationship("tshirts", backref="order", lazy=True)
    sweatwear = db.relationship("sweatwears", backref="order", lazy=True)
    outwear = db.relationship("outwears", backref="order", lazy=True)
    shoes = db.relationship("shoes", backref="order", lazy=True)
    trousers = db.relationship("trousers", backref="order", lazy=True)
    accessory = db.relationship("accessories", backref="order", lazy=True)
    socks = db.relationship("socks", backref="order", lazy=True)
    
    def __repr__(self):
        return f'Order: {Order.id}, created: {self.created_at}'
    
class Review(db.Model):
    __tablename__ = 'reviews'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    review = db.column(db.Text)
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.func.now())
    modified_at = db.Column(db.DateTime)
    deleted_at = db.Column(db.DateTime)
    
    t_shirts = db.relationship("tshirts", backref="review", lazy=True)
    sweatwear = db.relationship("sweatwears", backref="review", lazy=True)
    outwear = db.relationship("outwears", backref="review", lazy=True)
    shoes = db.relationship("shoes", backref="review", lazy=True)
    trousers = db.relationship("trousers", backref="review", lazy=True)
    accessory = db.relationship("accessories", backref="review", lazy=True)
    socks = db.relationship("socks", backref="review", lazy=True)
    
    
    def __repr__(self):
        return f'Review: {self.id}, user: {self.user_id}, created: {self.created_at}'
    
class Purchase_return(db.Model):
    __tablename__ = 'purchase_returns'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.func.now())
    modified_at = db.Column(db.DateTime)
    deleted_at = db.Column(db.DateTime)
    
    def __repr__(self):
        return f'Purchase_return: {self.id}, order: {self.order_id}, created: {self.created_at}'
    
class Tshirt(db.Model):
    __tablename__= 'tshirts'
    id = db.Column(db.Integer, primary_key=True)
    type_item = db.Column(db.String(25), nullable=False)
    picture = db.Column(db.Text)
    brand = db.Column(db.String(50), nullable=False)
    gender = db.Column(Enum('мужской','женский', 'детский', name='gender_enum'), nullable=False)
    size = db.Column(db.Text, nullable=False)
    material = db.Column(db.Text)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    discount = db.Column(db.Integer)
    amount = db.Column(db.Integer)
    review_id = db.Column(db.Integer, db.ForeignKey('reviews.id'))
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.func.now())
    modified_at = db.Column(db.DateTime)
    deleted_at = db.Column(db.DateTime)

    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'))
        
    def __repr__(self):
        return f'Tshirt: {self.id}, created: {self.created_at}'
    
class Sweatwear(db.Model):
    __tablename__= 'sweatwears'
    id = db.Column(db.Integer, primary_key=True)
    type_item = db.Column(db.String(25), nullable=False)
    picture = db.Column(db.Text)
    brand = db.Column(db.String(50), nullable=False)
    gender = db.Column(Enum('мужской','женский', 'детский', name='gender_enum'), nullable=False)
    size = db.Column(db.Text, nullable=False)
    material = db.Column(db.Text)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    discount = db.Column(db.Integer)
    amount = db.Column(db.Integer)
    review_id = db.Column(db.Integer, db.ForeignKey('reviews.id'))
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.func.now())
    modified_at = db.Column(db.DateTime)
    deleted_at = db.Column(db.DateTime)

    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'))
    
    def __repr__(self):
        return f'Sweatwear: {self.id}, created: {self.created_at}'
        
        
class Outwear(db.Model):
    __tablename__= 'outwears'
    id = db.Column(db.Integer, primary_key=True)
    type_item = db.Column(db.String(25), nullable=False)
    picture = db.Column(db.Text)
    brand = db.Column(db.String(50), nullable=False)
    gender = db.Column(Enum('мужской','женский', 'детский', name='gender_enum'), nullable=False)
    size = db.Column(db.Text, nullable=False)
    material = db.Column(db.Text)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    discount = db.Column(db.Integer)
    amount = db.Column(db.Integer)
    review_id = db.Column(db.Integer, db.ForeignKey('reviews.id'))
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.func.now())
    modified_at = db.Column(db.DateTime)
    deleted_at = db.Column(db.DateTime)

    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'))
    
    def __repr__(self):
        return f'Outwear: {self.id}, created: {self.created_at}'
    
class Shoes(db.Model):
    __tablename__= 'shoes'
    id = db.Column(db.Integer, primary_key=True)
    type_item = db.Column(db.String(25), nullable=False)
    picture = db.Column(db.Text)
    brand = db.Column(db.String(50), nullable=False)
    gender = db.Column(Enum('мужской','женский', 'детский', name='gender_enum'), nullable=False)
    size = db.Column(db.Text, nullable=False)
    material = db.Column(db.Text)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    discount = db.Column(db.Integer)
    amount = db.Column(db.Integer)
    review_id = db.Column(db.Integer, db.ForeignKey('reviews.id'))
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.func.now())
    modified_at = db.Column(db.DateTime)
    deleted_at = db.Column(db.DateTime)

    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'))
    
    def __repr__(self):
        return f'Shoes: {self.id}, created: {self.created_at}'
    
class trousers(db.Model):
    __tablename__= 'trousers'
    id = db.Column(db.Integer, primary_key=True)
    type_item = db.Column(db.String(25), nullable=False)
    picture = db.Column(db.Text)
    brand = db.Column(db.String(50), nullable=False)
    gender = db.Column(Enum('мужской','женский', 'детский', name='gender_enum'), nullable=False)
    size = db.Column(db.Text, nullable=False)
    material = db.Column(db.Text)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    discount = db.Column(db.Integer)
    amount = db.Column(db.Integer)
    review_id = db.Column(db.Integer, db.ForeignKey('reviews.id'))
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.func.now())
    modified_at = db.Column(db.DateTime)
    deleted_at = db.Column(db.DateTime)

    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'))
    
    def __repr__(self):
        return f'Trousers: {self.id}, created: {self.created_at}'
    
class accessories(db.Model):
    __tablename__= 'accessories'
    id = db.Column(db.Integer, primary_key=True)
    type_item = db.Column(db.String(25), nullable=False)
    picture = db.Column(db.Text)
    brand = db.Column(db.String(50), nullable=False)
    gender = db.Column(Enum('мужской','женский', 'детский', name='gender_enum'), nullable=False)
    size = db.Column(db.Text, nullable=False)
    material = db.Column(db.Text)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    discount = db.Column(db.Integer)
    amount = db.Column(db.Integer)
    review_id = db.Column(db.Integer, db.ForeignKey('reviews.id'))
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.func.now())
    modified_at = db.Column(db.DateTime)
    deleted_at = db.Column(db.DateTime)

    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'))
    
    def __repr__(self):
        return f'Accessory: {self.id}, created: {self.created_at}'
    
class socks(db.Model):
    __tablename__= 'socks'
    id = db.Column(db.Integer, primary_key=True)
    type_item = db.Column(db.String(25), nullable=False)
    picture = db.Column(db.Text)
    brand = db.Column(db.String(50), nullable=False)
    gender = db.Column(Enum('мужской','женский', 'детский', name='gender_enum'), nullable=False)
    size = db.Column(db.Text, nullable=False)
    material = db.Column(db.Text)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    discount = db.Column(db.Integer)
    amount = db.Column(db.Integer)
    review_id = db.Column(db.Integer, db.ForeignKey('reviews.id'))
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.func.now())
    modified_at = db.Column(db.DateTime)
    deleted_at = db.Column(db.DateTime)

    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'))
    
    def __repr__(self):
        return f'Socks: {self.id}, created: {self.created_at}'

with app.app_context():
    db.create_all()