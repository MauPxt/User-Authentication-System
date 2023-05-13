import pytest
from src.controllers.registration_controller import RegistrationController


class TestRegistrationController:
    @pytest.fixture(autouse=True)
    def teardown(self, registration_controller):
        try:
            registration_controller.delete_user('test_user')
        except ValueError:
            pass

    @pytest.fixture
    def registration_controller(self):
        return RegistrationController()

    def test_register_user(self, registration_controller):
        assert registration_controller.register_user('test_user', 'Test1234')

    def test_register_user_with_invalid_username(
        self, registration_controller
    ):
        invalid_usernames = ['', 'test', 'test_user' * 4, None]

        for username in invalid_usernames:
            with pytest.raises(ValueError):
                registration_controller.register_user(username, 'Test1234')

    def test_register_user_with_invalid_password(
        self, registration_controller
    ):
        invalid_passwords = ['', 'test', 'Test1234' * 4, None]

        for password in invalid_passwords:
            with pytest.raises(ValueError):
                registration_controller.register_user('test_user', password)

    def test_register_user_with_taken_username(self, registration_controller):
        registration_controller.register_user('test_user', 'Test1234')
        with pytest.raises(ValueError):
            registration_controller.register_user('test_user', 'Test1234')

    def test_delete_user(self, registration_controller):
        registration_controller.register_user('test_user', 'Test1234')
        assert registration_controller.delete_user('test_user')

    def test_delete_nonexistent_user(self, registration_controller):
        with pytest.raises(ValueError):
            registration_controller.delete_user('test_user')

    def test_delete_user_with_invalid_username(self, registration_controller):
        invalid_usernames = ['', 'test', 'test_user' * 4, None]

        for username in invalid_usernames:
            with pytest.raises(ValueError):
                registration_controller.delete_user(username)

    def test_register_user_with_whitespace_username(
        self, registration_controller
    ):
        username = '          '
        with pytest.raises(ValueError):
            registration_controller.register_user(username, 'Test1234')

    def test_register_user_with_whitespace_password(
        self, registration_controller
    ):
        password = '          '
        with pytest.raises(ValueError):
            registration_controller.register_user('test_user', password)
