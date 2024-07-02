from flask import Flask, render_template
from lib.database.models import *
from config import app
import random


@app.route("/", methods=['GET'])
def home_page():
    page_title = "Интернет магазин" 
    main_img = 'https://sun9-67.userapi.com/c844721/v844721600/12813f/IOTsEqFrmZY.jpg'
    #текст под картинкой
    text1 = 'Выберете интересующий вас раздел' 
    #кнопки
    button1 = 'Мужское'
    button2 = 'Женское'
    button3 = 'Детское'
    
    tshirts = Tshirt.query.all()
    sweatwears = Sweatwear.query.all()
    outwers = Outwear.query.all()
    socks = Socks.query.all()
    
    products = []
    
    products.extend(tshirts)
    products.extend(sweatwears)
    products.extend(outwers)
    products.extend(socks)
    
    random.shuffle(products)
    products = products[:4]
    
    return render_template("home_page.html", page_title=page_title, text1=text1,
                       main_img=main_img, button1=button1,
                       button2=button2, button3=button3, products=products)

@app.route("/login")
def login():
    page_title = "Авторизация"
    return render_template("login.html", page_title=page_title)

@app.route("/basket")
def basket():
    page_title = "Корзина"
    return render_template("basket.html", page_title=page_title)

@app.route("/<gender>", methods = ['GET'])
def catalo_gender(gender):
    if gender == 'mans':
        page_title = 'Мужское'
    elif gender == 'womans':
        page_title = 'Женское'
    else:
        page_title = 'Детское'
    
    return render_template('catalog.html', page_title=page_title)
    

if __name__ == "__main__":
    app.run(debug=True)
