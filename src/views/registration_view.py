import customtkinter as ctk

from src.controllers.registration_controller import RegistrationController


class RegistrationApp(ctk.CTkFrame):
    def __init__(self, parent, main_app):
        ctk.CTkFrame.__init__(self, parent)
        self.controller = RegistrationController()

        self.main_app = main_app

        self.username_label = ctk.CTkLabel(self, text='Username')
        self.username_entry = ctk.CTkEntry(self)
        self.password_label = ctk.CTkLabel(self, text='Password')
        self.password_entry = ctk.CTkEntry(self, show='*')
        self.register_button = ctk.CTkButton(
            self, text='Register', command=self.register_user
        )
        self.to_login_page_button = ctk.CTkButton(
            self,
            text='Login',
            command=self.main_app.switch_to_login_view,
            fg_color='yellow',
            text_color='black',
        )

        self.username_label.pack(padx=10, pady=5)
        self.username_entry.pack(padx=10, pady=10)
        self.password_label.pack(padx=10, pady=5)
        self.password_entry.pack(padx=10, pady=10)
        self.register_button.pack(padx=10, pady=10)
        self.to_login_page_button.pack(padx=10, pady=10)

    def register_user(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        try:
            # Perform registration actions here
            self.controller.register_user(username, password)
            print('User registered successfully')
        except ValueError as error:
            print(error)
