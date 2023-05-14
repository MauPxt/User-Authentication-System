import customtkinter as ctk
import pytest

from src.main import MainApp
from src.models.user_model import UserDAO


class TestMainApp:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.user_model = UserDAO()

    @pytest.fixture
    def main_app(self):
        app = MainApp()
        yield app
        app.root_tk.destroy()

    def test_switch_mode(self, main_app):
        current_mode = ctk.get_appearance_mode()

        # Switch mode
        main_app.switch_mode()
        new_mode = ctk.get_appearance_mode()

        # Assert mode changed
        assert new_mode != current_mode

        # Switch mode again
        main_app.switch_mode()
        final_mode = ctk.get_appearance_mode()

        # Assert mode reverted to original
        assert final_mode == current_mode

    def test_update_title(self, main_app):
        subtitle = 'Test Subtitle'
        expected_title = f'{main_app.principal_title} - {subtitle}'

        main_app.update_title(subtitle)
        assert main_app.root_tk.title() == expected_title

    def test_show_login_view(self, main_app):
        main_app.show_login_view()

        assert (
            main_app.root_tk.title() == f'{main_app.principal_title} - Login'
        )

    def test_show_registration_view(self, main_app):
        main_app.show_registration_view()

        assert (
            main_app.root_tk.title()
            == f'{main_app.principal_title} - Registration'
        )

    def test_show_profile_view(self, main_app):
        if not self.user_model.get_user_by_username('test_user'):
            self.user_model.create_user('test_user', 'Teste1234')

        user = self.user_model.get_user_by_username('test_user')

        main_app.show_profile_view(user)

        assert (
            main_app.root_tk.title()
            == f'{main_app.principal_title} - Profile - {user.username}'
        )

    def test_switch_to_login_view(self, main_app):
        main_app.switch_to_login_view()

        assert (
            main_app.root_tk.title() == f'{main_app.principal_title} - Login'
        )

    def test_switch_to_registration_view(self, main_app):
        main_app.switch_to_registration_view()

        assert (
            main_app.root_tk.title()
            == f'{main_app.principal_title} - Registration'
        )

    def test_switch_to_profile_view(self, main_app):
        self.user_model.create_user('test_user', 'Teste1234')
        user = self.user_model.get_user_by_username('test_user')

        main_app.show_profile_view(user)

        assert (
            main_app.root_tk.title()
            == f'{main_app.principal_title} - Profile - {user.username}'
        )


# Run the tests
if __name__ == '__main__':
    pytest.main()
