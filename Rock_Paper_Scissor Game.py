#Rock_Paper_Scissor Game
#importing necessary modules
import random


print("1.Rock")
print("2.Paper")
print("3.Scissors",'\n')

#taking choice from users.
User_choice = int(input("Enter your choice: "))
Computer_choice = random.randint(1, 3)
print("Computer choice:", Computer_choice,'\n')
match Computer_choice:
  case 1:
    print("1.Rock")
  case 2:
    print("2.Paper")
  case 3:
    print("3.Scissors")

#checking who wins
if User_choice == Computer_choice:
  print("Match draw")
elif User_choice != Computer_choice:
  print("Computer wins!")
elif User_choice > Computer_choice:
  print("You win!")
elif User_choice < Computer_choice:
  print("You win!")
elif User_choice > Computer_choice:
  print("Computer wins!")
elif User_choice < Computer_choice:
  print("Computer wins!")
elif User_choice > Computer_choice:
  print("You win!")
else:
  print("Computer wins:)")
print("Want to play one more time?: "); print("1.Yes"); print("2.No")
ANS = input("Enter your choice: ")

while True:
  if ANS == 'yes':
    'continue'
  else:
    'break'
