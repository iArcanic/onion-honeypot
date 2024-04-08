import socket


def start_telnet_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("0.0.0.0", 23))
    server_socket.listen(1)
    print("Telnet server started. Waiting for connections...")
    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection from: {client_address}")
        client_socket.send(b"Welcome to the Telnet server!\n")
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            response = b"You entered: " + data
            client_socket.send(response)
        client_socket.close()


if __name__ == "__main__":
    start_telnet_server()
    
