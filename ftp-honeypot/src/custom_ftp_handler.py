from pyftpdlib.handlers import FTPHandler as OriginalFTPHandler
from utils import log_auth


class CustomFTPHandler(OriginalFTPHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.attempted_password = None


    def login(self, username, password):
        return super().login(username, password)


    def on_login_failed(self, username, password):
        log_auth(self, username, password)


    def on_login(self, username):
        password = self.attempted_password
        log_auth(self, username, password)
