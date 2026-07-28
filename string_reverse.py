str = input("Enter a string: ")
chars = list(str)
length = len(str)

for i in range(length//2):
    temp = chars[i]
    chars[i] = chars[length-i-1]
    chars[length-i-1] = temp
    
str = "".join(chars)

print("Reversed string is: " + str)