string = input("Enter the string:")
length = len(string)
if len(string) >= 2:
    print(string[0:2]+string[length-2:])
else:
    print("Empty String")
