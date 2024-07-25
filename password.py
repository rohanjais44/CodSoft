import tkinter as tk
from tkinter import ttk, messagebox
import random
import string

class PasswordGenerator:
    def __init__(self, master):
        self.master = master
        self.master.title("Password Generator")
        self.master.geometry("400x300")
        
        self.password_label = tk.Label(self.master, text="Generated Password", font=("Arial", 18))
        self.password_label.pack(pady=10)

        self.password_entry = tk.Entry(self.master, font=("Arial", 14), width=20, state='readonly')
        self.password_entry.pack(pady=10)

        self.length_label = tk.Label(self.master, text="Password Length:", font=("Arial", 12))
        self.length_label.pack()

        self.length_scale = tk.Scale(self.master, from_=4, to=30, orient=tk.HORIZONTAL, font=("Arial", 10), length=200)
        self.length_scale.set(12)  # Default length
        self.length_scale.pack()

        self.uppercase_var = tk.IntVar()
        self.uppercase_check = tk.Checkbutton(self.master, text="Include Uppercase", variable=self.uppercase_var, font=("Arial", 12))
        self.uppercase_check.pack()

        self.lowercase_var = tk.IntVar()
        self.lowercase_check = tk.Checkbutton(self.master, text="Include Lowercase", variable=self.lowercase_var, font=("Arial", 12))
        self.lowercase_check.pack()

        self.digits_var = tk.IntVar()
        self.digits_check = tk.Checkbutton(self.master, text="Include Digits", variable=self.digits_var, font=("Arial", 12))
        self.digits_check.pack()

        self.symbols_var = tk.IntVar()
        self.symbols_check = tk.Checkbutton(self.master, text="Include Symbols", variable=self.symbols_var, font=("Arial", 12))
        self.symbols_check.pack()

        self.generate_button = tk.Button(self.master, text="Generate Password", command=self.generate_password, font=("Arial", 14))
        self.generate_button.pack(pady=20)

    def generate_password(self):
        length = self.length_scale.get()
        include_uppercase = self.uppercase_var.get()
        include_lowercase = self.lowercase_var.get()
        include_digits = self.digits_var.get()
        include_symbols = self.symbols_var.get()

        if not (include_uppercase or include_lowercase or include_digits or include_symbols):
            messagebox.showerror("Error", "Please select at least one option.")
            return

        password_characters = []
        
        if include_uppercase:
            password_characters.extend(string.ascii_uppercase)
        if include_lowercase:
            password_characters.extend(string.ascii_lowercase)
        if include_digits:
            password_characters.extend(string.digits)
        if include_symbols:
            password_characters.extend(string.punctuation)

        generated_password = ''.join(random.sample(password_characters, length))
        
        self.password_entry.config(state='normal')
        self.password_entry.delete(0, tk.END)
        self.password_entry.insert(0, generated_password)
        self.password_entry.config(state='readonly')

# Create tkinter window
window = tk.Tk()

# Create instance of the PasswordGenerator class
app = PasswordGenerator(window)

# Run the tkinter main loop
window.mainloop()
