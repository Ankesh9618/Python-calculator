x=int(input("To find area press 1. To find volumes press 2   "))
if (x==1):
    y=int(input("To find Area of : Square press 1 ; Rectangle press 2 ; Triangle press 3 ; Rhombus press 4 ; Trapezoid press 5 ; Regular polygon press 6 ; Circle press 7 ; Cone press 8 ; Sphere press 9    "))
    if(y==1):
        a=int(input("Enter the length of side  "))
        print("Area of the given Square is ",a*a)
    elif(y==2):
        b=int(input("Enter the length of side   "))
        c=int(input("Enter the breadth   "))
        print("Area of the given Rectangle is ",b*c)
    elif(y==3):
        d=int(input("Enter the value of base   "))
        e=int(input("Enter the value of height   "))
        print("Area of the given Triangle is ",(d*e)/2)
    elif(y==4):
        f=int(input("Enter the value of large diagonal   "))
        g=int(input("Enter the value of small diagonal   "))
        print("Area of the given Rhombus is ",(f*g)/2)
    elif(y==5):
        h=int(input("Enter the value of large side   "))
        i=int(input("Enter the value of small side   "))
        j=int(input("Enter the value of height   "))
        print("Area of the given Trapezoid is ",((h+i)*j)/2)
    elif(y==6):
        k=int(input("Enter the value of perimetre   "))
        l=int(input("Enter the value of apothem   "))
        print("Area of the given Regular polygon is ",k*l/2)
    elif(y==7):
        m=int(input("Enter the radius   "))
        print("Area of the given Circle is ",3.142*m*m)
    elif(y==8):
        n=int(input("Enter the radius   "))
        o=int(input("Enter the slant height   "))
        print("Area of the given Cone is ",3.142*n*o)
    else:
        p=int(input("Enter the radius   "))
        print("Area of the given Sphere is ",4*3.142*p*p)