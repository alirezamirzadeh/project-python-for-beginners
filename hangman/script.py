import tkinter as tk
from tkinter import messagebox
import random

class HangmanGame:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Hangman Game")
        self.root.geometry("400x400")
        self.root.configure(bg="lightgreen")

        self.words = ["apple", "banana", "orange", "grape", "kiwi", "melon", "peach"]
        self.word_to_guess = random.choice(self.words)
        self.guesses_left = 6
        self.word_display = ["_"] * len(self.word_to_guess)
        self.guessed_letters = set()

        self.create_widgets()

    def create_widgets(self):
        self.title_label = tk.Label(self.root, text="Note, Enter the name of a fruit", font=("Arial", 18))
        self.title_label.pack(pady=10)

        self.word_label = tk.Label(self.root, text=" ".join(self.word_display), font=("Arial", 18))
        self.word_label.pack(pady=20)

        self.guess_label = tk.Label(self.root, text=f"Guesses left: {self.guesses_left}", font=("Arial", 12))
        self.guess_label.pack()

        self.entry = tk.Entry(self.root, font=("Arial", 14))
        self.entry.pack(pady=10)

        self.submit_button = tk.Button(self.root, text="Submit", command=self.check_guess)
        self.submit_button.pack(pady=5)

    def check_guess(self):
        guess = self.entry.get().lower()
        self.entry.delete(0, tk.END)

        if not guess.isalpha():
            messagebox.showwarning("Invalid Input", "Please enter a single letter.")
            return


        self.guessed_letters.add(guess)
        if guess in self.word_to_guess:
            for i, letter in enumerate(self.word_to_guess):
                if letter == guess:
                    self.word_display[i] = guess
            self.word_label.config(text=self.word_label.config(text=" ".join(guess)))
            " ".join(self.word_display)
            messagebox.showinfo("Duplicate Guess", "You have already guessed that letter.")
            self.root.quit()

        else:
            self.guesses_left -= 1
            self.guess_label.config(text=f"Guesses left: {self.guesses_left}")
            if self.guesses_left == 0:
                self.game_over()

        if "_" not in self.word_display:
            self.game_won()

    def game_over(self):
        messagebox.showinfo("Game Over", "You lost! The word was: " + self.word_to_guess)
        self.root.quit()

    def game_won(self):
        messagebox.showinfo("Congratulations", "You won!")
        self.root.quit()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    hangman = HangmanGame()
    hangman.run()
