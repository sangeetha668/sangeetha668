def gcd(a,b):
    while b != 0:
        rem = a % b
        a = b
        b = rem
        return (a*b)
def cop(a,b):
    return gcd(a,b)

a=int(input(" enter the number "))
for i in range(5,a):
    for j in range(4,i):
        for k in range(3,j):
            if(j*j+k*k==i*i and cop(i,j) and cop(j,k) and cop(i,k)):
               print(k,j,i)
