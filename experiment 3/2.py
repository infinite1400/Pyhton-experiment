import math

print("Enter a,b,e\n")
a=int(input())
b=int(input())
e=int(input())

print("Enter c,d,f\n")
c=int(input())
d=int(input())
f=int(input())

z=a*d-b*c
if z==0:
    print("Equation has no solutions")
else:
    x=(e*d-b*f)/z
    print("x:",x)
    x=(a*f-c*e)/z
    print("x:",x)