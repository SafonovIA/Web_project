from users.model import User_account

from config import app
from flask_login import LoginManager
from admin.views import blueprint as admin_blueprint
from users.views import blueprint as user_blueprint
from home_page.views import blueprint as home_page_blueprint

from flask_wtf.csrf import CSRFProtect

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'user.login'
app.register_blueprint(user_blueprint)
app.register_blueprint(admin_blueprint)
app.register_blueprint(home_page_blueprint)
csrf = CSRFProtect(app)


@login_manager.user_loader
def load_user(user_id):
    return User_account.query.get(user_id)


if __name__ == "__main__":
    app.run(debug=True)
