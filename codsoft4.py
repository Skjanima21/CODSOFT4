import random
def get_computer_choice():
    """Generate a random choice for the computer."""
    return random.choice(["rock", "paper", "scissors"])
def determine_winner(user_choice, computer_choice):
    """Determine the winner based on the rules of the game."""
    if user_choice == computer_choice:
        return "tie"
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "scissors" and computer_choice == "paper") or
        (user_choice == "paper" and computer_choice == "rock")
    ):
        return "user"
    else:
        return "computer"
def play_round():
    """Play a single round of Rock-Paper-Scissors."""
    user_choice = input("\nEnter your choice (rock, paper, scissors): ").lower()
    if user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        return None, None
    computer_choice = get_computer_choice()
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    winner = determine_winner(user_choice, computer_choice)
    if winner == "tie":
        print("It's a tie!")
    elif winner == "user":
        print("You win this round!")
    else:
        print("Computer wins this round!")
    return winner, computer_choice
def play_game():
    """Play the Rock-Paper-Scissors game."""
    print("Welcome to Rock-Paper-Scissors!")
    user_score = 0
    computer_score = 0
    while True:
        winner, _ = play_round()
        if winner == "user":
            user_score += 1
        elif winner == "computer":
            computer_score += 1
        print(f"\nCurrent Scores: You: {user_score} | Computer: {computer_score}")
        play_again = input("\nDo you want to play another round? (y/n): ").lower()
        if play_again != "y":
            print("\nThanks for playing!")
            print(f"Final Scores: You: {user_score} | Computer: {computer_score}")
            break
if __name__ == "__main__":
    play_game()
