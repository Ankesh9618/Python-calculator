x=int(input("To find area press 1. To find volumes press 2. For algebric equations press 3   "))
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
if (x==2):
    z=int(input("To find Volume of: Cube press 1 ; Cuboid press 2 ; Prism press 3 ; Cylinder press 4 ; Cone press 5 ; Sphere press 6"))
    if(z==1):
        A=int(input("Enter the length of side   "))
        print("Volume of the given Cube is ",A*A*A)
    elif(z==2):
        B=int(input("Enter the length   "))
        C=int(input("Enter the height   "))
        D=int(input("Enter the width   "))
        print("Volume of the given Cuboid is ",B*C*D)
    elif(z==3):
        E=int(input("Enter the value of base   "))
        F=int(input("Enter the value of height   "))
        print("Volume of the given Prism is ",E*F)
    elif(z==4):
        G=int(input("Enter the radius   "))
        H=int(input("Enter the height   "))
        print("Volume of the given Cylinder is ",3.142*G*G*H)
    elif(z==5):
        I=int(input("Enter the value of base   "))
        J=int(input("Enter the height   "))
        print("Volume of the given Cone is ",(I*J)/3)
    else:
        K=int(input("Enter the radius   "))
        print("Volume of the given Sphere is ",(K*K*K*3.142*4)/3)
if (x==3):
    x1=int(input("For a^2-b^2 press 1 ; (a+b)^2 press 2 ; a^2+b^2 press 3 ; (a-b)^2 press 4 ; (a+b+c)^2 press 5 ; (a-b-c)^2 press 6 ; (a+b)^3 press 7 ; (a-b)^3 press 8 ; a^3-b^3 press 9 ; a^3+b^3 press 0))
    if(x1==1):
        a1=int(input("Enter value of a   "))
        b1=int(input("Enter value of b   "))
        print((a1-b1)*(a1+b1))
    elif(x1==2):
        a2=int(input("Enter value of a   "))
        b2=int(input("Enter value of b   "))
        print(a2*a2+2*a2*b2+b2*b2)
    elif(x1==3):
        a3=int(input("Enter value of a   "))
        b3=int(input("Enter value of b   "))
        print((a3**a3-2*a3*b3+b3*b3)+2*a3*b3)
    elif(x1==4):
        a4=int(input("Enter value of a   "))
        b4=int(input("Enter value of b   "))
        print(a4*a4-2*a4*b4+b4*b4)
    elif(x1==5):
        a5=int(input("Enter value of a   "))
        b5=int(input("Enter value of b   "))
        c1=int(input("Enter value of c   "))
        print(a5*a5+b5*b5+c1*c1+2*a5*b5+2*b5*c1+2*c1*a5)
    elif(x1==6):
        a6=int(input("Enter value of a   "))
        b6=int(input("Enter value of b   "))
        c2=int(input("Enter value of c   "))
        print(a6*a6+b6*b6+c2*c2-2*a6*b6+2*b6*c2-2*c2*a6)
    elif(x1==7):
        a7=int(input("Enter value of a   "))
        b7=int(input("Enter value of b   "))
        print(a7*a7*a7+b7*b7*b7+3*a7*b7(a7+b7))
    elif(x1==8):
        a8=int(input("Enter value of a   "))
        b8=int(input("Enter value of b   "))
        print(a8*a8*a8-b8*b8*b8-3*a8*a8*b8+3*a8*b8*b8)
    elif(x1==9):
        a9=int(input("Enter value of a   "))
        b9=int(input("Enter value of b   "))
        print((a9-b9)*(a9*a9+a9*b9+b9*b9))
    else:
        a0=int(input("Enter value of a   "))
        b0=int(input("Enter value of b   "))
        print((a0+b0)*(a0*a0-a0*b0+b0*b0))
        
