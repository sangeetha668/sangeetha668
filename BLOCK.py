#block
start = int(input("Enter the stars (columns): "))
block = int(input("Enter the number of blocks: "))
lines = int(input("Enter the lines (rows): "))

# Loop through blocks
for i in range(block):
    count = 0
    # Loop through rows
    for j in range(lines-i):
        # Loop through columns
        for k in range(start):
            print("*", end=" ")
            count += 1
        print()  
    print(count)   
    print("----------")
