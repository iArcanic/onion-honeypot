from flask import Flask, request, jsonify


app = Flask(__name__)


# Default endpoint for testing
@app.route("/")
def index():
    return "Onion Honeypot Flask API"


@app.route("/log", methods=['POST'])
def log_handler():
    if request.method == 'POST':
        log_data = request.json
        return jsonify({"message": "Log received successfully", "data": log_data}), 200
    else:
        return f'{request.method} Method Not Allowed', 405


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
