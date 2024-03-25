from flask import Flask, request, jsonify


app = Flask(__name__)


@app.route("/")
def index():
    # Check if the X-Forwarded-For header is present
    if "X-Forwarded-For" in request.headers:
        # Get the client IP address from the X-Forwarded-For header
        client_ip = request.headers.get("X-Forwarded-For").split(",")[0].strip()
    else:
        # If the header is not present, fallback to using request.remote_addr
        client_ip = request.remote_addr
    return jsonify({"client_ip": client_ip})


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
