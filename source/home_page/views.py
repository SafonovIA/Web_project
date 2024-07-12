from home_page.models import (
    Tshirt, Outwear, Sweatwear, Socks, Shoes, Trousers, Accessories
    )
from flask import render_template, Blueprint, request, redirect
from config import db
from sqlalchemy import select
import random


blueprint = Blueprint("home_page", __name__)


@blueprint.route("/", methods=['GET'])
def home_page():
    tshirts = Tshirt.query.add_columns(
        Tshirt.picture, Tshirt.type_item, Tshirt.price, Tshirt.id
        ).all()
    sweatwears = Sweatwear.query.add_columns(
        Sweatwear.picture, Sweatwear.type_item, Sweatwear.price, Sweatwear.id
        ).all()
    outwears = Outwear.query.add_columns(
        Outwear.picture, Outwear.type_item, Outwear.price, Outwear.id
        ).all()
    socks = Socks.query.add_columns(
        Socks.picture, Socks.type_item, Socks.price, Socks.id
        ).all()
    shoes = Shoes.query.add_columns(
        Shoes.picture, Shoes.type_item, Shoes.price, Shoes.id
        ).all()
    trousers = Trousers.query.add_columns(
        Trousers.picture, Trousers.type_item, Trousers.price, Trousers.id
        ).all()
    products = []

    products = tshirts + sweatwears + outwears + socks + shoes + trousers

    random.shuffle(products)
    products = products[:8]

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


items = []


@blueprint.route('/add', methods=['GET', 'POST'])
def add_to_cart():
    if request.method == "POST":
        id = request.form["product_id"]
        type_item = request.form["product_type"]
        for i in (
            Accessories, Trousers, Shoes, Outwear, Sweatwear, Tshirt
                ):
            query = select(i).where(i.id == id, i.type_item == type_item)
            item = db.session.scalar(query)
            if item:
                items.append({
                    "picture": item.picture,
                    "type_item": item.type_item,
                    "price": item.price,
                    "id": item.id
                    })
                print(items)
                break

        return redirect("/")
    else:
        return redirect("/")


@blueprint.route("/basket")
def basket():
    page_title = "Корзина"
    return render_template(
        "basket.html",
        page_title=page_title,
        items=items
        )


@blueprint.route("/delet", methods=['GET', 'POST'])
def delete():
    dell = request.form["dell"]
    items.remove(eval(dell))
    return redirect("/basket")
