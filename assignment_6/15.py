dict1 = {'a': 100, 'b': 200, 'c': 300}
dict2 = {'a': 300, 'b': 200, 'd': 400}
res={}

for key in dict2:
    if key in dict1:
        dict2[key] = dict2[key] + dict1[key]
        del dict1[key]
    else:
        pass
res=dict1 |dict2
final_res=dict(sorted(res.items(),key=lambda x:x[1],reverse=True))
print(final_res)
