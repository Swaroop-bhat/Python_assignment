# print(pow(2,-3))

class Power:
    def power_of(self,base,power):
        result=pow(base,power)
        print(result)

base=int(input("Enter the base value: "))
power=int(input("Enter the power value: "))
ins=Power()
ins.power_of(base,power)


