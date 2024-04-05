from flask import Blueprint, render_template, redirect, url_for
from flask_login import logout_user

logout_blueprint = Blueprint('logout', __name__)


@logout_blueprint.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login.login'))

