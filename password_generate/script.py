import random
import string
import tkinter as tk

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")

        self.setup_ui()

    def setup_ui(self):
        # Password length label and entry
        self.password_length_label = tk.Label(self.root, text="Password Length:")
        self.password_length_label.grid(row=0, column=0, padx=10, pady=5)

        self.password_length_entry = tk.Entry(self.root, width=10)
        self.password_length_entry.insert(0, "12")  # Set default length
        self.password_length_entry.grid(row=0, column=1, padx=10, pady=5)

        # Character set checkboxes
        self.include_uppercase_var = tk.IntVar(value=1)  # Default checked
        self.include_uppercase_checkbox = tk.Checkbutton(self.root, text="Include Uppercase Letters", variable=self.include_uppercase_var)
        self.include_uppercase_checkbox.grid(row=1, column=0, columnspan=2, padx=10, pady=5, sticky=tk.W)

        self.include_lowercase_var = tk.IntVar(value=1)  # Default checked
        self.include_lowercase_checkbox = tk.Checkbutton(self.root, text="Include Lowercase Letters", variable=self.include_lowercase_var)
        self.include_lowercase_checkbox.grid(row=2, column=0, columnspan=2, padx=10, pady=5, sticky=tk.W)

        self.include_digits_var = tk.IntVar(value=1)  # Default checked
        self.include_digits_checkbox = tk.Checkbutton(self.root, text="Include Digits", variable=self.include_digits_var)
        self.include_digits_checkbox.grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky=tk.W)

        self.include_symbols_var = tk.IntVar()  # Default unchecked
        self.include_symbols_checkbox = tk.Checkbutton(self.root, text="Include Symbols", variable=self.include_symbols_var)
        self.include_symbols_checkbox.grid(row=4, column=0, columnspan=2, padx=10, pady=5, sticky=tk.W)

        # Generate password button
        self.generate_button = tk.Button(self.root, text="Generate Password", command=self.generate_password)
        self.generate_button.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

        # Password display label and entry
        self.password_label = tk.Label(self.root, text="Generated Password:")
        self.password_label.grid(row=6, column=0, padx=10, pady=5, sticky=tk.W)

        self.password_entry = tk.Entry(self.root, width=30)
        self.password_entry.grid(row=6, column=1, padx=10, pady=5, sticky=tk.W)

        # Copy to clipboard button
        self.copy_button = tk.Button(self.root, text="Copy to Clipboard", command=self.copy_to_clipboard)
        self.copy_button.grid(row=7, column=0, columnspan=2, padx=10, pady=5)

    def generate_password(self):
        length = self.password_length_entry.get()
        include_uppercase = self.include_uppercase_var.get()
        include_lowercase = self.include_lowercase_var.get()
        include_digits = self.include_digits_var.get()
        include_symbols = self.include_symbols_var.get()

        try:
            length = int(length)
            if length <= 0:
                raise ValueError
        except ValueError:
            self.password_entry.delete(0, tk.END)
            self.password_entry.insert(0, "Invalid length. Please enter a positive integer.")
            return

        try:
            password = self.generate_password_helper(length, include_uppercase, include_lowercase, include_digits, include_symbols)
        except ValueError as e:
            self.password_entry.delete(0, tk.END)
            self.password_entry.insert(0, str(e))
            return

        self.password_entry.delete(0, tk.END)
        self.password_entry.insert(0, password)

    def generate_password_helper(self, length, include_uppercase, include_lowercase, include_digits, include_symbols):
        characters = ""
        if include_uppercase:
            characters += string.ascii_uppercase
        if include_lowercase:
            characters += string.ascii_lowercase
        if include_digits:
            characters += string.digits
        if include_symbols:
            characters += string.punctuation

        # Raise error if no character sets are selected
        if not characters:
            raise ValueError("Please select at least one character set for password generation.")

        # Generate random password
        password = ''.join(random.choice(characters) for i in range(length))
        return password

    def copy_to_clipboard(self):
        self.root.clipboard_clear()
        self.root.clipboard_append(self.password_entry.get())
        self.password_entry.delete(0, tk.END)
        self.password_entry.insert(0, "Password copied!")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
