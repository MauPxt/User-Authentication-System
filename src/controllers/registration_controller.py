import re

from src.models.user_model import UserDAO


# from src.utils.encryption_utils import encrypt_password


class RegistrationController:
    def __init__(self):
        self.user_model = UserDAO()

    def register_user(self, username, password):
        self.validate_username(username)
        self.validate_password(password)

        self.check_username_not_taken(username)
        # encrypted_password = encrypt_password(password)

        self.create_user(username, password)

        return True

    def check_username_not_taken(self, username):
        if self.user_model.get_user_by_username(username) is not None:
            raise ValueError('Username already exists')

    def create_user(self, username, password):
        user_id = self.user_model.create_user(username, password)
        if user_id is None:
            raise ValueError('Invalid username or password')

    def validate_username(self, username):
        if not username:
            raise ValueError('Username is required')
        elif not re.match('^[a-zA-Z0-9_]{8,20}$', username):
            raise ValueError(
                'Username must be between 8 and 20 characters and contain only letters, numbers, and underscores'
            )

    def validate_password(self, password):
        if not password:
            raise ValueError('Password is required')
        elif not re.match(
            '^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,20}$', password
        ):
            raise ValueError(
                'Password must be between 8 and 20 characters and contain at least one uppercase letter, one lowercase letter, and one number'
            )

    def delete_user(self, username):
        self.validate_username(username)

        if self.user_model.get_user_by_username(username) is None:
            raise ValueError('User does not exist')

        if self.user_model.delete_user(username):
            return True
        else:
            raise ValueError('Failed to delete user')
