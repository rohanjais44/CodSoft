import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissorsGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Rock Paper Scissors Game")
        
        self.user_score = 0
        self.computer_score = 0
        
        self.label = tk.Label(self.master, text="Choose your move:", font=("Arial", 22))
        self.label.pack()

        self.rock_btn = tk.Button(self.master, text="Rock", width=10, command=lambda: self.player_choice('rock'), bg="light blue", font=("Arial", 18))
        self.rock_btn.pack(pady=5)

        self.paper_btn = tk.Button(self.master, text="Paper", width=10, command=lambda: self.player_choice('paper'), bg="light green", font=("Arial", 18))
        self.paper_btn.pack(pady=5)

        self.scissors_btn = tk.Button(self.master, text="Scissors", width=10, command=lambda: self.player_choice('scissors'), bg="light pink", font=("Arial", 18))
        self.scissors_btn.pack(pady=5)

        self.score_label = tk.Label(self.master, text=f"You: {self.user_score} | Computer: {self.computer_score}", font=("Arial", 20))
        self.score_label.pack()

    def determine_winner(self, user_choice, computer_choice):
        outcomes = {
            ('rock', 'paper'): 'Computer wins!',
            ('rock', 'scissors'): 'You win!',
            ('paper', 'rock'): 'You win!',
            ('paper', 'scissors'): 'Computer wins!',
            ('scissors', 'rock'): 'Computer wins!',
            ('scissors', 'paper'): 'You win!',
        }
        if user_choice == computer_choice:
            return "It's a tie!"
        elif (user_choice, computer_choice) in outcomes:
            return outcomes[(user_choice, computer_choice)]
        else:
            return outcomes[(computer_choice, user_choice)]

    def player_choice(self, player_pick):
        choices = ['rock', 'paper', 'scissors']
        computer_pick = random.choice(choices)
        result = self.determine_winner(player_pick, computer_pick)
        messagebox.showinfo("Result", f"Computer picked {computer_pick}. {result}")
        
        if result == 'You win!':
            self.user_score += 1
            self.update_scores()
            self.highlight_button(player_pick, 'green')
        elif result == 'Computer wins!':
            self.computer_score += 1
            self.update_scores()
            self.highlight_button(player_pick, 'red')
        else:
            self.highlight_button(player_pick, 'yellow')
            self.highlight_button(computer_pick, 'yellow')

    def update_scores(self):
        self.score_label.config(text=f"You: {self.user_score} | Computer: {self.computer_score}")

    def highlight_button(self, choice, color):
        if choice == 'rock':
            self.rock_btn.config(bg=color)
            self.master.after(1000, lambda: self.rock_btn.config(bg="light blue"))
        elif choice == 'paper':
            self.paper_btn.config(bg=color)
            self.master.after(1000, lambda: self.paper_btn.config(bg="light green"))
        elif choice == 'scissors':
            self.scissors_btn.config(bg=color)
            self.master.after(1000, lambda: self.scissors_btn.config(bg="light pink"))

# Create tkinter window
window = tk.Tk()

# Create instance of the game
game = RockPaperScissorsGame(window)

# Run the tkinter main loop
window.mainloop()
