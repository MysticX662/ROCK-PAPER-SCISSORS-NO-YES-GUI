import tkinter as tk
import random

class RockPaperScissors:
    def __init__(self, master):
        self.master = master
        self.master.title("Rock Paper Scissors")

        self.player_score = 0
        self.computer_score = 0

        self.choice_labels = []
        self.choice_images = []
        self.create_choices()

        self.score_label = tk.Label(self.master, text=f"Player {self.player_score} - Computer {self.computer_score}")
        self.score_label.pack()

        self.result_label = tk.Label(self.master, text="Choose an option to start playing!")
        self.result_label.pack()

        self.play_again_button = tk.Button(self.master, text="Play again", command=self.play_again)
        self.play_again_button.pack_forget()

    def create_choices(self):
        choices_frame = tk.Frame(self.master)
        for choice in ['rock', 'paper', 'scissors']:
            label = tk.Label(choices_frame, text=choice.title())
            label.pack(side=tk.LEFT, padx=10)
            self.choice_labels.append(label)

            image = tk.PhotoImage(file=f"{choice}.png").subsample(4)
            button = tk.Button(choices_frame, image=image, command=lambda choice=choice: self.play(choice))
            button.image = image
            button.pack(side=tk.LEFT, padx=10)
            self.choice_images.append(image)
        choices_frame.pack()

    def play(self, player_choice):
        computer_choice = random.choice(['rock', 'paper', 'scissors'])
        winner = self.determine_winner(player_choice, computer_choice)

        self.show_result(player_choice, computer_choice, winner)
        self.update_score(winner)
        self.update_choices_state()

    def determine_winner(self, player_choice, computer_choice):
        if player_choice == computer_choice:
            return "tie"
        elif (player_choice == 'rock' and computer_choice == 'scissors') or \
             (player_choice == 'paper' and computer_choice == 'rock') or \
             (player_choice == 'scissors' and computer_choice == 'paper'):
            return "player"
        else:
            return "computer"

    def show_result(self, player_choice, computer_choice, winner):
        result = f"Player chose {player_choice}, computer chose {computer_choice}. "
        if winner == "tie":
            result += "It's a tie!"
        elif winner == "player":
            result += "You win!"
        else:
            result += "Computer wins!"
        self.result_label.config(text=result)

    def update_score(self, winner):
        if winner == "player":
            self.player_score += 1
        elif winner == "computer":
            self.computer_score += 1
        self.score_label.config(text=f"Player {self.player_score} - Computer {self.computer_score}")

    def update_choices_state(self):
        if self.player_score >= 3 or self.computer_score >= 3:
            for image in self.choice_images:
                image.configure(state=tk.DISABLED)
            self.play_again_button.pack()
        else:
            for image in self.choice_images:
                image.configure(state=tk.NORMAL)

    def play_again(self):
        self.player_score = 0
        self.computer_score = 0
        self.score_label.config(text=f"Player {self.player_score} - Computer {self.computer_score}")
        self.result_label.config(text="Choose an option to start playing!")
        self.update_choices_state()

root = tk.Tk()
app = RockPaperScissors(root)
root.mainloop()
