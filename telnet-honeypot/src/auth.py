import json


# Load user credentials from JSON file
def load_credentials(filename):
    with open(filename, 'r') as file:
        return json.load(file)


# Authenticate user credentials
def authenticate_user(username, password):
    credentials = load_credentials("data/user_credentials.json")

    if username in credentials and credentials[username] == password:
        return True

    return False
    