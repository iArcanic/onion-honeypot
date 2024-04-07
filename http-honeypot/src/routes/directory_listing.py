import os

from flask import Blueprint, render_template, send_file
from flask_login import login_required, current_user


directory_listing_blueprint = Blueprint('directory_listing', __name__, template_folder='../../src/templates')


@directory_listing_blueprint.route('/<username>', methods=['GET'])
@login_required
def directory_listing(username):
    if username == current_user.get_id():
        absolute_path = os.path.join(os.path.abspath('data'), username)
        entries = os.listdir(absolute_path)
        return render_template('directory_listing.html', username=username, entries=entries)
    else:
        return 'You are not authorized to access this directory.', 403


@directory_listing_blueprint.route('/<username>/<path:requested_path>', methods=['GET'])
@login_required
def serve_file(username, requested_path):
    if username == current_user.get_id():
        # Construct absolute path to the requested resource
        absolute_path = os.path.join(os.path.abspath('data'), username, requested_path)

        # If it's a directory, list its contents
        if os.path.isdir(absolute_path):
            entries = os.listdir(absolute_path)
            return render_template('directory_listing.html', username=username, folder=requested_path, entries=entries)
        # If it's a file, serve it for download
        elif os.path.isfile(absolute_path):
            return send_file(absolute_path, as_attachment=True)
        else:
            return 'Resource not found.', 404
    else:
        return 'You are not authorized to access this directory.', 403
