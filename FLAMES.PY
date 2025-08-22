#FLAMES digital problem
a=input("enter teh boy name:  ")
b=input("enter teh girkl name:  ")

a1=list(a)
b1=list(b)
for i in range(len(a1)):
    for j in range (len(b1)):
        if (a1[i]==b1[j]):
            a1[i]="2"
            b1[j]="2"
print(a1)
print(b1)
c=0
for i in a1:
    if(i!='2'):
        c=c+1

for j in b1:
    if(j!='2'):
        c=c+1
print(c)
f=0
res=list("FLAMES")
for i in  range(5):
    f=(f+(c-1))%len(res)
    res.pop(f)
print(res[0])
