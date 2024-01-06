import tkinter as tk
from tkinter import ttk, messagebox
import random
import string
import pyperclip

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")

        self.length_label = ttk.Label(root, text="Password Length:")
        self.length_entry = ttk.Entry(root, width=5)
        self.include_digits_var = tk.IntVar()
        self.include_special_chars_var = tk.IntVar()
        self.include_digits_checkbox = ttk.Checkbutton(root, text="Include Digits", variable=self.include_digits_var)
        self.include_special_chars_checkbox = ttk.Checkbutton(root, text="Include Special Characters", variable=self.include_special_chars_var)
        self.generate_button = ttk.Button(root, text="Generate Password", command=self.generate_password)
        self.copy_button = ttk.Button(root, text="Copy to Clipboard", command=self.copy_to_clipboard)
        self.result_label = ttk.Label(root, text="Generated Password:")
        self.result_entry = ttk.Entry(root, state="readonly")

        # Set default values
        self.length_entry.insert(0, "12")
        self.include_digits_var.set(1)
        self.include_special_chars_var.set(1)

        # Grid layout
        self.length_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")
        self.length_entry.grid(row=0, column=1, padx=10, pady=10)
        self.include_digits_checkbox.grid(row=1, column=0, columnspan=2, pady=5, sticky="w")
        self.include_special_chars_checkbox.grid(row=2, column=0, columnspan=2, pady=5, sticky="w")
        self.generate_button.grid(row=3, column=0, columnspan=2, pady=10)
        self.copy_button.grid(row=3, column=2, pady=10, padx=10)
        self.result_label.grid(row=4, column=0, padx=10, pady=10, sticky="e")
        self.result_entry.grid(row=4, column=1, padx=10, pady=10, columnspan=2)

    def generate_password(self):
        try:
            length = int(self.length_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number for password length.")
            return

        include_digits = bool(self.include_digits_var.get())
        include_special_chars = bool(self.include_special_chars_var.get())

        password = self._generate_password(length, include_digits, include_special_chars)

        # Display the generated password
        self.result_entry.config(state="normal")
        self.result_entry.delete(0, "end")
        self.result_entry.insert(0, password)
        self.result_entry.config(state="readonly")

    def _generate_password(self, length, include_digits, include_special_chars):
        lowercase_letters = string.ascii_lowercase
        uppercase_letters = string.ascii_uppercase
        digits = string.digits if include_digits else ""
        special_chars = string.punctuation if include_special_chars else ""
        all_chars = lowercase_letters + uppercase_letters + digits + special_chars
        length = max(length, 8)
        password = random.sample(all_chars, length)
        return ''.join(password)

    def copy_to_clipboard(self):
        password = self.result_entry.get()
        if password:
            pyperclip.copy(password)
            messagebox.showinfo("Success", "Password copied to clipboard!")
        else:
            messagebox.showwarning("Warning", "No password generated to copy!")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
    
