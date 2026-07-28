password = input("Enter your password: ")
length_pass = len(password)

if length_pass < 6:
    print("weak password")
elif length_pass < 10:
    print("medium password")
else:
    print("strong password")
