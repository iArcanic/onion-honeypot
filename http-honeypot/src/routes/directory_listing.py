import os

from flask import Blueprint, render_template
from flask_login import login_required, current_user


directory_listing_blueprint = Blueprint('directory_listing', __name__, template_folder='../../src/templates')


@directory_listing_blueprint.route('/<username>', methods=['GET'])
@login_required
def directory_listing(username):
    if username == current_user.get_id():
        user_dir = os.path.join(os.path.abspath('data'), username)
        entries = os.listdir(user_dir)
        return render_template('directory_listing.html', username=username, entries=entries)
    else:
        return 'You are not authorized to access this directory.', 403


@directory_listing_blueprint.route('/<username>/<folder>', methods=['GET'])
@login_required
def folder_listing(username, folder):
    if username == current_user.get_id():
        user_dir = os.path.join(os.path.abspath('data'), username, folder)
        entries = os.listdir(user_dir)
        return render_template('directory_listing.html', username=username, folder=folder, entries=entries)
    else:
        return 'You are not authorized to access this directory.', 403
