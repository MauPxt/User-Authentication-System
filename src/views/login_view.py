import customtkinter as ctk

from src.controllers.authentication_controller import AuthenticationController


class LoginApp(ctk.CTkFrame):
    def __init__(self, parent, main_app):
        ctk.CTkFrame.__init__(self, parent)

        self.controller = AuthenticationController()

        self.main_app = main_app

        self.username_label = ctk.CTkLabel(self, text='Username')
        self.username_entry = ctk.CTkEntry(self)
        self.password_label = ctk.CTkLabel(self, text='Password')
        self.password_entry = ctk.CTkEntry(self, show='*')
        self.login_button = ctk.CTkButton(
            self, text='Login', command=self.login_user
        )

        self.to_register_page_button = ctk.CTkButton(
            self,
            text='Register',
            command=self.main_app.switch_to_registration_view,
            fg_color='yellow',
            text_color='black',
        )

        self.username_label.pack(padx=10, pady=5)
        self.username_entry.pack(padx=10, pady=10)
        self.password_label.pack(padx=10, pady=5)
        self.password_entry.pack(padx=10, pady=10)
        self.login_button.pack(padx=10, pady=10)
        self.to_register_page_button.pack(padx=10, pady=10)

    def login_user(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        try:
            # Perform login actions here
            user = self.controller.login_user(username, password)
            print('User logged in successfully')
            # change to profile page
            self.main_app.switch_to_profile_view(user)
        except ValueError as error:
            print(error)
