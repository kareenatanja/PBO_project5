import tkinter as tk
from tkinter import messagebox
import json
import os
import csv

USER_DATA_FILE_JSON = "user_data.json"
USER_DATA_FILE_CSV = "user_data.csv"

class HeartRateApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Heart Yield Performance Evaluator")
        self.geometry("1024x768")
        self.configure(bg='#ECE4B7')

        self.custom_font = ("Josefin Slab", 16)
        self.user_data = self.load_user_data()
        self.current_user = None

        self.show_login()

    def load_user_data(self):
        data = {}
        if os.path.exists(USER_DATA_FILE_JSON):
            with open(USER_DATA_FILE_JSON, "r") as file:
                data = json.load(file)
        return data

    def save_user_data(self):
        with open(USER_DATA_FILE_JSON, "w") as file:
            json.dump(self.user_data, file)
        self.save_user_data_to_csv()

    def save_user_data_to_csv(self):
        with open(USER_DATA_FILE_CSV, "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['username', 'password', 'name', 'age', 'gender', 'last_access'])
            for username, details in self.user_data.items():
                profile = details.get('profile', {})
                writer.writerow([
                    username,
                    details.get('password', ''),
                    profile.get('name', ''),
                    profile.get('age', ''),
                    profile.get('gender', ''),
                    details.get('last_access', '')
                ])

    def show_login(self):
        self.clear_window()
        tk.Label(self, text="USERNAME", bg='#ECE4B7', fg='#DD6031', font=self.custom_font).pack(pady=10)
        self.username_entry = tk.Entry(self, font=self.custom_font)
        self.username_entry.pack(pady=5)
        tk.Label(self, text="PASSWORD", bg='#ECE4B7', fg='#DD6031', font=self.custom_font).pack(pady=10)
        self.password_entry = tk.Entry(self, show="*", font=self.custom_font)
        self.password_entry.pack(pady=5)
        tk.Button(self, text="SUBMIT", command=self.login, bg='#18593E', fg='white', font=self.custom_font).pack(pady=10)
        tk.Button(self, text="CANCEL", command=self.clear_window, bg='#A21C1C', fg='white', font=self.custom_font).pack(pady=5)
        tk.Button(self, text="SIGN UP", command=self.show_signup, bg='#F9A826', font=self.custom_font).pack(pady=20)

    def show_signup(self):
        self.clear_window()
        tk.Label(self, text="NEW USERNAME", bg='#ECE4B7', fg='#DD6031', font=self.custom_font).pack(pady=10)
        self.new_username_entry = tk.Entry(self, font=self.custom_font)
        self.new_username_entry.pack(pady=5)
        tk.Label(self, text="NEW PASSWORD", bg='#ECE4B7', fg='#DD6031', font=self.custom_font).pack(pady=10)
        self.new_password_entry = tk.Entry(self, show="*", font=self.custom_font)
        self.new_password_entry.pack(pady=5)
        tk.Button(self, text="SUBMIT", command=self.signup, bg='#18593E', fg='white', font=self.custom_font).pack(pady=10)
        tk.Button(self, text="CANCEL", command=self.show_login, bg='#A21C1C', fg='white', font=self.custom_font).pack(pady=5)

    def show_main_menu(self):
        self.clear_window()
        tk.Button(self, text="PROFILE", command=self.show_profile_menu, bg='#F9A826', font=self.custom_font).pack(pady=10)
        tk.Button(self, text="GRAPHIC", command=self.show_graphic_menu, bg='#F9A826', font=self.custom_font).pack(pady=10)
        tk.Button(self, text="ABOUT US", command=self.show_about_us, bg='#F9A826', font=self.custom_font).pack(pady=10)
        tk.Button(self, text="HISTORY", command=self.show_history, bg='#F9A826', font=self.custom_font).pack(pady=10)
        tk.Button(self, text="LOG OUT", command=self.show_login, bg='#A21C1C', fg='white', font=self.custom_font).pack(pady=20)

    def show_profile_menu(self):
        self.clear_window()
        tk.Button(self, text="Show Profile", command=self.show_profile, bg='#F9A826', font=self.custom_font).pack(pady=10)
        tk.Button(self, text="Add/Edit Profile", command=self.show_profile_form, bg='#F9A826', font=self.custom_font).pack(pady=10)
        tk.Button(self, text="Back", command=self.show_main_menu, bg='#F9A826', font=self.custom_font).pack(pady=20)

    def show_profile(self):
        self.clear_window()
        profile = self.user_data.get(self.current_user, {}).get('profile', {})
        profile_text = f"Name: {profile.get('name', '')}\nAge: {profile.get('age', '')}\nGender: {profile.get('gender', '')}"
        tk.Label(self, text=profile_text, bg='#ECE4B7', fg='#DD6031', font=self.custom_font).pack(pady=20)
        tk.Button(self, text="Edit", command=self.show_profile_form, bg='#F9A826', font=self.custom_font).pack(pady=10)
        tk.Button(self, text="Delete", command=self.delete_profile, bg='#A21C1C', fg='white', font=self.custom_font).pack(pady=10)
        tk.Button(self, text="Back", command=self.show_profile_menu, bg='#F9A826', font=self.custom_font).pack(pady=10)

    def show_profile_form(self):
        self.clear_window()
        profile = self.user_data.get(self.current_user, {}).get('profile', {})
        tk.Label(self, text="Name", bg='#ECE4B7', fg='#DD6031', font=self.custom_font).pack(pady=10)
        self.name_entry = tk.Entry(self, font=self.custom_font)
        self.name_entry.insert(0, profile.get('name', ''))
        self.name_entry.pack(pady=5)
        tk.Label(self, text="Age", bg='#ECE4B7', fg='#DD6031', font=self.custom_font).pack(pady=10)
        self.age_entry = tk.Entry(self, font=self.custom_font)
        self.age_entry.insert(0, profile.get('age', ''))
        self.age_entry.pack(pady=5)
        tk.Label(self, text="Gender", bg='#ECE4B7', fg='#DD6031', font=self.custom_font).pack(pady=10)
        self.gender_entry = tk.Entry(self, font=self.custom_font)
        self.gender_entry.insert(0, profile.get('gender', ''))
        self.gender_entry.pack(pady=5)
        tk.Button(self, text="SAVE", command=self.submit_profile, bg='#18593E', fg='white', font=self.custom_font).pack(pady=10)
        tk.Button(self, text="CANCEL", command=self.show_profile_menu, bg='#A21C1C', fg='white', font=self.custom_font).pack(pady=5)

    def delete_profile(self):
        del self.user_data[self.current_user]['profile']
        self.save_user_data()
        messagebox.showinfo("Success", "Profile deleted")
        self.show_profile_menu()

    def show_graphic_menu(self):
        self.clear_window()
        tk.Button(self, text="Show Graphic", command=self.show_graphic, bg='#F9A826', font=self.custom_font).pack(pady=10)
        tk.Button(self, text="Print Graphic", command=self.print_graphic, bg='#F9A826', font=self.custom_font).pack(pady=10)
        tk.Button(self, text="Back", command=self.show_main_menu, bg='#F9A826', font=self.custom_font).pack(pady=20)

    def show_about_us(self):
        self.clear_window()
        frame1 = tk.Frame(self, bg='#DD6031', bd=20, relief='flat')
        frame1.place(relx=0.2, rely=0.3, relwidth=0.3, relheight=0.4)

        frame2 = tk.Frame(self, bg='#311E10', bd=20, relief='flat')
        frame2.place(relx=0.5, rely=0.2, relwidth=0.3, relheight=0.5)

        tk.Label(frame1, text="SDG Nomor 3: Kehidupan Sehat dan Sejahtera.\n\n"
                              "HYPE (Heart Yield Performance Evaluator) adalah sebuah aplikasi sederhana "
                              "untuk mendeteksi detak jantung dengan memunculkan grafik serta angka "
                              "kecepatan detak jantung lewat data yang diinputkan ke dalam program.", 
                              bg='#DD6031', fg='white', font=self.custom_font).pack(pady=10)
        
        tk.Label(frame2, text="kelompok 5 PBO\n\nHYPE (Heart Yield Performance Evaluator) merupakan program "
                              "yang dirancang oleh Kelompok 5 untuk memenuhi mata kuliah project Pemrograman "
                              "Berorientasi Objek.", 
                              bg='#311E10', fg='white', font=self.custom_font).pack(pady=10)
        
        tk.Button(self, text="Back", command=self.show_main_menu, bg='#F9A826', font=self.custom_font).pack(pady=10)

    def show_history(self):
        self.clear_window()
        last_access = self.user_data.get(self.current_user, {}).get("last_access", "No history available.")
        tk.Label(self, text=f"Last Access: {last_access}", bg='#ECE4B7', fg='#DD6031', font=self.custom_font).pack(pady=20)
        tk.Button(self, text="Back", command=self.show_main_menu, bg='#F9A826', font=self.custom_font).pack(pady=10)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if not username or not password:
            messagebox.showerror("Error", "Username and password cannot be empty")
            return

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

        if not username or not password:
            messagebox.showerror("Error", "Username and password cannot be empty")
            return

        if username in self.user_data:
            messagebox.showerror("Error", "Username already exists")
        else:
            self.user_data[username] = {'password': password, 'profile': {}, 'last_access': "Never"}
            self.save_user_data()
            messagebox.showinfo("Success", "Signup successful")
            self.show_login()

    def submit_profile(self):
        profile = {
            'name': self.name_entry.get(),
            'age': self.age_entry.get(),
            'gender': self.gender_entry.get()
        }
        self.user_data[self.current_user]['profile'] = profile
        self.save_user_data()
        messagebox.showinfo("Success", "Profile updated")
        self.show_profile_menu()

    def show_graphic(self):
        messagebox.showinfo("Graphic", "This will show the heart rate graphic.")

    def print_graphic(self):
        messagebox.showinfo("Print Graphic", "This will print the heart rate graphic.")

    def clear_window(self):
        for widget in self.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    app = HeartRateApp()
    app.mainloop()
