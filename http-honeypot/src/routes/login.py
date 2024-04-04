import json

from flask import Blueprint, render_template, request, session, redirect, url_for


login_blueprint = Blueprint('login', __name__, template_folder='../../src/templates')


@login_blueprint.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Load user credentials from JSON file
        with open('data/user_credentials.json', 'r') as file:
            user_credentials = json.load(file)

        username = request.form['username']
        password = request.form['password']

        if username in user_credentials and user_credentials[username] == password:
            # Authentication successful, set session and redirect to directory listing
            session['user'] = username
            return redirect(url_for('directory_listing.directory_listing'))
        else:
            # Authentication failed, render login page with error message
            error = 'Invalid username or password'
            return render_template('login.html', error=error)

    return render_template('login.html')

