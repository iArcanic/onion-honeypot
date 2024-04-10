import socket
import threading

from config import TELNET_HOST, TELNET_PORT
from client_handler import handle_client
from utils import send_log_to_logstash


# Main function to run the server
def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((TELNET_HOST, TELNET_PORT))
    server_socket.listen(5)  # Listen for incoming connections, with a backlog of 5

    # Accept incoming connections and spawn a thread to handle each one
    while True:
        client_socket, client_address = server_socket.accept()

        client_connection_log_data = {
            'honeypot': 'TELNET',
            'client-address': client_address,
            'action': 'TELNET-CONNECTION'
        }
        send_log_to_logstash(client_connection_log_data)

        client_handler = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_handler.start()


if __name__ == "__main__":
    main()
