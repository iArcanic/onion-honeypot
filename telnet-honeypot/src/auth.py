import json


# Load user credentials from JSON file
def load_credentials(filename):
    with open(filename, 'r') as file:
        return json.load(file)


# Authenticate user credentials
def authenticate_user(username, password):
    credentials = load_credentials("data/user_credentials.json")

    # Decode the username
    username = username.strip().decode('latin-1')
    print(f"Username: {username}")

    # Decode the password
    password = password.strip().decode('latin-1')
    print(f"Password: {password}")

    if username in credentials and credentials[username] == password:
        return True

    return False
    