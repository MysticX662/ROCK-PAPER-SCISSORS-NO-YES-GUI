import random

def get_player_choice():
    valid_choices = ['rock', 'paper', 'scissors']
    choice = input("Please choose (rock/paper/scissors): ").lower()
    while choice not in valid_choices:
        print("Invalid choice.")
        choice = input("Please choose (rock/paper/scissors): ").lower()
    return choice

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "tie"
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'paper' and computer_choice == 'rock') or \
         (player_choice == 'scissors' and computer_choice == 'paper'):
        return "player"
    else:
        return "computer"

def play_game():
    print("Welcome to Rock Paper Scissors!")
    player_score = 0
    computer_score = 0
    while True:
        print(f"\nScore: Player {player_score} - Computer {computer_score}")
        player_choice = get_player_choice()
        computer_choice = get_computer_choice()
        print(f"Player chose {player_choice}, computer chose {computer_choice}")
        winner = determine_winner(player_choice, computer_choice)
        if winner == "tie":
            print("It's a tie!")
        elif winner == "player":
            print("You win!")
            player_score += 1
        else:
            print("Computer wins!")
            computer_score += 1
        play_again = input("Play again? (y/n): ").lower()
        if play_again != 'y':
            break
    print("Thanks for playing!")

if __name__ == '__main__':
    play_game()
