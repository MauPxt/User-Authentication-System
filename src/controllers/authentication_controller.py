import re

from src.models.user_model import UserDAO
from src.utils.encryption_utils import decrypt_password


class AuthenticationController:
    def __init__(self):
        self.user_model = UserDAO()

    def login_user(self, username, password):
        # Validate input
        if not self.valid_username(username) or not self.valid_password(
            password
        ):
            raise ValueError('Invalid username or password')

        user = self.user_model.get_user_by_username(username)
        if user is None:
            raise ValueError('Invalid username or password')

        if not decrypt_password(user.password, password):
            raise ValueError('Invalid username or password')

        return user

    def valid_username(self, username):
        if not username:
            raise ValueError('Username is required')
        elif not re.match('^[a-zA-Z0-9_]{8,20}$', username):
            raise ValueError(
                'Username must be between 8 and 20 characters and contain only letters, numbers, and underscores'
            )
        else:
            return True

    def valid_password(self, password):
        if not password:
            raise ValueError('Password is required')
        elif not re.match(
            '^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,20}$', password
        ):
            raise ValueError(
                'Password must be between 8 and 20 characters and contain at least one uppercase letter, one lowercase letter, and one number'
            )
        else:
            return True
