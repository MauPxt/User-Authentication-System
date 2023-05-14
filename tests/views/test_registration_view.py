import customtkinter
import pytest

from src.models.user_model import UserDAO
from src.views.registration_view import RegistrationApp


class MockMainApp:
    def switch_to_login_view(self):
        return None


@pytest.fixture(scope='module')
def registration_app():
    root = customtkinter.CTk()
    app = RegistrationApp(root, main_app=MockMainApp())
    yield app
    root.destroy()


class TestRegistrationApp:
    def test_gui_elements(self, registration_app):
        assert registration_app.username_label.cget('text') == 'Username'
        assert registration_app.password_label.cget('text') == 'Password'
        assert registration_app.register_button.cget('text') == 'Register'
        assert registration_app.to_login_page_button.cget('text') == 'Login'

    def test_register_user_success(self, registration_app, capsys):
        registration_app.username_entry.insert(0, 'test_user')
        registration_app.password_entry.insert(0, 'Test1234')

        if UserDAO().get_user_by_username('test_user'):
            UserDAO().delete_user('test_user')

        registration_app.register_user()
        captured = capsys.readouterr()
        assert 'User registered successfully' in captured.out

    def test_register_user_error(self, registration_app, capsys):
        invalid_usernames = ['', 'test', 'test_user' * 4, None]
        invalid_passwords = ['', 'test', 'Test1234' * 4, None]

        expected_messages = [
            'Username is required',
            'Password is required',
            'Invalid username or password',
            'Username must be between 8 and 20 characters and contain only letters, numbers, and underscores',
            'Password must be between 8 and 20 characters and contain at least one uppercase letter, one lowercase letter, and one number',
        ]

        for username in invalid_usernames:
            for password in invalid_passwords:
                registration_app.username_entry.delete(0, 'end')
                registration_app.password_entry.delete(0, 'end')

                if username:
                    registration_app.username_entry.insert(0, username)

                if password:
                    registration_app.password_entry.insert(0, password)

                registration_app.register_user()
                captured = capsys.readouterr().out.strip()
                assert captured in expected_messages
