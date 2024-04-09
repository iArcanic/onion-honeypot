import socket
import threading
import json
import re

from config import TELNET_HOST, TELNET_PORT


# Load user credentials from JSON file
def load_credentials(filename):
    with open(filename, 'r') as file:
        return json.load(file)


# Function to handle client connections
def handle_client(client_socket, client_address):
    print(f"Accepted connection from {client_address}")

    # Dummy input field to consume Telnet negotiation commands
    client_socket.recv(1024)

    # Send a login prompt to the client
    client_socket.send(b"Username: ")

    # Receive username from the client
    username = b""
    while True:
        chunk = client_socket.recv(1)
        if chunk == b"\n":
            break
        username += chunk

    # Send a password prompt to the client
    client_socket.send(b"Password: ")

    # Receive password from the client
    password = b""
    while True:
        chunk = client_socket.recv(1)
        if chunk == b"\n":
            break
        password += chunk

    # Authenticate the user
    if authenticate_user(username, password):
        client_socket.send(b"Authentication successful. Welcome!\n")

        # Receive and echo data back to the client
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            print(f"Received data from {client_address}: {data.decode('latin-1')}")
            client_socket.send(data)
    else:
        client_socket.send(b"Authentication failed. Goodbye.\n")

    print(f"Connection from {client_address} closed.")
    client_socket.close()


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


# Main function to run the server
def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((TELNET_HOST, TELNET_PORT))
    server_socket.listen(5)  # Listen for incoming connections, with a backlog of 5

    # Accept incoming connections and spawn a thread to handle each one
    while True:
        client_socket, client_address = server_socket.accept()
        client_handler = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_handler.start()


if __name__ == "__main__":
    main()
