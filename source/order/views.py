from flask import render_template, Blueprint, request, redirect

from config import db
from home_page.models import (
    Socks, Trousers, Shoes, Outwear, Sweatwear, Tshirt, Accessories
    )
from flask_login import current_user, login_required
from order.models import Order

blueprint = Blueprint("order", __name__, url_prefix="/order")


@blueprint. route('/add', methods=['GET', 'POST'])
@login_required
def add_to_cart():
    if request.method == "POST":

        item_id = request.form["product_id"]
        type_item = request.form["product_type"]

        active_order = get_order()
        type = get_type_item()[type_item]
        item = type.query.get(item_id)

        if active_order:
            add_in_order(type_item, item)

        else:
            order = Order(
                user_id=current_user.id,
                price=0,
                amount=0,
                status='active'
                )
            db.session.add(order)
            db.session.commit()
            add_in_order(type_item, item)

    return redirect("/")


@blueprint.route("/basket")
@login_required
def basket():
    page_title = "Корзина"
    try:
        price = get_order().price
        amount = get_order().amount

    except AttributeError:
        price = 0
        amount = 0

    return render_template(
        "basket.html",
        page_title=page_title,
        items=all_order_items(),
        price=price,
        amount=amount
        )


@blueprint.route("/delet", methods=['GET', 'POST'])
def delete():
    if request.method == "POST":
        item_id = request.form["product_id"]
        type_item = request.form["product_type"]
        item = get_type_item()[type_item].query.get(item_id)
        remove_item_in_order(type_item, item)

    return redirect("/order/basket")


@blueprint.route("/checkout", methods=['POST'])
@login_required
def checkout():
    if get_order() and all_order_items():
        get_order().status = "inactive"
        db.session.commit()
    return redirect("/order/basket")


def get_order():
    user_id = current_user.id
    return Order.query.filter(
            Order.user_id == user_id,
            Order.status == "active"
            ).first()


def get_type_item():
    return {
        "Футболка": Tshirt,
        "Кофта": Sweatwear,
        "Куртка": Outwear,
        "Обувь": Shoes,
        "Штаны": Trousers,
        "Аксессуары": Accessories,
        "Носки": Socks
    }


def add_in_order(type_item, item):
    active_order = get_order()
    if active_order:
        if type_item == "Футболка":
            active_order.t_shirts.append(item)
        elif type_item == "Кофта":
            active_order.sweatwear.append(item)
        elif type_item == "Куртка":
            active_order.outwear.append(item)
        elif type_item == "Обувь":
            active_order.shoes.append(item)
        elif type_item == "Штаны":
            active_order.trousers.append(item)
        elif type_item == "Аксессуары":
            active_order.accessory.append(item)
        elif type_item == "Носки":
            active_order.socks.append(item)
        if item:
            active_order.amount += 1
            active_order.price += item.price
            db.session.commit()


def remove_item_in_order(type_item, item):
    active_order = get_order()
    if active_order:
        if type_item == "Футболка":
            active_order.t_shirts.remove(item)
        elif type_item == "Кофта":
            active_order.sweatwear.remove(item)
        elif type_item == "Куртка":
            active_order.outwear.remove(item)
        elif type_item == "Обувь":
            active_order.shoes.remove(item)
        elif type_item == "Штаны":
            active_order.trousers.remove(item)
        elif type_item == "Аксессуары":
            active_order.accessory.remove(item)
        elif type_item == "Носки":
            active_order.socks.remove(item)
        active_order.amount -= 1
        active_order.price -= item.price
        db.session.commit()


def all_order_items():
    active_order = get_order()
    lst = []
    if active_order:
        models = [
            active_order.socks,
            active_order.accessory,
            active_order.trousers,
            active_order.shoes,
            active_order.outwear,
            active_order.sweatwear,
            active_order.t_shirts
        ]
        for i in models:
            lst.extend(i)
    return lst
