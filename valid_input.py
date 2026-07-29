while True:
    num = int(input("Enter a number: "))
    if num > 0 and num < 10:
        print("valid input")
        break
    else:
        print("Invalid input, please enter a number between 1 and 9.")