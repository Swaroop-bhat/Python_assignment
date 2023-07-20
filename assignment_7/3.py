class Unique_subsets:
    def __init__(self):
        self.subsets = []

    def subset(self, num):
        self.subsets = []
        self.add(num, [], 0)
        return self.subsets

    def add(self, num, current, start):
        self.subsets.append(list(current))
        for i in range(start, len(num)):
            current.append(num[i])
            self.add(num, current, i + 1)
            current.pop()

input_set=[]
inp = int(input("Enter the no.of list elements: "))
for i in range(inp):
    value=int(input("Enter the elements: "))
    input_set.append(value)
generator = Unique_subsets()
result = generator.subset(input_set)
print(result)
