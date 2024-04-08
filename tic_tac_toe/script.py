import tkinter as tk
from tkinter import messagebox
import random

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")

        self.current_player = "X"
        self.board = [" "]*9

        self.buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                btn = tk.Button(root, text="", font=('Helvetica', 24), width=6, height=3,
                                command=lambda i=i, j=j: self.make_move(i, j))
                btn.grid(row=i, column=j, sticky="nsew")
                row.append(btn)
            self.buttons.append(row)

        self.mode = tk.StringVar(value="1player")
        mode_selector = tk.OptionMenu(root, self.mode, "1player", "2player", command=self.restart_game)
        mode_selector.grid(row=3, column=1, columnspan=2, sticky="ew")

    def make_move(self, i, j):
        if self.board[i*3 + j] == " ":
            self.board[i*3 + j] = self.current_player
            self.buttons[i][j].config(text=self.current_player, state="disabled")

            if self.check_winner():
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.restart_game()
            elif " " not in self.board:
                messagebox.showinfo("Game Over", "It's a tie!")
                self.restart_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                if self.mode.get() == "1player" and self.current_player == "O":
                    self.computer_move()

    def computer_move(self):
        empty_cells = [i for i in range(9) if self.board[i] == " "]
        selected_cell = random.choice(empty_cells)
        self.make_move(selected_cell // 3, selected_cell % 3)

    def check_winner(self):
        for i in range(3):
            if self.board[i] == self.board[i+3] == self.board[i+6] != " ":
                return True
            if self.board[i*3] == self.board[i*3+1] == self.board[i*3+2] != " ":
                return True
        if self.board[0] == self.board[4] == self.board[8] != " ":
            return True
        if self.board[2] == self.board[4] == self.board[6] != " ":
            return True
        return False

    def restart_game(self, *args):
        self.current_player = "X"
        self.board = [" "]*9
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text="", state="normal")

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
