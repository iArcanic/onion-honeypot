from flask import Flask
from routes import login_blueprint, directory_listing_blueprint


app = Flask(__name__)

# Register blueprints
app.register_blueprint(login_blueprint)
app.register_blueprint(directory_listing_blueprint)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

