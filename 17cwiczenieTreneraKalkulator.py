#!/usr/bin/python3

x = 9
while x == 9:

    choice = input(
        "\nStart calculator \n Prosze wpisać co chcesz zrobić... \n\n '1' or '+' = Dodać "
        "\n '2' or '-' = Odjąć \n '3' or '*' = Mnożyć \n " "'4' or '/' = Dzielenie \n '5' or '**' = Potęgowanie "
        "\n '6' or '%' = Moduło \n '7' or '//' = Dzielenie w dół \n '8' or 'end' = END PROGRAM \n")

    if choice == "1" or choice == "+":
        print("YOUR CHOICE IS ADDING")
        firstDigit = int(input("enter your first number \n"))
        secondDigit = int(input("enter your second number \n"))
        print("\n", firstDigit, "+", secondDigit, "=", firstDigit + secondDigit, "\n", "YOUR RESULT IS", "=",
              firstDigit + secondDigit)
    elif choice == "2" or choice == "-":
        print("YOUR CHOICE IS SUBTRACT")
        firstDigit = int(input("enter your first number \n"))
        secondDigit = int(input("enter your second number \n"))
        print("\n", firstDigit, "-", secondDigit, "=", firstDigit - secondDigit, "\n", "YOUR RESULT IS", "=",
              firstDigit - secondDigit)
    elif choice == "3" or choice == "*":
        print("YOUR CHOICE IS MULTIPLICATION")
        firstDigit = int(input("enter your first number \n"))
        secondDigit = int(input("enter your second number \n"))
        print("\n", firstDigit, "*", secondDigit, "=", firstDigit * secondDigit, "\n", "YOUR RESULT IS", "=",
              firstDigit * secondDigit)
    elif choice == "4" or choice == "/":
        print("YOUR CHOICE IS TO SHARE")
        firstDigit = int(input("enter your first number \n"))
        secondDigit = int(input("enter your second number \n"))
        if secondDigit == 0:
            print("Pamiętaj cholero nie dziel przez zero")
        else:
            firstDigit = int(input("enter your first number \n"))
            secondDigit = int(input("enter your second number \n"))
            print("\n", firstDigit, "/", secondDigit, "=", firstDigit / secondDigit, "\n", "YOUR RESULT IS", "=",
                  firstDigit / secondDigit)
    elif choice == "5" or choice == "**":
        print("YOUR CHOICE IS EXPANSION")
        firstDigit = int(input("enter your first number \n"))
        secondDigit = int(input("enter your second number \n"))
        print("\n", firstDigit, "**", secondDigit, "=", firstDigit ** secondDigit, "\n", "YOUR RESULT IS", "=",
              firstDigit ** secondDigit)
    elif choice == "6" or choice == "%":
        print("YOUR CHOICE IS A MODULE")
        firstDigit = int(input("enter your first number \n"))
        secondDigit = int(input("enter your second number \n"))
        print("\n", firstDigit, "%", secondDigit, "=", firstDigit % secondDigit, "\n", "YOUR RESULT IS", "=",
              firstDigit % secondDigit)
    elif choice == "7" or choice == "//":
        print("YOUR CHOICE IS TO SHARE DOWN")
        firstDigit = int(input("enter your first number \n"))
        secondDigit = int(input("enter your second number \n"))
        if secondDigit == 0:
            print("Pamiętaj cholero nie dziel przez zero")
        else:
            firstDigit = int(input("enter your first number \n"))
            secondDigit = int(input("enter your second number \n"))
            print("\n", firstDigit, "//", secondDigit, "=", firstDigit // secondDigit, "\n", "YOUR RESULT IS", "=",
                  firstDigit // secondDigit)
    elif choice == "8" or choice == "end":
        print("Quit")
        break
    else:
        print("\nNOT RIGHT CHOICE !")
        continue
