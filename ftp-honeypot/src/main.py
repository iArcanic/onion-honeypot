import os
import json

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer


def start_ftp_server():
    with open('data/user_credentials.json', 'r') as file:
        user_credentials = json.load(file)

    authorizer = DummyAuthorizer()

    for username, password in user_credentials.items():
        absolute_path = os.path.abspath(f'data/{username}')
        authorizer.add_user(username, password, absolute_path, perm="elradfmw")

    handler = FTPHandler
    handler.authorizer = authorizer

    server = FTPServer(("0.0.0.0", 21), handler)
    server.serve_forever()


if __name__ == "__main__":
    start_ftp_server()
    
