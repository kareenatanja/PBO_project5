import tkinter as tk
from tkinter import messagebox
from tkinter.font import Font
import json
import os

# File for storing user data
USER_DATA_FILE = 'user_data.json'

class HeartRateApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Heart Yield Performance Evaluator (HYPE)")
        self.geometry("800x600")
        self.configure(bg='#ECE4B7')
        self.current_user = None

        self.custom_font = Font(family="JosefinSlabRoman Regular", size=18)
        self.header_font = Font(family="JosefinSlabRoman Regular", size=36)
        self.subheader_font = Font(family="JosefinSlabRoman Regular", size=14)

        self.load_user_data()
        self.show_login()

    def load_user_data(self):
        if os.path.exists(USER_DATA_FILE):
            with open(USER_DATA_FILE, 'r') as file:
                self.user_data = json.load(file)
        else:
            self.user_data = {}

    def save_user_data(self):
        with open(USER_DATA_FILE, 'w') as file:
            json.dump(self.user_data, file)

    def show_login(self):
        self.clear_window()

        # Header
        header_frame = tk.Frame(self, bg='#ECE4B7')
        header_frame.pack(anchor='nw', padx=20, pady=20)
        
        tk.Label(header_frame, text="HYPE", font=self.header_font, bg='#ECE4B7', fg='#DD6031').pack(anchor='nw')
        tk.Label(header_frame, text="Heart Yield Performance Evaluator", font=self.subheader_font, bg='#ECE4B7', fg='#311E10').pack(anchor='nw')

        # Login frame
        login_frame = tk.Frame(self, bg='#18593E', bd=2, relief="groove")
        login_frame.pack(pady=50, padx=20, ipadx=10, ipady=10)

        inner_frame = tk.Frame(login_frame, bg='#D9DD92', bd=0, relief="groove")
        inner_frame.pack(padx=20, pady=20, ipadx=10, ipady=10)

        tk.Label(inner_frame, text="USERNAME", bg='#D9DD92', fg='#DD6031', font=self.subheader_font).grid(row=0, column=0, pady=5, padx=5, sticky='w')
        self.username_entry = tk.Entry(inner_frame, font=self.custom_font, bg='#ECE4B7', fg='#000716', relief='flat')
        self.username_entry.grid(row=0, column=1, pady=5, padx=5, ipady=5, ipadx=5)

        tk.Label(inner_frame, text="PASSWORD", bg='#D9DD92', fg='#DD6031', font=self.subheader_font).grid(row=1, column=0, pady=5, padx=5, sticky='w')
        self.password_entry = tk.Entry(inner_frame, show="*", font=self.custom_font, bg='#ECE4B7', fg='#000716', relief='flat')
        self.password_entry.grid(row=1, column=1, pady=5, padx=5, ipady=5, ipadx=5)

        # Button frame
        button_frame = tk.Frame(inner_frame, bg='#D9DD92')
        button_frame.grid(row=2, column=1, pady=20, sticky='e')

        tk.Button(button_frame, text="SUBMIT", command=self.login, bg='#18593E', fg='white', font=self.custom_font).grid(row=0, column=0, padx=5)
        tk.Button(button_frame, text="CANCEL", command=self.clear_window, bg='#A21C1C', fg='white', font=self.custom_font).grid(row=0, column=1, padx=5)

        tk.Button(inner_frame, text="SIGN UP", command=self.show_signup, bg='#F9A826', fg='#311E10', font=self.custom_font).grid(row=3, columnspan=2, pady=10)

    def show_signup(self):
        self.clear_window()

        signup_frame = tk.Frame(self, bg='#18593E', bd=2, relief="groove")
        signup_frame.pack(pady=50, padx=20, ipadx=10, ipady=10)

        inner_frame = tk.Frame(signup_frame, bg='#D9DD92', bd=0, relief="groove")
        inner_frame.pack(padx=20, pady=20, ipadx=10, ipady=10)

        tk.Label(inner_frame, text="USERNAME", bg='#D9DD92', fg='#DD6031', font=self.subheader_font).grid(row=0, column=0, pady=5, padx=5, sticky='w')
        self.new_username_entry = tk.Entry(inner_frame, font=self.custom_font, bg='#ECE4B7', fg='#000716', relief='flat')
        self.new_username_entry.grid(row=0, column=1, pady=5, padx=5, ipady=5, ipadx=5)

        tk.Label(inner_frame, text="PASSWORD", bg='#D9DD92', fg='#DD6031', font=self.subheader_font).grid(row=1, column=0, pady=5, padx=5, sticky='w')
        self.new_password_entry = tk.Entry(inner_frame, show="*", font=self.custom_font, bg='#ECE4B7', fg='#000716', relief='flat')
        self.new_password_entry.grid(row=1, column=1, pady=5, padx=5, ipady=5, ipadx=5)

        button_frame = tk.Frame(inner_frame, bg='#D9DD92')
        button_frame.grid(row=2, column=1, pady=20, sticky='e')

        tk.Button(button_frame, text="SUBMIT", command=self.signup, bg='#18593E', fg='white', font=self.custom_font).grid(row=0, column=0, padx=5)
        tk.Button(button_frame, text="CANCEL", command=self.show_login, bg='#A21C1C', fg='white', font=self.custom_font).grid(row=0, column=1, padx=5)

    def show_main_menu(self):
        self.clear_window()

        main_menu_frame = tk.Frame(self, bg='#D9DD92', bd=2, relief="groove")
        main_menu_frame.pack(padx=20, pady=20, ipadx=10, ipady=10)

        tk.Button(main_menu_frame, text="Profile", command=self.show_profile_menu, bg='#F9A826', font=self.custom_font).pack(pady=10)
        tk.Button(main_menu_frame, text="Graphic", command=self.show_graphic_menu, bg='#F9A826', font=self.custom_font).pack(pady=10)
        tk.Button(main_menu_frame, text="About Us", command=self.show_about_us, bg='#F9A826', font=self.custom_font).pack(pady=10)
        tk.Button(main_menu_frame, text="History", command=self.show_history, bg='#F9A826', font=self.custom_font).pack(pady=10)
        tk.Button(main_menu_frame, text="Logout", command=self.show_login, bg='#F9A826', font=self.custom_font).pack(pady=10)

    def show_profile_menu(self):
        self.clear_window()

        profile_menu_frame = tk.Frame(self, bg='#D9DD92', bd=2, relief="groove")
        profile_menu_frame.pack(padx=20, pady=20, ipadx=10, ipady=10)

        tk.Button(profile_menu_frame, text="Show Profile", command=self.show_profile, bg='#F9A826', font=self.custom_font).pack(pady=10)
        tk.Button(profile_menu_frame, text="Add/Edit Profile", command=self.show_profile_form, bg='#F9A826', font=self.custom_font).pack(pady=10)
        tk.Button(profile_menu_frame, text="Back", command=self.show_main_menu, bg='#F9A826', font=self.custom_font).pack(pady=10)

    def show_profile(self):
        self.clear_window()

        profile_frame = tk.Frame(self, bg='#D9DD92', bd=2, relief="groove")
        profile_frame.pack(padx=20, pady=20, ipadx=10, ipady=10)

        user_profile = self.user_data.get(self.current_user, {}).get("profile", {})
        profile_info = f"Name: {user_profile.get('name', 'N/A')}\nAge: {user_profile.get('age', 'N/A')}\nGender: {user_profile.get('gender', 'N/A')}"

        tk.Label(profile_frame, text=profile_info, bg='#D9DD92', fg='#DD6031', font=self.custom_font).pack(pady=20)
        tk.Button(profile_frame, text="Back", command=self.show_profile_menu, bg='#F9A826', font=self.custom_font).pack(pady=10)

    def show_profile_form(self):
        self.clear_window()

        profile_form_frame = tk.Frame(self, bg='#D9DD92', bd=2, relief="groove")
        profile_form_frame.pack(padx=20, pady=20, ipadx=10, ipady=10)

        tk.Label(profile_form_frame, text="Name", bg='#D9DD92', fg='#DD6031', font=self.custom_font).grid(row=0, column=0, pady=5, padx=5, sticky='w')
        self.name_entry = tk.Entry(profile_form_frame, font=self.custom_font, bg='#ECE4B7', fg='#000716', relief='flat')
        self.name_entry.grid(row=0, column=1, pady=5, padx=5, ipady=5, ipadx=5)

        tk.Label(profile_form_frame, text="Age", bg='#D9DD92', fg='#DD6031', font=self.custom_font).grid(row=1, column=0, pady=5, padx=5, sticky='w')
        self.age_entry = tk.Entry(profile_form_frame, font=self.custom_font, bg='#ECE4B7', fg='#000716', relief='flat')
        self.age_entry.grid(row=1, column=1, pady=5, padx=5, ipady=5, ipadx=5)

        tk.Label(profile_form_frame, text="Gender", bg='#D9DD92', fg='#DD6031', font=self.custom_font).grid(row=2, column=0, pady=5, padx=5, sticky='w')
        self.gender_entry = tk.Entry(profile_form_frame, font=self.custom_font, bg='#ECE4B7', fg='#000716', relief='flat')
        self.gender_entry.grid(row=2, column=1, pady=5, padx=5, ipady=5, ipadx=5)

        button_frame = tk.Frame(self, bg='#D9DD92')
        button_frame.pack(pady=20)

        tk.Button(button_frame, text="Submit", command=self.submit_profile, bg='#18593E', fg='white', font=self.custom_font).grid(row=0, column=0, padx=5)
        tk.Button(button_frame, text="Cancel", command=self.show_profile_menu, bg='#A21C1C', fg='white', font=self.custom_font).grid(row=0, column=1, padx=5)

    def show_graphic_menu(self):
        self.clear_window()

        graphic_menu_frame = tk.Frame(self, bg='#D9DD92', bd=2, relief="groove")
        graphic_menu_frame.pack(padx=20, pady=20, ipadx=10, ipady=10)

        tk.Button(graphic_menu_frame, text="Show Graphic", command=self.show_graphic, bg='#F9A826', font=self.custom_font).pack(pady=10)
        tk.Button(graphic_menu_frame, text="Print Graphic", command=self.print_graphic, bg='#F9A826', font=self.custom_font).pack(pady=10)
        tk.Button(graphic_menu_frame, text="Back", command=self.show_main_menu, bg='#F9A826', font=self.custom_font).pack(pady=10)

    def show_about_us(self):
        self.clear_window()

        about_us_frame = tk.Frame(self, bg='#D9DD92', bd=2, relief="groove")
        about_us_frame.pack(padx=20, pady=20, ipadx=10, ipady=10)

        tk.Label(about_us_frame, text="Heart Yield Performance Evaluator (HYPE) is a ...", bg='#D9DD92', fg='#DD6031', font=self.custom_font).pack(pady=20)
        tk.Button(about_us_frame, text="Back", command=self.show_main_menu, bg='#F9A826', font=self.custom_font).pack(pady=10)

    def show_history(self):
        self.clear_window()

        history_frame = tk.Frame(self, bg='#D9DD92', bd=2, relief="groove")
        history_frame.pack(padx=20, pady=20, ipadx=10, ipady=10)

        last_access = self.user_data.get(self.current_user, {}).get("last_access", "No history available.")
        tk.Label(history_frame, text=f"Last Access: {last_access}", bg='#D9DD92', fg='#DD6031', font=self.custom_font).pack(pady=20)
        tk.Button(history_frame, text="Back", command=self.show_main_menu, bg='#F9A826', font=self.custom_font).pack(pady=10)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username in self.user_data and self.user_data[username]['password'] == password:
            self.current_user = username
            self.user_data[username]['last_access'] = "Now"  # For simplicity, setting as "Now"
            self.save_user_data()
            self.show_main_menu()
        else:
            messagebox.showerror("Error", "Invalid username or password")

    def signup(self):
        username = self.new_username_entry.get()
        password = self.new_password_entry.get()

        if username in self.user_data:
            messagebox.showerror("Error", "Username already exists")
        else:
            self.user_data[username] = {
                'password': password,
                'profile': {
                    'name': '',
                    'age': '',
                    'gender': ''
                },
                'last_access': "Never"
            }
            self.save_user_data()
            messagebox.showinfo("Success", "Signup successful")
            self.show_login()

    def submit_profile(self):
        name = self.name_entry.get()
        age = self.age_entry.get()
        gender = self.gender_entry.get()

        self.user_data[self.current_user]['profile'] = {
            'name': name,
            'age': age,
            'gender': gender
        }
        self.save_user_data()
        messagebox.showinfo("Success", "Profile updated successfully")
        self.show_profile_menu()

    def show_graphic(self):
        # Placeholder for graphic display functionality
        pass

    def print_graphic(self):
        # Placeholder for graphic printing functionality
        pass

    def clear_window(self):
        for widget in self.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    app = HeartRateApp()
    app.mainloop()