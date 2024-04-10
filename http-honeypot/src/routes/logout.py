from flask import Blueprint, render_template, redirect, url_for
from flask_login import logout_user, current_user
from utils import send_log_to_logstash


logout_blueprint = Blueprint('logout', __name__)


@logout_blueprint.route('/logout')
def logout():
    # Send logout data to Logstash
    logout_log_data = {
        'honeypot': 'HTTP',
        'username': current_user.get_id(),
        'action': 'LOGOUT',
        'RemoteAddr': request.remote_addr,
        'UserAgent': request.headers.get('User-Agent'),
        'RequestURI': request.full_path
    }
    send_log_to_logstash(logout_log_data)

    logout_user()
    return redirect(url_for('login.login'))
