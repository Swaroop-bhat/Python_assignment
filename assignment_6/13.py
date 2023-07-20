dictionary = {'e': 120, 'f': 104, 'b': 150,
              'a': 132, 'c': 125, 'h': 45, 's': 132}
res = {}
for key, value in dictionary.items():
    if value not in res.values():
        res[key] = value
print(res)
