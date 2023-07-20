dict1 = [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max',
                                                             'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]

sorted_dict1=sorted(dict1,key=lambda x:x['color'])
print(sorted_dict1)
