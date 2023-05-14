import customtkinter
import pytest

from src.main import MainApp
from src.views.login_view import LoginApp
from src.models.user_model import UserDAO


class TestLoginApp:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.user_model = UserDAO()
        if self.user_model.get_user_by_username('test_user'):
            self.user_model.delete_user('test_user')

    @pytest.fixture(scope='module')
    def login_app(self):
        root = customtkinter.CTk()
        app = LoginApp(root, MainApp())
        yield app
        root.destroy()

    def test_gui_elements(self, login_app):
        assert login_app.username_label.cget('text') == 'Username'
        assert login_app.password_label.cget('text') == 'Password'
        assert login_app.login_button.cget('text') == 'Login'
        assert login_app.to_register_page_button.cget('text') == 'Register'

    def test_login_user_success(self, login_app, capsys):
        login_app.username_entry.insert(0, 'test_user')
        login_app.password_entry.insert(0, 'Test1234')

        self.user_model.create_user('test_user', 'Test1234')

        login_app.login_user()

        captured = capsys.readouterr()
        assert captured.out.strip() == 'User logged in successfully'

    def test_login_user_error(self, login_app, capsys):
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
                login_app.username_entry.delete(0, 'end')
                login_app.password_entry.delete(0, 'end')

                if username:
                    login_app.username_entry.insert(0, username)

                if password:
                    login_app.password_entry.insert(0, password)

                login_app.login_user()
                captured = capsys.readouterr()
                assert captured.out.strip() in expected_messages


if __name__ == '__main__':
    pytest.main()
