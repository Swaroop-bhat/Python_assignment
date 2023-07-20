# res = {}
# dict1 = {1: 1, 2: 34, 3: 56, 4: 67, 5: 87}
# sorted_dict = sorted(dict1.items(), key=lambda x: x[1], reverse=True)
# for i in range(3):
#     res[sorted_dict[i][0]] = sorted_dict[i][1]
# print(res)


dict1 = {'A': 67, 'B': 23, 'C': 45,
           'D': 56, 'E': 12, 'F': 69}

x = list(dict1.values())
x.sort(reverse=True)
x = x[:3]
print(x)
