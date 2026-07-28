choose = input("Enter the size of coffee you want: ")
options = ["Small", "Medium", "Large"]
extra_shot = input("Do you want an extra shot? ")

if choose in options:
    print("Your coffee size is " + choose)
    if extra_shot.lower() == "yes":
        print("Here is your extra shot")
