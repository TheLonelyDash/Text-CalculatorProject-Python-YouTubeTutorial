#Create a menu offering the user the options of
    #introduction, addition, subtraction, division, or multiplication
    #ensure there is an option to quit the program.
#Create an input for two numbers after user choice.
#Create functions for each of the options in the menu
    #Printing out the mathematical equation and the result.
#Prompt the user if they would like to do another calculation.

def addition(x, y):
    result = round(x + y, 2)
    print("\n" + str(x) + " + " + str(y) + " = " + str(result))

def subtraction(x, y):
    result = round(x - y, 2)
    print("\n" + str(x) + " - " + str(y) + " = " + str(result))

def division(x, y):
    result = round(x / y, 2)
    print("\n" + str(x) + " / " + str(y) + " = " + str(result))

def multiplication(x, y):
    result = round(x * y, 2)
    print("\n" + str(x) + " * " + str(y) + " = " + str(result))


while True:

    print("\nThe LonelyDash Calculator: What would you like to do?\n")
    print("1. Add")
    print("2. Subtract")
    print("3. Divide")
    print("4. Multiply")
    print("5. Quit")

    choice = input("\nChoose a number: ")
    choices = ["1", "2", "3", "4", "5"]
    if choice not in choices:
        print("Try again, choose 1, 2, 3, 4, or 5!")
    else:
        choice = int(choice)

    if choice == 1:
        x = input("Input your first number: ")
        y = input("Input your second number: ")
        try:
            x = float(x)
            y = float(y)
            addition(x, y)
        except:
            print("Both inputs can only contain numbers and a decimal. Try again!")

    elif choice == 2:
        x = input("Input your first number: ")
        y = input("Input your second number: ")
        try:
            x = float(x)
            y = float(y)
            subtraction(x, y)
        except:
            print("Both inputs can only contain numbers and a decimal. Try again!")

    elif choice == 3:
        x = input("Input your first number: ")
        y = input("Input your second number: ")
        try:
            x = float(x)
            y = float(y)
            division(x, y)
        except:
            print("Both inputs can only contain numbers and a decimal. Try again!")

    elif choice == 4:
        x = input("Input your first number: ")
        y = input("Input your second number: ")
        try:
            x = float(x)
            y = float(y)
            multiplication(x, y)
        except:
            print("Both inputs can only contain numbers and a decimal. Try again!")

    elif choice == 5:
        print("We're sorry to see you go!  Thank you for choosing The Lonely Dash!")
        quit()