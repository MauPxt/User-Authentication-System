import customtkinter as ctk


class ProfilleApp(ctk.CTkFrame):
    def __init__(self, parent, main_app, user):
        ctk.CTkFrame.__init__(self, parent)

        self.main_app = main_app

        self.profile_label = ctk.CTkLabel(
            self, text=f'Welcome {user.username}!'
        )
        self.profile_label.pack(padx=10, pady=5)

        self.github_frame = ctk.CTkFrame(self)
        self.github_frame.pack()
        self.github_link = ctk.CTkLabel(
            self.github_frame,
            text='github.com/MauPxt',
        )
        self.github_link.pack(padx=10, pady=5)

        self.logout_button = ctk.CTkButton(
            self,
            text='Logout',
            command=self.main_app.switch_to_login_view,
            fg_color='red',
            text_color='white',
        )
        self.logout_button.pack(padx=10, pady=10)
