import os
import json

from pyftpdlib.authorizers import DummyAuthorizer
from custom_ftp_handler import CustomFTPHandler
from pyftpdlib.servers import FTPServer
from config import FTP_HOST, FTP_PORT


def start_ftp_server():
    with open('data/user_credentials.json', 'r') as file:
        user_credentials = json.load(file)

    authorizer = DummyAuthorizer()

    for username, password in user_credentials.items():
        user_path = os.path.abspath(f'data/{username}')
        authorizer.add_user(username, password, user_path, perm="elradfmw")

    handler = CustomFTPHandler
    handler.authorizer = authorizer
    handler.banner = "Welcome to the FTP server"

    server = FTPServer((FTP_HOST, FTP_PORT), handler)
    server.serve_forever()


if __name__ == "__main__":
    start_ftp_server()  
