# user.py

class User:
    def __init__(self, user_id, name, email):
        self._user_id = user_id
        self._name = name
        self._email = email
        self._access_level = 'user'

    @property
    def user_id(self):
        return self._user_id

    @property
    def name(self):
        return self._name

    @property
    def email(self):
        return self._email

    @property
    def access_level(self):
        return self._access_level

    @access_level.setter
    def access_level(self, level):
        self._access_level = level
