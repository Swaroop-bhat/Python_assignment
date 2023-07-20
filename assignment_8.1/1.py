import random

def num_generator():
    com_num=random.sample("0123456789",4)
    com_num="".join(com_num)
    print(com_num)
    return(com_num)

def user_input():
    while(True):
        try:
            global user_num
            user_num=input("Enter Your Number:")
            if(len(user_num)!=4):
                print("Enter a 4 digit number")
                continue
        except ValueError:
            print("The input you entered is not a number")
        else:
            x=0
            for i in range(0,4):
                x=x+user_num.count(user_num[i])
            if(x!=4):
                print("Enter a number with different digits")
                continue
            else:
                return

def num_comparison(a,b):
    a=str(a)
    b=str(b)
    for i in range(0,4):
        for j in range(0,4):
            if(i==j)and(a[i]==b[j]):
                global cow_count
                cow_count+=1
            elif(i!=j)and(a[i]==b[j]):
                global bull_count
                bull_count+=1
            else:
                pass

print("***********COWS AND BULLS GAME***********")
user_num=0
user_choice=True
cow_count=0
bull_count=0
game_num=num_generator()
score_counter=0
while(True):
    user_input()
    score_counter=score_counter+1
    num_comparison(game_num,user_num)
    if(cow_count==4):
        print("You won")
        print("Completed in",str(score_counter)," chances")
        break
    else:
        print("cow_count",cow_count)
        print("bull_count",bull_count)
        cow_count=0
        bull_count=0