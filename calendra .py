"""import random
no=int(input("enter the no of teams"))
team=[]
for i in range(no):
    a=(input("enter the team name:"))
    team.append(a)
meet=int(input("enter the  no of meetings   b?w two teams:"))
matches=[]
for i in range(no-1):
    for j in range(i+1,no):
        for k in range(meet):
            matches.append([team[i],team[j]])
random.shuffle(matches)
for i in range(len(matches)):
    print("matches{} .{} vs {}".format(i+1,matches[i][0],matches[i][1]))


"""
n=int(input("enter the number:"))
num=[]
res=0
num.append(n)
while(n!=1 or n not in num):
    res=[int(i)*int(i) for i in str(n)]
    print(sum(res))

