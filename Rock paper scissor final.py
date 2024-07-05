import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissorsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock-Paper-Scissors Game")
        self.root.geometry("400x300")
        self.root.configure(bg='#1e1e1e')

        self.user_score = 0
        self.computer_score = 0

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.root, text="Choose Rock, Paper, or Scissors", font=("Arial", 14), bg='#1e1e1e', fg='white')
        self.label.pack(pady=20)

        frame = tk.Frame(self.root, bg='#333333')
        frame.pack(pady=10)

        button_style = {'font': ("Arial", 12), 'bg': 'black', 'fg': 'white', 'width': 10, 'height': 2}

        self.rock_button = tk.Button(frame, text="Rock", command=lambda: self.play_game("Rock"), **button_style)
        self.rock_button.pack(side=tk.LEFT, padx=10)

        self.paper_button = tk.Button(frame, text="Paper", command=lambda: self.play_game("Paper"), **button_style)
        self.paper_button.pack(side=tk.LEFT, padx=10)

        self.scissors_button = tk.Button(frame, text="Scissors", command=lambda: self.play_game("Scissors"), **button_style)
        self.scissors_button.pack(side=tk.LEFT, padx=10)

        self.result_label = tk.Label(self.root, text="", font=("Arial", 12), bg='#1e1e1e', fg='white')
        self.result_label.pack(pady=20)

        self.score_label = tk.Label(self.root, text="User - 0 / 0 - Computer", font=("Arial", 12), bg='#1e1e1e', fg='white')
        self.score_label.pack(pady=20)

    def play_game(self, user_choice):
        computer_choice = random.choice(["Rock", "Paper", "Scissors"])
        result = self.determine_winner(user_choice, computer_choice)

        self.result_label.config(text=f"User chose: {user_choice}, Computer chose: {computer_choice}\n{result}")
        self.score_label.config(text=f"User - {self.user_score} / {self.computer_score} - Computer")

        play_again = messagebox.askyesno("Play Again", "Do you want to play another round?")
        if not play_again:
            self.root.quit()

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "It's a tie!"

        if (user_choice == "Rock" and computer_choice == "Scissors") or \
           (user_choice == "Paper" and computer_choice == "Rock") or \
           (user_choice == "Scissors" and computer_choice == "Paper"):
            self.user_score += 1
            return "You win!"
        else:
            self.computer_score += 1
            return "You lose!"

if __name__ == "__main__":
    root = tk.Tk()
    game = RockPaperScissorsGame(root)
    root.mainloop()
