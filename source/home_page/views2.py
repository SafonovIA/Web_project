from home_page.models import (
    Tshirt, Outwear, Sweatwear, Socks, Shoes, Trousers,
    )
from flask import render_template, Blueprint
import random

blueprint = Blueprint("home_page", __name__)


@blueprint.route("/", methods=['GET'])
def home_page():
    tshirts = Tshirt.query.add_columns(
        Tshirt.picture, Tshirt.type_item, Tshirt.price,
        Tshirt.id
        ).all()
    sweatwears = Sweatwear.query.add_columns(
        Sweatwear.picture, Sweatwear.type_item, Sweatwear.price,
        Sweatwear.id
        ).all()
    outwears = Outwear.query.add_columns(
        Outwear.picture, Outwear.type_item, Outwear.price,
        Sweatwear.id
        ).all()
    socks = Socks.query.add_columns(
        Socks.picture, Socks.type_item, Socks.price,
        Socks.id
        ).all()
    shoes = Shoes.query.add_columns(
        Shoes.picture, Shoes.type_item, Shoes.price,
        Shoes.id
        ).all()
    trousers = Trousers.query.add_columns(
        Trousers.picture, Trousers.type_item, Trousers.price,
        Trousers.id
        ).all()
    products = []

    products = tshirts + sweatwears + outwears + socks + shoes + trousers

    random.shuffle(products)
    products = products[:4]

    return render_template("home_page.html", products=products)


# кнопки на главной странице с гендерным фильтром
@blueprint.route("/<gender>", methods=['GET'])
def catalog_gender(gender):
    if gender == 'mans':
        tshirts = Tshirt.query.add_columns(
            Tshirt.picture, Tshirt.type_item, Tshirt.price,
            Tshirt.id
            ).filter(Tshirt.gender == 'мужской').all()
        sweatwears = Sweatwear.query.add_columns(
            Sweatwear.picture, Sweatwear.type_item, Sweatwear.price,
            Sweatwear.id
            ).filter(Sweatwear.gender == 'мужской').all()
        outwears = Outwear.query.add_columns(
            Outwear.picture, Outwear.type_item, Outwear.price,
            Outwear.id
            ).filter(Outwear.gender == 'мужской').all()
        socks = Socks.query.add_columns(
            Socks.picture, Socks.type_item, Socks.price,
            Socks.id
            ).filter(Socks.gender == 'мужской').all()
        shoes = Shoes.query.add_columns(
            Shoes.picture, Shoes.type_item, Shoes.price,
            Shoes.id
            ).filter(Shoes.gender == 'мужской').all()
        trousers = Trousers.query.add_columns(
            Trousers.picture, Trousers.type_item, Trousers.price,
            Trousers.id
            ).filter(Trousers.gender == 'мужской').all()
        products = tshirts + sweatwears + outwears + socks + shoes + trousers
        return render_template('catalog.html', products=products)
    elif gender == 'womans':
        tshirts = Tshirt.query.add_columns(
            Tshirt.picture, Tshirt.type_item, Tshirt.price,
            Tshirt.id
            ).filter(Tshirt.gender == 'женский').all()
        sweatwears = Sweatwear.query.add_columns(
            Sweatwear.picture, Sweatwear.type_item, Sweatwear.price,
            Sweatwear.id
            ).filter(Sweatwear.gender == 'женский').all()
        outwears = Outwear.query.add_columns(
            Outwear.picture, Outwear.type_item, Outwear.price,
            Outwear.id
            ).filter(Outwear.gender == 'женский').all()
        socks = Socks.query.add_columns(
            Socks.picture, Socks.type_item, Socks.price,
            Socks.id
            ).filter(Socks.gender == 'женский').all()
        shoes = Shoes.query.add_columns(
            Shoes.picture, Shoes.type_item, Shoes.price,
            Shoes.id
            ).filter(Shoes.gender == 'женский').all()
        trousers = Trousers.query.add_columns(
            Trousers.picture, Trousers.type_item, Trousers.price,
            Trousers.id
            ).filter(Trousers.gender == 'женский').all()
        products = tshirts + sweatwears + outwears + socks + shoes + trousers
        return render_template('catalog.html', products=products)
    elif gender == 'kids':
        tshirts = Tshirt.query.add_columns(
            Tshirt.picture, Tshirt.type_item, Tshirt.price,
            Tshirt.id
            ).filter(Tshirt.gender == 'детский').all()
        sweatwears = Sweatwear.query.add_columns(
            Sweatwear.picture, Sweatwear.type_item, Sweatwear.price,
            Sweatwear.id
            ).filter(Sweatwear.gender == 'детский').all()
        outwears = Outwear.query.add_columns(
            Outwear.picture, Outwear.type_item, Outwear.price,
            Outwear.id
            ).filter(Outwear.gender == 'детский').all()
        socks = Socks.query.add_columns(
            Socks.picture, Socks.type_item, Socks.price,
            Socks.id
            ).filter(Socks.gender == 'детский').all()
        shoes = Shoes.query.add_columns(
            Shoes.picture, Shoes.type_item, Shoes.price,
            Shoes.id
            ).filter(Shoes.gender == 'детский').all()
        trousers = Trousers.query.add_columns(
            Trousers.picture, Trousers.type_item, Trousers.price,
            Trousers.id
            ).filter(Trousers.gender == 'детский').all()
    else:
        return render_template("home_page.html")
