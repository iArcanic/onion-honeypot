import os

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer


def start_ftp_server():
    absolute_path = os.path.abspath('mock_data')
    authorizer = DummyAuthorizer()
    authorizer.add_user("user", "password", absolute_path, perm="elradfmw")
    handler = FTPHandler
    handler.authorizer = authorizer
    server = FTPServer(("0.0.0.0", 21), handler)
    server.serve_forever()


if __name__ == "__main__":
    start_ftp_server()
    
