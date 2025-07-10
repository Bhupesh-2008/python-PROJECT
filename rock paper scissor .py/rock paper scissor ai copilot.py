import random
while True:
    you = input("Choose Rock(r), Paper(p), Scissors(s): ").lower()

    if you not in ['r', 'p', 's']:
        print("PLEASE PUT IN A VALID CHOICE")
        continue

    computer_choice = random.choice(['r', 'p', 's'])

    if you == computer_choice:
        print("You have a tie!")
    elif (you == 'r' and computer_choice == 's') or \
         (you == 'p' and computer_choice == 'r') or \
         (you == 's' and computer_choice == 'p'):
        print("Awesome, You won!")
    else:
        print("Computer wins")

    again = input("Play again? (y/n): ").lower()
    if again != 'y':
        break