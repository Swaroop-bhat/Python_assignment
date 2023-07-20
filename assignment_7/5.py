def findTriplets(arr, n):
    res = False
    a=[]
    b=[]
    for i in range(0, n-2):

        for j in range(i+1, n-1):

            for k in range(j+1, n):

                if (arr[i] + arr[j] + arr[k] == 0):
                    a = [arr[i], arr[j], arr[k]]
                    b.append(a)
                    res = True              
    if (res == False):
        print(" not exist ")
    else:
        print(b)    


List1 = [-25, -10, -7, -3, 2, 4, 8, 10]
n = len(List1)
findTriplets(List1, n)
