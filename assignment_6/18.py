list1 = [{}, {}, {}]
list2 = [{1: 2}, {}, {}]
print(all(not item for item in list1))
print(all(not item for item in list2))
