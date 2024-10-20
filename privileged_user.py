# privileged_user.py

from user import User

class PrivilegedUser(User):
    def __init__(self, user_id, name, email):
        super().__init__(user_id, name, email)
        self._access_level = 'privileged'

    def access_user_data(self):
        return "Accessing user data..."

    def access_statistics(self):
        return "Accessing site statistics..."
