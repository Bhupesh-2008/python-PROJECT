import random

while True:
    you= input("What do you wanna want to choose among Rock,Paper and Scissors? (r/p/s):").lower()

    computer_choice= random.choice(['r','p','s'])
    if you=='r'and computer_choice=='r':
        print("You have a tie!")
    elif you=='r' and computer_choice=='p':
        print ("Computer wins")
    elif you=='r' and computer_choice=='s':
        print("Awesome, You won !")
    elif you =='p' and computer_choice=='r':
        print("Awesome, You won!")
    elif you=='p' and computer_choice =='p':
        print("You have a tie!")
    elif you=='p' and computer_choice =='s':
        print("Computer wins")
    elif you=='s' and  computer_choice=='r':
        print("Compuiter wins")
    elif you=='s'and  computer_choice=='p':
        print("Awesome, You won!")
    elif you=='s'and  computer_choice=='s':
        print("You have a tie!")

        break
    if you not in ['r','p','s'] :
         print("PLEASE PUT IN A VALID CHOICE")