import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissorsGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Rock Paper Scissors Game")
        self.master.configure(bg="#f0f0f0")
        self.master.geometry("500x500")  # Adjusted for extra space

        self.user_score = 0
        self.computer_score = 0

        # Header Label
        self.header_label = tk.Label(self.master, text="Rock Paper Scissors", font=("Arial", 24, 'bold'), bg="#f0f0f0")
        self.header_label.pack(pady=10)

        # Choice Label
        self.label = tk.Label(self.master, text="Choose your move:", font=("Arial", 18), bg="#f0f0f0")
        self.label.pack(pady=10)

        # Buttons
        button_font = ("Arial", 16)
        self.rock_btn = tk.Button(self.master, text="Rock", width=12, height=2, command=lambda: self.player_choice('rock'), bg="#4CAF50", fg="white", font=button_font, relief='raised', bd=3)
        self.rock_btn.pack(pady=10)

        self.paper_btn = tk.Button(self.master, text="Paper", width=12, height=2, command=lambda: self.player_choice('paper'), bg="#2196F3", fg="white", font=button_font, relief='raised', bd=3)
        self.paper_btn.pack(pady=10)

        self.scissors_btn = tk.Button(self.master, text="Scissors", width=12, height=2, command=lambda: self.player_choice('scissors'), bg="#FFC107", fg="white", font=button_font, relief='raised', bd=3)
        self.scissors_btn.pack(pady=10)

        # Score Label
        self.score_label = tk.Label(self.master, text=f"You: {self.user_score} | Computer: {self.computer_score}", font=("Arial", 20), bg="#f0f0f0")
        self.score_label.pack(pady=20)

        # Game History Label
        self.history_label = tk.Label(self.master, text="Game History:", font=("Arial", 16, 'bold'), bg="#f0f0f0")
        self.history_label.pack(pady=10)

        # Game History Listbox
        self.history_listbox = tk.Listbox(self.master, width=50, height=10, font=("Arial", 12))
        self.history_listbox.pack(pady=10)

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
        else:
            return outcomes.get((user_choice, computer_choice), outcomes.get((computer_choice, user_choice)))

    def player_choice(self, player_pick):
        choices = ['rock', 'paper', 'scissors']
        computer_pick = random.choice(choices)
        result = self.determine_winner(player_pick, computer_pick)
        messagebox.showinfo("Result", f"Computer picked {computer_pick}. {result}")

        if result == 'You win!':
            self.user_score += 1
            self.update_scores()
            self.highlight_button(player_pick, '#4CAF50')
        elif result == 'Computer wins!':
            self.computer_score += 1
            self.update_scores()
            self.highlight_button(player_pick, '#F44336')
        else:
            self.highlight_button(player_pick, '#FFC107')
            self.highlight_button(computer_pick, '#FFC107')

        # Add result to game history
        self.history_listbox.insert(tk.END, f"You: {player_pick} | Computer: {computer_pick} | Result: {result}")

    def update_scores(self):
        self.score_label.config(text=f"You: {self.user_score} | Computer: {self.computer_score}")

    def highlight_button(self, choice, color):
        if choice == 'rock':
            self.rock_btn.config(bg=color)
            self.master.after(1000, lambda: self.rock_btn.config(bg="#4CAF50"))
        elif choice == 'paper':
            self.paper_btn.config(bg=color)
            self.master.after(1000, lambda: self.paper_btn.config(bg="#2196F3"))
        elif choice == 'scissors':
            self.scissors_btn.config(bg=color)
            self.master.after(1000, lambda: self.scissors_btn.config(bg="#FFC107"))

# Create tkinter window
window = tk.Tk()

# Create instance of the game
game = RockPaperScissorsGame(window)

# Run the tkinter main loop
window.mainloop()
