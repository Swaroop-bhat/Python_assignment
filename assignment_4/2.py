string = input("Enter the string:")
all_freq = {}

for i in string:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1

sorted_dict = dict(sorted(all_freq.items(), key=lambda x: x[1], reverse=True))
print("Frequency of character in string:\n"+str(sorted_dict))
