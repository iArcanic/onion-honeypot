import socket
import os

from auth import authenticate_user
from command_handler import *
from utils import send_log_to_logstash


# Function to handle client connections
def handle_client(client_socket, client_address):
    print(f"Accepted connection from {client_address}")

    # Dummy input field to consume Telnet negotiation commands
    client_socket.recv(1024)

    # Send a login prompt to the client
    client_socket.send(b"\nApacheServer login: ")

    # Receive username from the client
    username = b""
    while True:
        chunk = client_socket.recv(1)
        if chunk == b"\n":
            break
        username += chunk

    # Decode the username
    username = username.strip().decode('latin-1')

    # Send a password prompt to the client
    client_socket.send(b"Password: ")

    # Receive password from the client
    password = b""
    while True:
        chunk = client_socket.recv(1)
        if chunk == b"\n":
            break
        password += chunk

    # Decode the password
    password = password.strip().decode('latin-1')

    # Send attempted credentials to Logstash
    login_log_data = {
        'honeypot': 'TELNET',
        'username': username,
        'password': password,
        'action': 'LOGIN'
    }
    send_log_to_logstash(login_log_data)

    # Authenticate the user
    if authenticate_user(username, password):
        client_socket.send(b"\n--------------------------------\n")
        client_socket.send(b"Welcome to Apache Linux 2.4.43!\n")
        client_socket.send(b"Type 'help' for a list of commands.\n\n")

        while True:
            # Mock command prompt
            client_socket.send(bytes(username.encode()) + b"@ApacheServer:~$ ")

            # Receive command from the client
            command = b""
            while True:
                chunk = client_socket.recv(1)
                if chunk == b"\n":
                    break
                command += chunk

            # Decode the command
            command = command.strip().decode('latin-1')

            if command == "pwd":
                response = handle_pwd()
                client_socket.send(response.encode('latin-1'))
            elif command.startswith("echo"):
                message = command.split(" ", 1)[1]
                response = handle_echo(message)
                client_socket.send(response.encode('latin-1'))
            elif command in ["quit", b"exit"]:
                break
            else:
                client_socket.send(b"Command not found: " + bytes(command.encode()) + b"\n")

    else:
        client_socket.send(b"Authentication failed. Goodbye.\n")

    print(f"Connection from {client_address} closed.")
    client_socket.close()
