# admin.py

from user import User

class Admin(User):
    def __init__(self, user_id, name, email):
        super().__init__(user_id, name, email)
        self._access_level = 'admin'
        self._users = []

    def add_user(self, user):
        self._users.append(user)

    def remove_user(self, user):
        self._users = [u for u in self._users if u.user_id != user.user_id]

    def set_user_access_level(self, user, level):
        user.access_level = level
