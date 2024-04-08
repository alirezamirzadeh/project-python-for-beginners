import tkinter as tk
from tkinter import messagebox
import mysql.connector

class DatabaseManager:
    def __init__(self):
        self.db = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="aLIREZA22!",
            database="products_managment"
        )
        self.cursor = self.db.cursor()

    def register_user(self, username, email, password):
        self.cursor.execute("INSERT INTO users (username, email, password) VALUES (%s, %s, %s)", (username, email, password))
        self.db.commit()

    def login_user(self, username, password):
        self.cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
        return self.cursor.fetchone()

    def add_product(self, id, name, price, size, brand, year, weight, category):
        self.cursor.execute("INSERT INTO products (id, name, price, size, brand, year, weight, category) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (id, name, price, size, brand, year, weight, category))
        self.db.commit()

    def get_products(self):
        self.cursor.execute("SELECT * FROM products")
        return self.cursor.fetchall()

    def update_product(self, id, name, price, size, brand, year, weight, category):
        self.cursor.execute("""UPDATE products SET name=%s, price=%s, size=%s, brand=%s, year=%s, weight=%s, category=%s WHERE id=%s""" , (name, price, size, brand, year, weight, category,id))
        self.db.commit()
        print("update",id, name, price, size, brand, year, weight, category)

    def delete_product(self, id):
        self.cursor.execute("DELETE FROM products WHERE id=%s", (id,))
        self.db.commit()

class RegisterPage(tk.Frame):
    def __init__(self, master, db, show_login_page):
        super().__init__(master)
        self.db = db
        self.show_login_page = show_login_page
        self.create_widgets()

    def create_widgets(self):
        self.username_label = tk.Label(self, text="Username:")
        self.username_label.grid(row=0, column=0)

        self.username_entry = tk.Entry(self)
        self.username_entry.grid(row=0, column=1)

        self.email_label = tk.Label(self, text="Email:")
        self.email_label.grid(row=1, column=0)

        self.email_entry = tk.Entry(self)
        self.email_entry.grid(row=1, column=1)

        self.password_label = tk.Label(self, text="Password:")
        self.password_label.grid(row=2, column=0)

        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.grid(row=2, column=1)

        self.repeat_password_label = tk.Label(self, text="Repeat Password:")
        self.repeat_password_label.grid(row=3, column=0)

        self.repeat_password_entry = tk.Entry(self, show="*")
        self.repeat_password_entry.grid(row=3, column=1)

        self.register_button = tk.Button(self, text="Register", command=self.register)
        self.register_button.grid(row=4, columnspan=2)

        self.status_label = tk.Label(self, text="")
        self.status_label.grid(row=5, columnspan=2)

        self.login_button = tk.Button(self, text="Go to Login", command=self.go_to_login)
        self.login_button.grid(row=6, columnspan=2)

    def go_to_login(self):
        self.pack_forget()
        self.show_login_page()

    def register(self):
        username = self.username_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()
        repeat_password = self.repeat_password_entry.get()
        
        if password == repeat_password:
            self.db.register_user(username, email, password)
            self.status_label.config(text="Registration successful", fg="green")
            self.go_to_login()
        else:
            self.status_label.config(text="Passwords do not match", fg="red")


class LoginPage(tk.Frame):
    def __init__(self, master, db, show_product_page):
        super().__init__(master)
        self.db = db
        self.show_product_page = show_product_page
        self.create_widgets()

    def create_widgets(self):
        self.username_label = tk.Label(self, text="Username:")
        self.username_label.grid(row=0, column=0)

        self.username_entry = tk.Entry(self)
        self.username_entry.grid(row=0, column=1)

        self.password_label = tk.Label(self, text="Password:")
        self.password_label.grid(row=1, column=0)

        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.grid(row=1, column=1)

        self.login_button = tk.Button(self, text="Login", command=self.login)
        self.login_button.grid(row=2, columnspan=2)

        self.status_label = tk.Label(self, text="")
        self.status_label.grid(row=3, columnspan=2)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        user = self.db.login_user(username, password)
        if user:
            self.show_product_page()
        else:
            self.status_label.config(text="Invalid username or password", fg="red")

class ProductPage(tk.Frame):
    def __init__(self, master, db):
        super().__init__(master)
        self.db = db
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Product Management", font=("Helvetica", 16)).grid(row=0, column=0, columnspan=2, pady=10)
        
        # Add Product Section
        tk.Label(self, text="Add Product", font=("Helvetica", 12)).grid(row=1, column=0, columnspan=2, pady=5)
        fields = ["ID:","Name:", "Price:", "Size:", "Brand:", "Year:", "Weight:", "Category:"]
        self.entry_widgets = {}
        for i, field in enumerate(fields):
            tk.Label(self, text=field).grid(row=i+2, column=0, sticky='e', pady=2)
            entry = tk.Entry(self, width=30)
            entry.grid(row=i+2, column=1, pady=2)
            self.entry_widgets[field.lower()] = entry
        self.add_button = tk.Button(self, text="Add Product", command=self.add_product)
        self.add_button.grid(row=len(fields)+2, columnspan=2, pady=5)

        # Show Products Section
        tk.Label(self, text="Products", font=("Helvetica", 12)).grid(row=len(fields)+3, column=0, columnspan=2, pady=5)
        self.products_listbox = tk.Listbox(self, width=60, height=15)
        self.products_listbox.grid(row=len(fields)+4, column=0, columnspan=2)
        self.update_button = tk.Button(self, text="Update Product", command=self.update_product)
        self.update_button.grid(row=len(fields)+5, column=0, columnspan=2, pady=5)
        self.delete_button = tk.Button(self, text="Delete Product", command=self.delete_product)
        self.delete_button.grid(row=len(fields)+6, column=0, columnspan=2, pady=5)

        self.products_listbox.bind("<Double-Button-1>", self.populate_entry_fields)

        self.show_products()

    def add_product(self):
        values = [entry.get() for entry in self.entry_widgets.values()]
        id, name, price, size, brand, year, weight, category = values
        self.db.add_product(id, name, price, size, brand, year, weight, category)
        self.show_products()

    def show_products(self):
        self.products_listbox.delete(0, tk.END)
        products = self.db.get_products()
        if products:
            for product in products:
                self.products_listbox.insert(tk.END, product)
        else:
            self.products_listbox.insert(tk.END, "No products found")

    def update_product(self):
        selected_index = self.products_listbox.curselection()
        if selected_index:
            values = [entry.get() for entry in self.entry_widgets.values()]
            self.db.update_product(*values)
            self.show_products()
        else:
            tk.messagebox.showinfo("Update Product", "Please select a product to update.")

    def delete_product(self):
        products = self.db.get_products()
        selected_index = self.products_listbox.curselection()
        if selected_index:
            selected_product = self.products_listbox.get(selected_index)
            confirmation = messagebox.askyesno("Delete Product", f"Are you sure you want to delete {selected_product}?")
            if confirmation:
                product_id = products[selected_index[0]][0]
                self.db.delete_product(product_id)
                self.show_products()
        else:
            tk.messagebox.showinfo("Delete Product", "Please select a product to delete.")

    def populate_entry_fields(self, event):
        selected_index = self.products_listbox.curselection()
        if selected_index:
            selected_product = self.products_listbox.get(selected_index)
            for field, entry in self.entry_widgets.items():
                entry.delete(0, tk.END)
                entry.insert(tk.END, selected_product[list(self.entry_widgets.keys()).index(field)])
        else:
            tk.messagebox.showinfo("Select Product", "Please select a product to populate entry fields.")

class ProductManagementApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Product Management")
        self.geometry("600x400")

        self.db = DatabaseManager()

        self.register_page = RegisterPage(self, self.db, self.show_login_page)
        self.login_page = LoginPage(self, self.db, self.show_product_page)
        self.product_page = ProductPage(self, self.db)

        self.show_register_page()

    def show_register_page(self):
        self.login_page.pack_forget()
        self.product_page.pack_forget()
        self.register_page.pack()

    def show_login_page(self):
        self.register_page.pack_forget()
        self.product_page.pack_forget()
        self.login_page.pack()

    def show_product_page(self):
        self.register_page.pack_forget()
        self.login_page.pack_forget()
        self.product_page.pack()

if __name__ == "__main__":
    app = ProductManagementApp()
    app.mainloop()
