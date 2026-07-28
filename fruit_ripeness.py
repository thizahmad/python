ripe_dictionary = {
    "green": "unripe",
    "yellow": "ripe",
    "brown": "overripe"
}

fruit_color = input("Enter the color of your fruit: ")

if fruit_color in ripe_dictionary:
    print("The fruit is " + ripe_dictionary[fruit_color])
else:
    print("Color not found in the dictionary.")