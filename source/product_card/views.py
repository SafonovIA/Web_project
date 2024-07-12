from home_page.models import (
    Tshirt, Outwear, Sweatwear, Socks, Shoes, Trousers,
    Accessories)
from flask import render_template, Blueprint

blueprint = Blueprint("product_page", __name__)


@blueprint.route('/<product_type>/<int:product_id>/', methods=['GET'])
def product_details(product_type, product_id):
    product = None
    models = [Tshirt, Outwear, Sweatwear, Socks, Shoes, Trousers, Accessories]
    for model in models:
        if model.__tablename__.lower() == product_type.lower():
            product = model.query.filter_by(id=product_id).first()
            break
    models = {
        'Футболка': Tshirt,
        'Куртка': Outwear,
        'Кофта': Sweatwear,
        'Аксессуары': Socks,
        'Обувь': Shoes,
        'Штаны': Trousers
    }
    model = models.get(product_type)
    product = model.query.get(product_id)
    return render_template('product_details.html', product=product)
