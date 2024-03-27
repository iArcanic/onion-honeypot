import logging
import paramiko
import requests
import threading

# Configure logging
logging.basicConfig(level=logging.INFO)

# Define Flask API endpoint
FLASK_API_URL = 'http://localhost:5000/log'


# Define the SSH honeypot handler
class SSHHoneypotHandler(paramiko.ServerInterface):
    def __init__(self):
        self.event = threading.Event()

    def check_auth_password(self, username, password):
        logging.info(f"Authentication attempt - Username: {username}, Password: {password}")
        log_to_flask(username, password)
        return paramiko.AUTH_FAILED

    def check_channel_request(self, kind, chanid):
        if kind == "session":
            logging.info("Session request received")
            return paramiko.OPEN_FAILED_ADMINISTRATIVELY_PROHIBITED
        return paramiko.OPEN_FAILED_UNKNOWN_CHANNEL_TYPE


# Function to log authentication attempts to Flask server
def log_to_flask(username, password):
    payload = {'username': username, 'password': password}
    try:
        response = requests.post(FLASK_API_URL, json=payload)
        response.raise_for_status()
        logging.info("Authentication attempt logged to Flask server")
    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to log authentication attempt to Flask server: {e}")


# Start the SSH honeypot
def start_ssh_honeypot():
    # Set up SSH server
    host_key = paramiko.RSAKey.generate(2048)
    server = '0.0.0.0'
    port = 22

    logging.info(f"Starting SSH honeypot on {server}:{port}")

    # Create SSH server
    ssh_server = paramiko.Transport((server, port))
    ssh_server.add_server_key(host_key)

    # Set up SSH handler
    honeypot_handler = SSHHoneypotHandler()
    ssh_server.set_subsystem_handler("sftp", paramiko.SFTPServer, paramiko.SFTPServer)

    # Start listening for connections
    try:
        ssh_server.start_server(server=server)
        logging.info("SSH server started successfully.")
    except Exception as e:
        logging.error(f"Failed to start SSH server: {e}")

    # Accept incoming connections
    while True:
        client_socket, client_address = ssh_server.accept()
        logging.info(f"Received connection from {client_address}")
        client_thread = threading.Thread(target=handle_connection, args=(client_socket, client_address))
        client_thread.start()


if __name__ == "__main__":
    start_ssh_honeypot()
