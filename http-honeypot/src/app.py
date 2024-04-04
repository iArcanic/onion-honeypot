from flask import Flask
from routes import login_blueprint, directory_listing_blueprint
from config import FLASK_SESSION_SECRET_KEY 

app = Flask(__name__)
app.secret_key = FLASK_SESSION_SECRET_KEY

# Register blueprints
app.register_blueprint(login_blueprint)
app.register_blueprint(directory_listing_blueprint)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

