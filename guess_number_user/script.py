import tkinter as tk
from random import randint


class GuessingGame:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Guessing Game")
        self.window.geometry("280x120")
        self.window.readprofile(False,False)

        self.x = 0
        self.y = 99

        # Store the user_guess widget in a class attribute
        self.user_guess = tk.Entry(self.window)
        self.user_guess.pack()

        self.guess_button = tk.Button(
            self.window, text="Guess", command=self.check_guess
        )
        self.guess_button.pack()

        self.message_label = tk.Label(self.window, text="")
        self.message_label.pack()

        self.restart_button = tk.Button(
            self.window, text="Restart Game", command=self.reset_game, state="disabled"
        )
        self.restart_button.pack()
        self.reset_game()  # Initialize game state


        self.window.mainloop()

    def reset_game(self):
        self.x = 0
        self.y = 99
        self.computer_number = randint(self.x, self.y)
        self.user_guess.delete(0, tk.END)  # Clear the entry widget
        self.message_label.config(text="")
        self.guess_button.config(state="normal")  # Re-enable guess button
        self.restart_button.config(state="disabled")  # Disable restart button

    def check_guess(self):
        # Access the user_guess widget using self.user_guess
        user_number = int(self.user_guess.get())

        if self.computer_number != user_number:
            if self.computer_number > user_number:
                if user_number > self.x:
                    self.x = user_number
                message = "Too low! Guess a number between {} and {}".format(
                    self.x, self.y
                )
            else:
                if user_number < self.y:
                    self.y = user_number
                message = "Too high! Guess a number between {} and {}".format(
                    self.x, self.y
                )
            self.message_label.config(text=message)
        else:
            message = "Yessssss, you guessed it! The number was {}".format(
                self.computer_number
            )
            self.message_label.config(text=message)
            self.guess_button.config(state="disabled")  # Disable guess button
            self.restart_button.config(state="normal")  # Enable restart button

if __name__ == "__main__":
    game = GuessingGame()
