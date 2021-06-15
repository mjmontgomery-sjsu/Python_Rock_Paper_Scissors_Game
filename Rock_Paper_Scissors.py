#Rock, Paper, Scissors Program
import random

choices = ["R","P","S"]

def get_choice(input):
  if input == "R":
    return "Rock"
  elif input == "P":
    return "Paper"
  elif input == "S":
    return "Scissors"
  else:
    return "Not [R,P, or S]"

print ("Rock, Paper, Scissors - Shoot!")
print ("[R] = Rock, [P] = Paper, [S] = Scissors and [Q] = Quit")
counter = 1

while True:

  print("Game "+str(counter)+":")
  print("Please choose a letter (Choices are Case Sensitive)")

  user_choice = input()

  if user_choice =="Q":
    print("Thanks for Playing! ")
    break;

  random_index = random.randint(0,2)
  computer_choice = choices[random_index]

  print("You chose "+get_choice(user_choice)+" and the computer chose "+get_choice(computer_choice))

  if user_choice =="R" and computer_choice == "S":
    print("You win! Rock beats Scissors!")
  elif user_choice =="P" and computer_choice == "R":
    print("You win! Paper beats Rock!")
  elif user_choice =="S" and computer_choice == "P":
    print("You win! Scissors beats Paper!")
  elif user_choice =="R" and computer_choice == "P":
    print("Computer wins, Paper beats Rock  ):")
  elif user_choice =="P" and computer_choice == "S":
    print("Computer wins, Scissors beats Paper  ):")
  elif user_choice =="S" and computer_choice == "R":
    print("Computer wins, Rock beats Scissors  ):")
  elif user_choice == computer_choice:
    print("It's a Draw!")
  else:
    print("Please enter [R, P, S, or Q ]")

  counter = counter+1
  print('\n')





