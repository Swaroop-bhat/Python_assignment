import itertools
num = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
num.sort()
new= list(num for num, _ in itertools.groupby(num))
print(new)
