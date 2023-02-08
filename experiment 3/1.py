import math

print("Enter the three numbers\n")
a=int(input())
b=int(input())
c=int(input())

d=b**2-4*a*c
if d==0:
    x=(-b)/2*a
    print("The roots are %d %d",x,x)
elif d>0:
    D=math.sqrt(d)
    r1=(-b+D)/2*a
    r2=(-b-D)/2*a
    print("The roots are %d %d",r1,r2)
else:
    print("The equations has no real roots")

