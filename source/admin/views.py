from flask_login import current_user, login_required
from flask import Blueprint


blueprint = Blueprint("admin", __name__, url_prefix="/admin")


@blueprint.route('/admin')
@login_required
def admin():
    if current_user.is_admin:
        return "Админ"
    else:
        return "Доступ запрещен"
