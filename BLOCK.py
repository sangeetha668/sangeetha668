#BLOCK PATTERN
start = int(input("Enter the stars (columns): "))
block = int(input("Enter the number of blocks: "))
lines = int(input("Enter the lines (rows): "))
for i in range(block):
    count = 0
    for j in range(lines-i):
        
        for k in range(start):
            print("*", end=" ")
            count += 1
        print()  
    print(count)   
    print("----------")

