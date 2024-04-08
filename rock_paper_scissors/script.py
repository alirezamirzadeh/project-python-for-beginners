# class Person:
#     count = 0 # class variabel
#     def __init__(self,name,age):
#         self.name =name  # object variable
#         self.age =age
#         Person.count +=1
#     def get_name(self):
#         print(self.name)
#     def get_info(self):
#         print(self.name,self.age)
#     def return_count(self):
#         return (Person.count)
    
# class Student(Person):
#     pass
    
# ali = Person('ali',12)
# ali.get_name()
# ali.get_info()

# mamad = Person("mohammad",23)

# reza = Student("reza",19)

# print(ali.return_count())


import tkinter as tk
from random import choice

# Define options for the game
options = ["rock", "paper", "scissors"]


class RockPaperScissors:
    def __init__(self, master):
        self.master = master
        master.title("Rock Paper Scissors")

        self.user_choice = tk.StringVar()
        self.computer_choice = tk.StringVar()
        self.result = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        # Label for user choice
        user_choice_label = tk.Label(
            self.master, text="Your Choice:", font=("Arial", 12)
        )
        user_choice_label.pack(pady=10)

        # Buttons for user selection
        rock_button = tk.Button(
            self.master,
            text="Rock",
            font=("Arial", 12),
            command=lambda: self.user_select("rock"),
        )
        rock_button.pack(padx=10, pady=5)

        paper_button = tk.Button(
            self.master,
            text="Paper",
            font=("Arial", 12),
            command=lambda: self.user_select("paper"),
        )
        paper_button.pack(padx=10, pady=5)

        scissors_button = tk.Button(
            self.master,
            text="Scissors",
            font=("Arial", 12),
            command=lambda: self.user_select("scissors"),
        )
        scissors_button.pack(padx=10, pady=5)

        # Label for computer choice
        computer_choice_label = tk.Label(
            self.master, text="Computer's Choice:", font=("Arial", 12)
        )
        computer_choice_label.pack(pady=10)

        # Label to display computer's choice
        self.computer_choice_label = tk.Label(
            self.master, textvariable=self.computer_choice, font=("Arial", 12)
        )
        self.computer_choice_label.pack()

        # Label to display result
        self.result_label = tk.Label(self.master, textvariable=self.result, font=("Arial", 12))
        self.result_label.pack(pady=10)

        # Button to play again
        play_again_button = tk.Button(
            self.master, text="Play Again", font=("Arial", 12), command=self.play_again
        )
        play_again_button.pack(pady=10)

    def user_select(self, choice):
        self.user_choice.set(choice)
        self.computer_select()

    def computer_select(self):
        self.computer_choice.set(choice(options))
        self.check_winner()

    def check_winner(self):
        user_choice = self.user_choice.get()
        computer_choice = self.computer_choice.get()

        if user_choice == computer_choice:
            self.result.set("It's a Tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or (
            user_choice == "paper" and computer_choice == "rock"
        ) or (user_choice == "scissors" and computer_choice == "paper"):
            self.result.set("You Win!")
        else:
            self.result.set("You Lose!")

    def play_again(self):
        self.user_choice.set("")
        self.computer_choice.set("")
        self.result.set("")


root = tk.Tk()
game = RockPaperScissors(root)
root.mainloop()

