import tkinter as tk
from random import randint

# my numbert in my brain => 67

class GuessingGame:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Guessing Game (Computer Guesses)")

        self.x = 2
        self.y = 100
        self.guess = 50
        self.computer_number = randint(self.x, self.y)

        self.user_feedback = tk.StringVar()

        self.feedback_label = tk.Label(
            self.window, textvariable=self.user_feedback
        )
        self.feedback_label.pack()

        self.lower_button = tk.Button(
            self.window, text="Lower (l)", command=self.user_said_lower
        )
        self.lower_button.pack()

        self.higher_button = tk.Button(
            self.window, text="Higher (h)", command=self.user_said_higher
        )
        self.higher_button.pack()

        self.correct_button = tk.Button(
            self.window, text="Correct (c)", command=self.user_said_correct
        )
        self.correct_button.pack()
        
        self.reset_button = tk.Button(
            self.window, text="reset", command=self.reset_game , state="disabled"
        )
        self.reset_button.pack()

        self.guess_computer_number()  # Start the guessing process

        self.window.mainloop()

    def reset_game(self):
        self.x = 0
        self.y = 100
        self.computer_number = randint(self.x, self.y)
        self.guess = 50  # Reset guess counter
        self.user_feedback.set(f"Is your number 50 (l/h/c)?")
        self.lower_button.config(state="active")
        self.higher_button.config(state="active")
        self.correct_button.config(state="active")
        self.reset_button.config(state="disabled")

        
    def guess_computer_number(self):
        self.guess = int((self.x + self.y) / 2)
        self.user_feedback.set(f"Is your number {self.guess} (l/h/c)?")

    def user_said_lower(self):
        self.y = self.guess - 1
        self.guess_computer_number()

    def user_said_higher(self):
        self.x = self.guess + 1
        self.guess_computer_number()

    def user_said_correct(self):
        self.user_feedback.set(f"Yes! I guessed your number in {self.guess} tries!")
        self.lower_button.config(state="disabled")
        self.higher_button.config(state="disabled")
        self.correct_button.config(state="disabled")
        self.reset_button.config(state="active")


if __name__ == "__main__":
    game = GuessingGame()
