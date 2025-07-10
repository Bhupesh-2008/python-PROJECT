import random
while True:

  Q1= input("Do you wanna want to roll a dice? (y/n):").lower()
  num=[1,2,3,4,5,6]
  get= random.choice(num)

  if (Q1=='y'):
    print(get)

  elif (Q1=='n'):
    print("Thanks for playing.")
    break
  else:
    print("Invalid choice")
