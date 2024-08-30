#Designing A Simple Caslculator
#Taking the user input for the number
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

#operation choice for the user
choice = input("Enter the operation to be performed(+,-,*,/): ")

#performing operations
if choice == '+':
  print(num1 + num2)
elif choice == '-':
  print(num1 - num2)
elif choice == '*':
  print(num1 * num2)
elif choice == '/':
  print(num1 / num2)
else:
  print("Invalid operation")