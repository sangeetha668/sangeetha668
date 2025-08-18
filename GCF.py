a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))

while b != 0:
    rem = a % b
    a = b
    b = rem

print(a)
