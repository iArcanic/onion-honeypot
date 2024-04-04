from flask import Blueprint, render_template


login_blueprint = Blueprint('login', __name__, template_folder='../../src/templates')


@login_blueprint.route('/', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

