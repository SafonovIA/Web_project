from flask import render_template, Blueprint, redirect, url_for, flash
from home_page.models import (
    Tshirt, Outwear, Sweatwear, Socks, Shoes, Trousers,
    Accessories)
from lib.database.models import Review
from .forms import ReviewForm
from flask_login import current_user
from config import db
from datetime import datetime, timezone

blueprint = Blueprint("product_page", __name__)


@blueprint.route('/<product_type>/<int:product_id>/', methods=['GET', 'POST'])
def product_details(product_type, product_id):
    models = {
        'Футболка': Tshirt,
        'Куртка': Outwear,
        'Кофта': Sweatwear,
        'Аксессуары': Accessories,
        'Обувь': Shoes,
        'Штаны': Trousers,
        'Носки': Socks
    }
    model = models.get(product_type)
    product = model.query.get(product_id)
    review_id = product.review_id
    reviews = Review.query.filter_by(id=review_id).all()
    print(reviews)
    if len(reviews) > 1:
        review_list = reviews
    else:
        review_list = reviews if reviews else []
    if reviews:
        total_rating = sum(review.rating for review in reviews)
        average_rating = total_rating / len(reviews)
        rating = round(average_rating)
    else:
        rating = None
    form = ReviewForm()
    if form.validate_on_submit():
        if current_user.is_authenticated:
            new_review = Review(
                user_id=current_user.id,
                rating=form.rating.data,
                review=form.review.data,
                created_at=datetime.now(timezone.utc)
            )
            db.session.add(new_review)
            db.session.commit()
            flash('Вы оставили отзыв, спасибо!')
            review_id = new_review.id
            product.review_id = review_id
            db.session.commit()
            return redirect(url_for('product_page.product_details',
                                    product_type=product_type,
                                    product_id=product_id))
        else:
            return redirect(url_for('auth.login'))

    return render_template('product_details.html', product=product,
                           rating=rating, reviews=review_list, form=form)
