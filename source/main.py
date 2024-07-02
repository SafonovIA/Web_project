from flask import Flask, render_template
from lib.database.models import *
from config import app
import random


@app.route("/", methods=['GET'])
def home_page():
    page_title = "Интернет магазин" 
    tshirts = Tshirt.query.add_columns(Tshirt.picture, Tshirt.type_item, Tshirt.price).all()
    sweatwears = Sweatwear.query.add_columns(Sweatwear.picture, Sweatwear.type_item, Sweatwear.price).all()
    outwears = Outwear.query.add_columns(Outwear.picture, Outwear.type_item, Outwear.price).all()
    socks = Socks.query.add_columns(Socks.picture, Socks.type_item, Socks.price).all()
    shoes = Shoes.query.add_columns(Shoes.picture, Shoes.type_item, Shoes.price).all()
    trousers = Trousers.query.add_columns(Trousers.picture, Trousers.type_item, Trousers.price).all()
    products = []
    
    products = tshirts + sweatwears + outwears + socks + shoes + trousers
    
    random.shuffle(products)
    products = products[:4]
    
    return render_template("home_page.html", page_title=page_title, products=products)

@app.route("/login")
def login():
    page_title = "Авторизация"
    return render_template("login.html", page_title=page_title)

@app.route("/basket")
def basket():
    page_title = "Корзина"
    return render_template("basket.html", page_title=page_title)

# кнопки на главной странице с гендерным фильтром
@app.route("/<gender>", methods = ['GET'])
def catalog_gender(gender):
    # показывает только мужское
    if gender == 'mans':
        page_title = 'Мужское'
        tshirts = Tshirt.query.add_columns(Tshirt.picture, Tshirt.type_item, Tshirt.price)\
                          .filter(Tshirt.gender == 'мужской').all()
        sweatwears = Sweatwear.query.add_columns(Sweatwear.picture, Sweatwear.type_item, Sweatwear.price)\
                                .filter(Sweatwear.gender == 'мужской').all()
        outwears = Outwear.query.add_columns(Outwear.picture, Outwear.type_item, Outwear.price)\
                            .filter(Outwear.gender == 'мужской').all()
        socks = Socks.query.add_columns(Socks.picture, Socks.type_item, Socks.price)\
                       .filter(Socks.gender == 'мужской').all()
        shoes = Shoes.query.add_columns(Shoes.picture, Shoes.type_item, Shoes.price)\
                       .filter(Shoes.gender == 'мужской').all()
        trousers = Trousers.query.add_columns(Trousers.picture, Trousers.type_item, Trousers.price)\
                             .filter(Trousers.gender == 'мужской').all()

    
        products = tshirts + sweatwears + outwears + socks + shoes + trousers
    # показывает только женское
    elif gender == 'womans':
        page_title = 'Женское'
    else:
        page_title = 'Детское'
    return render_template('catalog.html', page_title=page_title, products=products)
    
 
if __name__ == "__main__":
    app.run(debug=True)
