from home_page.models import (
    Tshirt, Outwear, Sweatwear, Socks, Shoes, Trousers,
    )
from flask import render_template, Blueprint, request, redirect
from sqlalchemy import select
from config import db
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
    products = products[:8]

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


items = []


@blueprint.route('/add', methods=['GET', 'POST'])
def add_to_cart():
    if request.method == "POST":
        id = request.form["product_id"]
        type_item = request.form["product_type"]
        for i in (
            Socks, Trousers, Shoes, Outwear, Sweatwear, Tshirt
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
