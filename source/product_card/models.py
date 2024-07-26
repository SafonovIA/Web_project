from config import db


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
        "Trousers", backref="review_trousers", lazy=True
        )
    accessory = db.relationship(
        "Accessories", backref="review_accessory", lazy=True
        )
    socks = db.relationship("Socks", backref="review_socks", lazy=True)

    user = db.relationship('User', backref='reviews')

    def __repr__(self):
        return f"Review: {self.id}, user: {self.user_id}, \
    created: {self.created_at}"
