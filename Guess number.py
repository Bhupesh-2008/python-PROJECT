import random
number_to_guess= random.randint(1,100)
while True:
  try:
    guess=int(input("GUESS THE NUMBER BETWEEN 1 AND 100:"))

    if guess <number_to_guess:
      print("Too low")
    elif guess>number_to_guess:
      print("Too high")
    else:
      print("Congrats! You are absolutely right and guessed the correct number.")
      break
  except ValueError:
    print("PLEASE ENTER A VALID INPUT")
         

         