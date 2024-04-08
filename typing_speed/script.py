import tkinter as tk
import random
from time import time

class TypingSpeedTest:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Typing Speed Test")
        self.root.geometry("800x400")
        self.root.configure(bg="blue")

        self.text = tk.StringVar()  # Variable to hold the displayed text
        self.user_input = tk.StringVar()  # Variable to hold user input

        self.create_widgets()
        self.generate_text()  # Generate initial random text to type

    def create_widgets(self):
        self.display_label = tk.Label(self.root, textvariable=self.text, font=("Arial", 20), bg="lightgreen")
        self.display_label.pack(pady=20)

        self.entry_field = tk.Entry(self.root, textvariable=self.user_input, font=("Arial", 16), width=50)
        self.entry_field.pack(pady=10)
        self.entry_field.bind("<Return>", self.check_speed)  # Start test on Enter press

        self.start_button = tk.Button(self.root, text="Start Test", command=self.start_test,bg="lightgreen",fg="black",padx=10,pady=5,font=("Arial",12))
        self.start_button.pack(pady=10)

        self.results_frame = tk.Frame(self.root, bg="lightgreen")
        self.results_frame.pack(pady=20)

        self.time_label = tk.Label(self.results_frame, text="Time: ", font=("Arial", 14), bg="lightgreen")
        self.time_label.pack(side="left", padx=10)

        self.accuracy_label = tk.Label(self.results_frame, text="Accuracy: ", font=("Arial", 14), bg="lightgreen")
        self.accuracy_label.pack(side="right", padx=10)

        self.wpm_label = tk.Label(self.results_frame, text="WPM: ", font=("Arial", 14), bg="lightgreen")
        self.wpm_label.pack(side="left", padx=10)

    def generate_text(self):
        # Replace with your preferred method for generating text (quotes, websites, etc.)
        self.text.set(random.choice([
            "The quick brown fox jumps over the lazy dog.",
            "This is a sample sentence to test your typing speed.",
            "Python is a powerful and versatile programming language."
        ]))

    def start_test(self):
        self.start_time = time()  # Record start time
        self.entry_field.delete(0, tk.END)  # Clear the entry field
        self.disabled_buttons()  # Disable start button during test
        self.user_input.trace("w", self.check_input)  # Track changes in user input

    def check_input(self, *args):
        if len(self.user_input.get()) == len(self.text.get()):
            self.calculate_speed()

    def calculate_speed(self):
        end_time = time()
        elapsed_time = end_time - self.start_time
        words = len(self.text.get().split())  # Count words in the displayed text
        wpm = int((words / elapsed_time) * 60)  # Words per minute calculation

        accuracy = self.calculate_accuracy()

        self.time_label.config(text=f"Time: {elapsed_time:.2f} s")
        self.accuracy_label.config(text=f"Accuracy: {accuracy}%")
        self.wpm_label.config(text=f"WPM: {wpm}")
        self.enabled_buttons()  # Re-enable start button after test

    def calculate_accuracy(self):
        typed_text = self.user_input.get()
        original_text = self.text.get()
        typed_words = typed_text.split()
        original_words = original_text.split()
        correct_words = sum(1 for typed, original in zip(typed_words, original_words) if typed == original)
        total_words = len(original_words)
        accuracy = (correct_words / total_words) * 100
        return round(accuracy, 2)

    def disabled_buttons(self):
        self.start_button.config(state=tk.DISABLED)
        self.time_label.config(text="Time:")
        self.accuracy_label.config(text="Accuracy:")
        self.wpm_label.config(text="WPM:")
    def enabled_buttons(self):
        self.start_button.config(state=tk.NORMAL)
        


    def check_speed(self, event):
        if len(self.user_input.get()) == len(self.text.get()):
            self.calculate_speed()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = TypingSpeedTest()
    app.run()
