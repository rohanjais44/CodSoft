import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import random
import string

class PasswordGenerator:
    def __init__(self, master):
        self.master = master
        self.master.title("Password Generator")
        self.master.geometry("500x550")  # Increased size for better layout

        # Style Configuration
        self.master.configure(bg='#f5f5f5')
        font_large = ("Arial", 16)
        font_medium = ("Arial", 12)
        font_small = ("Arial", 10)

        # Header
        self.header_frame = tk.Frame(self.master, bg='#4CAF50')
        self.header_frame.pack(fill=tk.X, pady=10)
        self.header_label = tk.Label(self.header_frame, text="Password Generator", font=("Arial", 24, 'bold'), bg='#4CAF50', fg='white')
        self.header_label.pack(padx=20, pady=10)

        # Generated Password
        self.password_label = tk.Label(self.master, text="Generated Password", font=font_large, bg='#f5f5f5')
        self.password_label.pack(pady=10)

        self.password_entry = tk.Entry(self.master, font=("Arial", 14), width=40, state='readonly', bd=2, relief='solid')
        self.password_entry.pack(pady=10)

        # Copy Button
        self.copy_button = tk.Button(self.master, text="Copy Password", command=self.copy_password, font=font_large, bg='#FF5722', fg='white', bd=0, width=20)
        self.copy_button.pack(pady=10)

        # Password Length
        self.length_label = tk.Label(self.master, text="Password Length:", font=font_medium, bg='#f5f5f5')
        self.length_label.pack()

        self.length_scale = tk.Scale(self.master, from_=4, to=30, orient=tk.HORIZONTAL, font=font_small, length=300, bg='#f5f5f5')
        self.length_scale.set(12)  # Default length
        self.length_scale.pack(pady=10)

        # Character Options
        options_frame = tk.Frame(self.master, bg='#f5f5f5')
        options_frame.pack(pady=10)

        self.uppercase_var = tk.IntVar()
        self.uppercase_check = tk.Radiobutton(options_frame, text="Include Uppercase", variable=self.uppercase_var, value=1, font=font_medium, bg='#f5f5f5', activebackground='#e0e0e0', indicatoron=0)
        self.uppercase_check.grid(row=0, column=0, padx=10, pady=5)

        self.lowercase_var = tk.IntVar()
        self.lowercase_check = tk.Radiobutton(options_frame, text="Include Lowercase", variable=self.lowercase_var, value=1, font=font_medium, bg='#f5f5f5', activebackground='#e0e0e0', indicatoron=0)
        self.lowercase_check.grid(row=0, column=1, padx=10, pady=5)

        self.digits_var = tk.IntVar()
        self.digits_check = tk.Radiobutton(options_frame, text="Include Digits", variable=self.digits_var, value=1, font=font_medium, bg='#f5f5f5', activebackground='#e0e0e0', indicatoron=0)
        self.digits_check.grid(row=1, column=0, padx=10, pady=5)

        self.symbols_var = tk.IntVar()
        self.symbols_check = tk.Radiobutton(options_frame, text="Include Symbols", variable=self.symbols_var, value=1, font=font_medium, bg='#f5f5f5', activebackground='#e0e0e0', indicatoron=0)
        self.symbols_check.grid(row=1, column=1, padx=10, pady=5)

        # Additional Words
        self.words_label = tk.Label(self.master, text="Additional Words (comma-separated):", font=font_medium, bg='#f5f5f5')
        self.words_label.pack(pady=10)

        self.words_entry = tk.Entry(self.master, font=("Arial", 14), width=40, bd=2, relief='solid')
        self.words_entry.pack(pady=10)

        # Buttons
        self.button_frame = tk.Frame(self.master, bg='#f5f5f5')
        self.button_frame.pack(pady=20)

        self.generate_button = tk.Button(self.button_frame, text="Generate Password", command=self.generate_password, font=font_large, bg='#4CAF50', fg='white', bd=0, width=20)
        self.generate_button.grid(row=0, column=0, padx=10)

        self.save_button = tk.Button(self.button_frame, text="Save Password", command=self.save_password, font=font_large, bg='#2196F3', fg='white', bd=0, width=20)
        self.save_button.grid(row=0, column=1, padx=10)

    def generate_password(self):
        length = self.length_scale.get()
        include_uppercase = self.uppercase_var.get()
        include_lowercase = self.lowercase_var.get()
        include_digits = self.digits_var.get()
        include_symbols = self.symbols_var.get()

        if not (include_uppercase or include_lowercase or include_digits or include_symbols):
            messagebox.showerror("Error", "Please select at least one option.")
            return

        additional_words = self.words_entry.get().split(',')
        additional_words = [word.strip() for word in additional_words if word.strip()]

        password_characters = []
        
        if include_uppercase:
            password_characters.extend(string.ascii_uppercase)
        if include_lowercase:
            password_characters.extend(string.ascii_lowercase)
        if include_digits:
            password_characters.extend(string.digits)
        if include_symbols:
            password_characters.extend(string.punctuation)

        # Generate the password base
        if not password_characters:
            password_characters = string.ascii_letters + string.digits + string.punctuation
        
        if length > 0:
            generated_password = ''.join(random.choices(password_characters, k=length))
        else:
            generated_password = ''

        # Insert additional words if specified
        if additional_words:
            additional_word_str = ''.join(additional_words)
            # Adjust length to ensure that additional words fit
            remaining_length = max(0, length - len(additional_word_str))
            generated_password = ''.join(random.choices(password_characters, k=remaining_length)) + additional_word_str
        
        self.password_entry.config(state='normal')
        self.password_entry.delete(0, tk.END)
        self.password_entry.insert(0, generated_password)
        self.password_entry.config(state='readonly')

    def copy_password(self):
        password = self.password_entry.get()
        if not password:
            messagebox.showerror("Error", "No password to copy. Generate a password first.")
            return
        
        self.master.clipboard_clear()
        self.master.clipboard_append(password)
        messagebox.showinfo("Success", "Password copied to clipboard.")

    def save_password(self):
        password = self.password_entry.get()
        if not password:
            messagebox.showerror("Error", "No password to save. Generate a password first.")
            return
        
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                               filetypes=[("Text files", "*.txt"), ("All files", "*.*")],
                                               title="Save Password")
        if file_path:
            try:
                with open(file_path, 'w') as file:
                    file.write(password)
                messagebox.showinfo("Success", "Password saved successfully.")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save password: {e}")

# Create tkinter window
window = tk.Tk()

# Create instance of the PasswordGenerator class
app = PasswordGenerator(window)

# Run the tkinter main loop
window.mainloop()
