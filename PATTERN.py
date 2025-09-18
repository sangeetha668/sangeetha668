a=int(input("enter the number:"))
grid=[["A " for i in range (a+2)] for i in range (a+2)]
for i in range(a+2):
    for j in range(a+2):
        if(i==0 or i==a+1 or j==0 or j==a+1):
            grid[i][j]="A"
        elif(a%2!=0):
            grid[i][j]="*"
        elif(a%2==0):
            grid[i][j]="$"
        print(grid[i][j],end=" ")

    print()
