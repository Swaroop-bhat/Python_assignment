file = open("file.txt", "r")

words = file.read()
list1= words.replace('\n', ' ').split(".")

print(list1)
file.close()
