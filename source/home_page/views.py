from home_page.models import (
    Tshirt, Outwear, Sweatwear, Socks, Shoes, Trousers,
    )
from flask import render_template, Blueprint
import random

blueprint = Blueprint("home_page", __name__)


@blueprint.route("/", methods=['GET'])
def home_page():
    models = [Tshirt, Sweatwear, Outwear, Socks, Shoes, Trousers]
    products = []
    for model in models:
        query = model.query.add_columns(
            model.picture, model.type_item,
            model.price, model.id
        )
        products.extend(query)

    random.shuffle(products)
    products = products[:4]

    return render_template("home_page.html", products=products)


# кнопки на главной странице с гендерным фильтром
@blueprint.route("/<gender>", methods=['GET'])
def catalog_gender(gender):
    models = [Tshirt, Sweatwear, Outwear, Socks, Shoes, Trousers]
    products = []
    gender_mapping = {
        'mans': 'мужской',
        'womans': 'женский',
        'kids': 'детский'
    }

    gender_value = gender_mapping.get(gender)
    for model in models:
        query = model.query.add_columns(
            model.picture, model.type_item, model.price,
            model.id
        ).filter(model.gender == gender_value).all()
        products.extend(query)
    return render_template('catalog.html', products=products)
