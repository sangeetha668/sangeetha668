a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))

x, y = a, b  


while b != 0:
    rem = a % b
    a = b
    b = rem


lcm = (x * y) // a

print("LCM =", lcm)
