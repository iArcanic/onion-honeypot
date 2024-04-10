import json

from flask import Blueprint, render_template, request, session, redirect, url_for
from flask_login import login_user
from models import User
from utils import send_log_to_logstash


login_blueprint = Blueprint('login', __name__, template_folder='../../src/templates')


@login_blueprint.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Load user credentials from JSON file
        with open('data/user_credentials.json', 'r') as file:
            user_credentials = json.load(file)

        # Get attempted credentials from login form
        username = request.form['username']
        password = request.form['password']

        # Send attempted credentials to Logstash
        login_log_data = {
            'honeypot': 'HTTP',
            'username': username,
            'password': password,
            'action': 'LOGIN',
            'RemoteAddr': request.remote_addr,
            'UserAgent': request.headers.get('User-Agent'),
            'RequestURI': request.full_path
        }
        send_log_to_logstash(login_log_data)

        if username in user_credentials and user_credentials[username] == password:
            user = User(username, password)
            login_user(user)
            return redirect(url_for('directory_listing.directory_listing', username=user.username))
        else:
            # Authentication failed, render login page with error message
            return render_template('login.html', error='Invalid username or password')
    
    # Render page for GET requests
    return render_template('login.html')
