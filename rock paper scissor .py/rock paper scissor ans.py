import random

def get_user_choice():
    print("Rock 🪨, Paper 📄, or Scissors ✂️?")
    choice = input("Enter your choice: ").lower()
    if choice in ['rock', 'paper', 'scissors']:
        return choice
    else:
        print("Invalid choice! Please select Rock, Paper, or Scissors.")
        return get_user_choice()

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user, computer):
    print(f"\nYou chose: {user}")
    print(f"Computer chose: {computer}")
    
    if user == computer:
        return "It's a tie!"
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'scissors' and computer == 'paper') or \
         (user == 'paper' and computer == 'rock'):
        return "You win! 🎉"
    else:
        return "You lose! 😢"

# Main game loop
def play_game():
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        result = determine_winner(user_choice, computer_choice)
        print(result)
        
        again = input("\nPlay again? (yes/no): ").lower()
        if again != 'yes':
            print("Thanks for playing!")
            break

play_game()
