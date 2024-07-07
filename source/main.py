from flask import render_template
from users.model import User_account

from config import app
from flask_login import LoginManager
from admin.views import blueprint as admin_blueprint
from users.views import blueprint as user_blueprint
from home_page.views import blueprint as home_page_blueprint

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'user.login'
app.register_blueprint(user_blueprint)
app.register_blueprint(admin_blueprint)
app.register_blueprint(home_page_blueprint)


@login_manager.user_loader
def load_user(user_id):
    return User_account.query.get(user_id)


@app.route("/basket")
def basket():
    page_title = "Корзина"
    return render_template("basket.html", page_title=page_title)


"""
# кнопки на главной странице с гендерным фильтром
@app.route("/<gender>", methods=['GET'])
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


if __name__ == "__main__":
    app.run(debug=True)
