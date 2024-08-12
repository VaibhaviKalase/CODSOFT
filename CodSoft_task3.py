# Task 3 :- Password Generator
import tkinter as tk
import random
import string
from tkinter import messagebox

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Enhanced Password Generator")
        self.root.geometry("400x400")
        self.root.configure(bg="#2C3E50")

        # Custom Fonts and Colors
        self.label_font = ("Helvetica", 12, "bold")
        self.entry_font = ("Helvetica", 12)
        self.button_font = ("Helvetica", 12, "bold")
        self.button_color = "#2980B9"
        self.button_hover_color = "#3498DB"
        self.text_color = "#ECF0F1"

        # Password Length
        self.length_label = tk.Label(root, text="Password Length:", font=self.label_font, bg="#2C3E50", fg=self.text_color)
        self.length_label.pack(pady=10)

        self.length_entry = tk.Entry(root, font=self.entry_font, width=10, justify='center')
        self.length_entry.pack(pady=5)

        # Options for password strength
        self.include_uppercase = tk.BooleanVar(value=True)
        self.include_digits = tk.BooleanVar(value=True)
        self.include_special = tk.BooleanVar(value=True)

        self.uppercase_check = tk.Checkbutton(root, text="Include Uppercase Letters", variable=self.include_uppercase,
                                              font=self.label_font, bg="#2C3E50", fg=self.text_color, selectcolor="#34495E")
        self.uppercase_check.pack(pady=5)

        self.digits_check = tk.Checkbutton(root, text="Include Digits", variable=self.include_digits,
                                           font=self.label_font, bg="#2C3E50", fg=self.text_color, selectcolor="#34495E")
        self.digits_check.pack(pady=5)

        self.special_check = tk.Checkbutton(root, text="Include Special Characters", variable=self.include_special,
                                            font=self.label_font, bg="#2C3E50", fg=self.text_color, selectcolor="#34495E")
        self.special_check.pack(pady=5)

        # Generate Password Button
        self.generate_button = tk.Button(root, text="Generate Password", font=self.button_font, bg=self.button_color,
                                         fg=self.text_color, command=self.generate_password, activebackground=self.button_hover_color)
        self.generate_button.pack(pady=20)

        # Display Generated Password
        self.password_label = tk.Label(root, text="", font=self.label_font, bg="#2C3E50", fg=self.text_color)
        self.password_label.pack(pady=10)

        # Copy to Clipboard Button
        self.copy_button = tk.Button(root, text="Copy to Clipboard", font=self.button_font, bg=self.button_color,
                                     fg=self.text_color, command=self.copy_to_clipboard, activebackground=self.button_hover_color)
        self.copy_button.pack(pady=10)

    def generate_password(self):
        try:
            password_length = int(self.length_entry.get())
            if password_length <= 0:
                raise ValueError("Password length must be greater than 0")

            password = self.generate_random_password(password_length)
            self.password_label.config(text="Generated Password: " + password)
        except ValueError as e:
            messagebox.showerror("Invalid Input", str(e))

    def generate_random_password(self, length):
        characters = string.ascii_lowercase
        if self.include_uppercase.get():
            characters += string.ascii_uppercase
        if self.include_digits.get():
            characters += string.digits
        if self.include_special.get():
            characters += string.punctuation

        if not characters:
            messagebox.showerror("Invalid Selection", "No character types selected. Please select at least one option.")
            return ""

        password = ''.join(random.choice(characters) for _ in range(length))
        return password

    def copy_to_clipboard(self):
        password = self.password_label.cget("text").replace("Generated Password: ", "")
        if password:
            self.root.clipboard_clear()
            self.root.clipboard_append(password)
            messagebox.showinfo("Copied", "Password copied to clipboard")
        else:
            messagebox.showwarning("No Password", "Please generate a password first")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
