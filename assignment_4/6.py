string = input("Enter the first string:")
if len(string)>=3:
    if string.endswith('ing'):
        string += 'ly'
        print(string)
    else:
        string += 'ing'
        print(string)
