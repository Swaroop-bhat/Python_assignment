dictionary = {'a': 120, 'b': 104, 'c': 150, 'd': 132, 'e': 125}
asc_sorted_dictionary = sorted(dictionary.items(), key=lambda x: x[1])
asc_converted_dict = dict(asc_sorted_dictionary)
print(asc_converted_dict)


des_sorted_dictionary = sorted(dictionary.items(), key=lambda x: x[1],reverse=True)
des_converted_dict = dict(des_sorted_dictionary)
print(des_converted_dict)

