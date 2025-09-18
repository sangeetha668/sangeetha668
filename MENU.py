def sq():
    print("enter teh side of square")
def rect(a,b):
    print("area of the rectangle:",a*b)
def cir():
    return 3.14*r*r
def tri(a,b):
    return 0.5*a*b
          
while(1):
    print("___ MENU_____")
    print("SQUARE")
    print("RECTANGLE")
    print("CIRCLE")
    print("TRIANGLE")
    d=int(input("enter the choice:"))
    if(d==1):
        sq()
    elif(d==2):
        l=int(input("enter the len of rect"))
        b=int(input("enter the breadth of the rect"))
        rect(l,b)
    elif(d==3):
        x=cir()
        print("the area is",x)
    elif(d==4):
        b=int(input("enter the base of the triangle"))
        h=int(input("enter the ht of the triangle"))
        f=tri(b,h)
