n=int(input("enter the number:"))
num=[]


while(n!=1 and n not in num):
    num.append(n)
    n=sum([int(i)*int(i) for i in str(n)])
    
print(num)
if (n==1):
    print("round")
else:
    print("Not a round")
    

