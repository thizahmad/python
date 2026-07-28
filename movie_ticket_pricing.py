age = input("Enter your age: ")
day = input("Enter the day: ")
int_age = int(age)

price = 12 if int_age >= 18 else 8

if(day.lower() == "wednesday"):
    price -= 2

print("Your price is: $", price)