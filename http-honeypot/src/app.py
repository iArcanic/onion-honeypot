from flask import Flask, request, jsonify


app = Flask(__name__)


# Default endpoint
@app.route("/")
def index():
    return "HTTP Honeypot"


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
    