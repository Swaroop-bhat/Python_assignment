dict1 = {}
number=int(input("enter the number: "))
for i in range(number):
    key=input("Enter the key: ")
    value=input("Enter the value: ")
    dict1[key]=value
    
print(dict1)
    
for key,item in dict1.items():
    print(key,item)