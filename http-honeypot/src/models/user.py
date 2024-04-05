import json

from flask_login import UserMixin


class User(UserMixin):
    def __init__(self, username, password):
        self.username = username
        self.password = password


    def get_id(self):
        return self.username


    @classmethod
    def get(cls, user_id):
        with open('data/user_credentials.json', 'r') as file:
            user_credentials = json.load(file)

        if user_id in user_credentials:
            return cls(user_id, user_credentials[user_id])
        else:
            return None

