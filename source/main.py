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


if __name__ == "__main__":
    app.run(debug=True)
