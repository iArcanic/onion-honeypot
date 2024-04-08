from flask import Flask
from flask_login import LoginManager
from routes import login_blueprint, directory_listing_blueprint, logout_blueprint
from config import FLASK_SESSION_SECRET_KEY 
from models import User


# Configure Flask
app = Flask(__name__)
app.secret_key = FLASK_SESSION_SECRET_KEY

# Configure Flask Login
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)


# Register blueprints
app.register_blueprint(login_blueprint)
app.register_blueprint(directory_listing_blueprint)
app.register_blueprint(logout_blueprint)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
