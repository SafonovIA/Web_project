from home_page.models import (
    Tshirt, Outwear, Sweatwear, Socks, Shoes, Trousers,
    )
from flask import render_template, Blueprint
import random

blueprint = Blueprint("home_page", __name__)


@blueprint.route("/", methods=['GET'])
def home_page():
    tshirts = Tshirt.query.add_columns(
        Tshirt.picture, Tshirt.type_item, Tshirt.price
        ).all()
    sweatwears = Sweatwear.query.add_columns(
        Sweatwear.picture, Sweatwear.type_item, Sweatwear.price
        ).all()
    outwears = Outwear.query.add_columns(
        Outwear.picture, Outwear.type_item, Outwear.price
        ).all()
    socks = Socks.query.add_columns(
        Socks.picture, Socks.type_item, Socks.price
        ).all()
    shoes = Shoes.query.add_columns(
        Shoes.picture, Shoes.type_item, Shoes.price
        ).all()
    trousers = Trousers.query.add_columns(
        Trousers.picture, Trousers.type_item, Trousers.price
        ).all()
    products = []

    products = tshirts + sweatwears + outwears + socks + shoes + trousers

    random.shuffle(products)
    products = products[:4]

    return render_template("home_page.html", products=products)


"""
# кнопки на главной странице с гендерным фильтром
@blueprint.route("/<gender>", methods=['GET'])
def catalog_gender(gender):
    # показывает только мужское
    if gender == 'mans':
        tshirts = Tshirt.query.add_columns(
            Tshirt.picture, Tshirt.type_item, Tshirt.price
            ).filter(Tshirt.gender == 'мужской').all()
        sweatwears = Sweatwear.query.add_columns(
            Sweatwear.picture, Sweatwear.type_item, Sweatwear.price
            ).filter(Sweatwear.gender == 'мужской').all()
        outwears = Outwear.query.add_columns(
            Outwear.picture, Outwear.type_item, Outwear.price
            ).filter(Outwear.gender == 'мужской').all()
        socks = Socks.query.add_columns(
            Socks.picture, Socks.type_item, Socks.price
            ).filter(Socks.gender == 'мужской').all()
        shoes = Shoes.query.add_columns(
            Shoes.picture, Shoes.type_item, Shoes.price
            ).filter(Shoes.gender == 'мужской').all()
        trousers = Trousers.query.add_columns(
            Trousers.picture, Trousers.type_item, Trousers.price
            ).filter(Trousers.gender == 'мужской').all()

        products = tshirts + sweatwears + outwears + socks + shoes + trousers
    # показывает только женское
        return render_template('catalog.html', products=products)

    elif gender == 'womans':
        pass
"""
