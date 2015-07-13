from flask import render_template, abort
from flask.ext.login import current_user, login_required
from ..models import User, Pic
from . import panel

@panel.route('/<user_id>')
@login_required
def user(user_id):
    user = User.query.filter_by(id=int(user_id)).first()
    if user is None:
        abort(404)
    pics = user.pics.order_by(Pic.timestamp.desc())
    return render_template("panel/index.html", user=user, posts=pics)
