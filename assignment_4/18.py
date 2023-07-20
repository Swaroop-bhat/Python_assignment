string = input("Enter the string:")
new_string = ""
for char in range(len(string)):
    if string[char] == ',':
        new_string += '.'
    elif string[char] == '.':
        new_string += ','
    else:
        new_string += string[char]
print(new_string)
