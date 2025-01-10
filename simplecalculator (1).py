#Kaylie Yuen
#Simple Calculator

#Functions
def addition(num1, num2):
    solution = num1 + num2
    print("The solution is: " + str(solution) + "\n")
def subtraction(num1, num2):
    solution = num1 - num2
    print("The solution is: " + str(solution) + "\n")
def multiplication(num1, num2):
    solution = num1 * num2
    print("The solution is: " + str(solution) + "\n")
def division(num1, num2):
    solution = num1 / num2
    print("The solution is: " + str(solution) + "\n")

#Main

print("Welcome to a simple, 4-function calculator!")

while True:
    print("Select an operation: ")
    print("1. Addition \n2. Subtraction \n3. Multiplication \n4. Division \n5. Quit program")
    option = int(input("(1-5) Select an option: "))

    if option == 1:
        int1 = int(input("Enter the first number: "))
        int2 = int(input("Enter the second number: "))
        addition(int1, int2)

    if option == 2:
        int1 = int(input("Enter the first number: "))
        int2 = int(input("Enter the second number: "))
        subtraction(int1, int2)

    if option == 3:
        int1 = int(input("Enter the first number: "))
        int2 = int(input("Enter the second number: "))
        multiplication(int1, int2)

    if option == 4:
        int1 = int(input("Enter the first number: "))
        int2 = int(input("Enter the second number: "))
        division(int1, int2)

    if option == 5:
        print("You have ended the calculator program.")
        break
