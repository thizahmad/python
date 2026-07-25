age = input("Give me your age: ")

int_age = int(age)

if int_age < 13:
    print("Child")
elif int_age < 20:
    print("Teenager")
elif int_age < 59:
    print("Adult")
elif int_age >= 60:
    print("Senior")
    