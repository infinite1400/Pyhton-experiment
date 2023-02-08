print("Enter the edges of triangles")
a=int(input())
b=int(input())
c=int(input())
if a+b>c and b+c>a and a+c>b:
    print("The perimeter is :",a+b+c)
else:print("Invalid input")
