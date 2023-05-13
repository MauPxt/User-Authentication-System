import pytest
from src.controllers.authentication_controller import AuthenticationController
from src.models.user_model import UserDAO


class TestAuthenticationController:
    def setup_method(self):
        self.controller = AuthenticationController()
        self.user_model = UserDAO()

    def teardown_method(self):
        user_model = UserDAO()
        user_model.delete_user('test_user')

    def test_login_user(self):
        username = 'test_user'
        password = 'Test1234'

        self.user_model.create_user(username, password)

        user = self.controller.login_user(username, password)
        assert user.username == username

    def test_login_user_invalid_username(self):
        usernames = ['', 'test', 'test_user' * 4, None]
        password = 'Test1234'

        for username in usernames:
            self.user_model.create_user(username, password)
            with pytest.raises(ValueError) as e:
                self.controller.login_user(username, password)
            assert (
                str(e.value) == 'Invalid username or password'
                or 'Username is required'
            )

            self.user_model.delete_user(username)

    def test_login_user_invalid_password(self):
        username = 'test_user'
        passwords = ['', 'test', 'test_user' * 4, None]

        for password in passwords:
            self.user_model.create_user(username, password)
            with pytest.raises(ValueError) as e:
                self.controller.login_user(username, password)
            assert (
                str(e.value) == 'Invalid username or password'
                or 'Password is required'
            )

            self.user_model.delete_user(username)

    def test_valid_username(self):
        usernames = ['', 'test', 'test_user' * 4, None]

        for username in usernames:
            with pytest.raises(ValueError) as e:
                self.controller.valid_username(username)
            assert (
                str(e.value) == 'Username is required'
                or 'Username must be between 8 and 20 characters and contain only letters, numbers, and underscores'
            )

    def test_valid_password(self):
        passwords = ['', 'test', 'test_user' * 4, None]

        for password in passwords:
            with pytest.raises(ValueError) as e:
                self.controller.valid_password(password)
            assert (
                str(e.value) == 'Password is required'
                or 'Password must be between 8 and 20 characters and contain at least one uppercase letter, one lowercase letter, and one number'
            )