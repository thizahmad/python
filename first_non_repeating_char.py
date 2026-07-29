text = input("Enter a string: ")
freq = {}

for ch in text:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

for ch in text:
    if freq[ch] == 1:
        print("First non-repeating character is: ", ch)
        break
else:
    print("All characters are repeating")