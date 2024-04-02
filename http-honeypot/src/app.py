import json
import requests

from flask import Flask, request, jsonify

# Logstash endpoint details
LOGSTASH_HOST = "logstash"
LOGSTASH_PORT = 5514

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def index():
    # Extract request data
    request_data = {
        'RemoteAddr': request.remote_addr,
        'Method': request.method,
        'RequestURI': request.full_path,
        'Header': dict(request.headers),
        'UserAgent': request.headers.get('User-Agent'),
        'PostForm': request.form,
    }

    send_log_to_logstash(request_data)
    return jsonify(request_data)


def send_log_to_logstash(data):
    try:
        response = requests.post(f"http://{LOGSTASH_HOST}:{LOGSTASH_PORT}", json=data)
        response.raise_for_status()  # Raise an exception for non-200 status codes
        print("Log sent successfully!")
    except requests.exceptions.RequestException as e:
        print(f"Error sending log: {e}")


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
