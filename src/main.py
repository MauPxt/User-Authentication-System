import customtkinter as ctk

from src.views.login_view import LoginApp
from src.views.profile_view import ProfilleApp
from src.views.registration_view import RegistrationApp


class MainApp:
    def __init__(self):
        self.root_tk = ctk.CTk()
        self.root_tk.geometry('500x500')
        self.root_tk.resizable(False, False)
        self.principal_title = 'Main App'
        self.root_tk.title(self.principal_title)

        self.container = ctk.CTkFrame(self.root_tk)
        self.container.pack(fill='both', expand=True)

        self.show_login_view()

        # Create a button to switch mode
        self.create_mode_button()

    def create_mode_button(self):
        self.mode_button = ctk.CTkButton(
            self.root_tk, text='Switch Mode', command=self.switch_mode
        )
        self.mode_button.pack(side='bottom', fill='x', padx=10, pady=10)

    def switch_mode(self):
        current_mode = ctk.get_appearance_mode()
        new_mode = 'Light' if current_mode == 'Dark' else 'Dark'
        ctk.set_appearance_mode(new_mode)

    def show_login_view(self):
        login_view = LoginApp(self.container, self)
        login_view.pack(padx=10, pady=10, ipadx=10, ipady=10)
        self.update_title('Login')

    def show_registration_view(self):
        registration_view = RegistrationApp(self.container, self)
        registration_view.pack(padx=10, pady=10, ipadx=10, ipady=10)
        self.update_title('Registration')

    def switch_to_registration_view(self):
        self.clear_container()
        self.show_registration_view()

    def switch_to_login_view(self):
        self.clear_container()
        self.show_login_view()

    def switch_to_profile_view(self, user):
        self.clear_container()
        self.show_profile_view(user)

    def show_profile_view(self, user):
        profile_view = ProfilleApp(self.container, self, user)
        profile_view.pack(padx=10, pady=10, ipadx=10, ipady=10)
        self.update_title(f'Profile - {user.username}')

    def clear_container(self):
        self.container.pack_forget()
        self.container = ctk.CTkFrame(self.root_tk)
        self.container.pack(fill='both', expand=True)

    def update_title(self, subtitle):
        self.root_tk.title(f'{self.principal_title} - {subtitle}')

    def run(self):
        self.root_tk.mainloop()


if __name__ == '__main__':
    main_app = MainApp()
    main_app.run()
