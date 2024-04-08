import tkinter as tk


class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Simple Calculator")

        # Initialize display and calculation variables
        self.expression = ""
        self.display_var = tk.StringVar()

        self.create_widgets()
        self.display_var.set("")

    def create_widgets(self):
        # Entry field for displaying the expression
        self.display_entry = tk.Entry(
            self.master, textvariable=self.display_var, width=30, borderwidth=5
        )
        self.display_entry.grid(row=0, columnspan=4, padx=10, pady=10)

        # Button functions for each number and operator
        button_7 = self.create_button(7, command=lambda: self.press(7))
        button_7.grid(row=1, column=0)
        button_8 = self.create_button(8, command=lambda: self.press(8))
        button_8.grid(row=1, column=1)
        button_9 = self.create_button(9, command=lambda: self.press(9))
        button_9.grid(row=1, column=2)
        button_div = self.create_button("/", command=lambda: self.press("/"))
        button_div.grid(row=1, column=3)

        button_4 = self.create_button(4, command=lambda: self.press(4))
        button_4.grid(row=2, column=0)
        button_5 = self.create_button(5, command=lambda: self.press(5))
        button_5.grid(row=2, column=1)
        button_6 = self.create_button(6, command=lambda: self.press(6))
        button_6.grid(row=2, column=2)
        button_mul = self.create_button("*", command=lambda: self.press("*"))
        button_mul.grid(row=2, column=3)

        button_1 = self.create_button(1, command=lambda: self.press(1))
        button_1.grid(row=3, column=0)
        button_2 = self.create_button(2, command=lambda: self.press(2))
        button_2.grid(row=3, column=1)
        button_3 = self.create_button(3, command=lambda: self.press(3))
        button_3.grid(row=3, column=2)
        button_sub = self.create_button("-", command=lambda: self.press("-"))
        button_sub.grid(row=3, column=3)

        button_0 = self.create_button(0, command=lambda: self.press(0))
        button_0.grid(row=4, column=0)
        button_dot = self.create_button(".", command=lambda: self.press("."))
        button_dot.grid(row=4, column=1)
        button_clear = self.create_button("C", command=self.clear)
        button_clear.grid(row=4, column=2)
        button_equal = self.create_button("=", command=self.calculate)
        button_equal.grid(row=4, column=3)

    def create_button(self, text, command):
        # Create a button with consistent style
        return tk.Button(self.master, text=text, width=5, command=command)

    def press(self, char):
        # Update expression and display
        self.expression += str(char)
        self.display_var.set(self.expression)

    def clear(self):
        # Clear expression and display
        self.expression = ""
        self.display_var.set("")

    def calculate(self):
        # Try-except block for handling potential errors
        try:
            result = eval(self.expression)
            self.expression = str(result)
            self.display_var.set(self.expression)
        except:
            self.display_var.set("Error")


root = tk.Tk()
calc = Calculator(root)
root.mainloop()
