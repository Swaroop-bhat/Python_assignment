dictionary = {'e': 120, 'f': 104, 'b': 150, 'a': 132, 'c': 125}
sorted_dictionary = sorted(dictionary.items(), key=lambda x: x[0])
converted_dict = dict(sorted_dictionary)
print(converted_dict)
