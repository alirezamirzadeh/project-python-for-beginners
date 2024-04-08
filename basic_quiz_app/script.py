import tkinter as tk
from tkinter import messagebox

class QuizApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Basic Quiz App")
        self.geometry("400x350")
        self.current_question = 0
        self.score = 0
        self.questions = [
            {"question": "What is the capital of France?",
             "options": ["Paris", "London", "Berlin", "Rome"],
             "answer": "Paris"},
            {"question": "What is 2 + 2?",
             "options": ["3", "4", "5", "6"],
             "answer": "4"},
            {"question": "What is the largest mammal?",
             "options": ["Elephant", "Whale", "Giraffe", "Rhino"],
             "answer": "Whale"},
            {"question": "What is the chemical symbol for water?",
             "options": ["H2O", "CO2", "NaCl", "O2"],
             "answer": "H2O"},
            {"question": "Which planet is known as the Red Planet?",
             "options": ["Earth", "Venus", "Mars", "Jupiter"],
             "answer": "Mars"},
            {"question": "Who wrote 'Romeo and Juliet'?",
             "options": ["William Shakespeare", "Charles Dickens", "Jane Austen", "Leo Tolstoy"],
             "answer": "William Shakespeare"},
            {"question": "What is the chemical symbol for gold?",
             "options": ["Au", "Ag", "Fe", "Pb"],
             "answer": "Au"},
            {"question": "What is the tallest mountain in the world?",
             "options": ["Mount Everest", "K2", "Kangchenjunga", "Lhotse"],
             "answer": "Mount Everest"},
            {"question": "What is the main ingredient in guacamole?",
             "options": ["Tomato", "Avocado", "Onion", "Lime"],
             "answer": "Avocado"},
            {"question": "Which country is home to the kangaroo?",
             "options": ["Australia", "Brazil", "India", "South Africa"],
             "answer": "Australia"}
        ]
        
        self.create_widgets()
        self.display_question()
        
        
    def create_widgets(self):
        self.question_label = tk.Label(self, text="", font=("Helvetica", 12))
        self.question_label.pack(pady=10)
        self.option_vars = []
        self.btn = []
        for i in range(4):
            var = tk.StringVar()
            option = tk.Radiobutton(self, text="", variable=var, value="", font=("Helvetica", 10),)
            option.pack(anchor=tk.W)
            self.option_vars.append(var)
            self.btn.append(option)
        
        self.submit_button = tk.Button(self, text="Submit", command=self.check_answer)
        self.submit_button.pack(pady=10)
        
        self.answer_label = tk.Label(self, text="")
        self.answer_label.pack()
        
        self.score_label = tk.Label(self, text="")
        self.score_label.pack()
        
    def display_question(self):
        if self.current_question < len(self.questions):
            question_data = self.questions[self.current_question]
            self.question_label.config(text=question_data["question"])
            for i in range(4):
                self.option_vars[i].set(question_data["options"][i])
                self.btn[i].config(text=question_data["options"][i])
        else:
            self.question_label.config(text="Quiz Completed!")
            self.submit_button.config(state=tk.DISABLED)
            messagebox.showinfo("Result", f"Your score: {self.score}/100")
        
    def check_answer(self):
        selected_options = []
        for i, var in enumerate(self.option_vars):
            if var.get():
                selected_options.append(self.option_vars[i].get())

        if not selected_options:
            messagebox.showerror("Error", "Please select an answer.")
            return

        correct_answer = self.questions[self.current_question]["answer"]

        is_correct = any(option == correct_answer for option in selected_options)
        self.display_correct_answer(correct_answer)

        if is_correct == False:
            self.score += 10
        self.current_question += 1
        self.display_question()

    def display_correct_answer(self, correct_answer):
        self.answer_label.config(text=f"Correct answer: {correct_answer}")

if __name__ == "__main__":
    app = QuizApp()
    app.mainloop()
