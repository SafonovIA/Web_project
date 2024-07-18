from config import app, db
from flask_login import LoginManager
from admin.views import blueprint as admin_blueprint
from users.views import blueprint as user_blueprint
from home_page.views import blueprint as home_page_blueprint
from product_card.views import blueprint as product_page_blueprint
from flask_wtf.csrf import CSRFProtect
from flask_migrate import Migrate
from order.views import blueprint as order_blueprint

from home_page.models import (
    Tshirt,
    Outwear,
    Sweatwear,
    Socks,
    Shoes,
    Trousers,
    Accessories
    )
from order.models import Order
from users.model import User_account, User, User_address
from lib.database.models import Review, Purchase_return


migrate = Migrate(app, db)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'user.login'

app.register_blueprint(user_blueprint)
app.register_blueprint(admin_blueprint)
app.register_blueprint(home_page_blueprint)
app.register_blueprint(product_page_blueprint)
app.register_blueprint(order_blueprint)

csrf = CSRFProtect(app)


@login_manager.user_loader
def load_user(user_id):
    return User_account.query.get(user_id)


if __name__ == "__main__":
    app.run(debug=True)
