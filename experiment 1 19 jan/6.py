import math

print("Enter co-ordinates of point 1")
x1=int(input())
y1=int(input())

print("Enter co-ordinates of point 2")
x2=int(input())
y2=int(input())
a=math.pow(x1-x2, 2)+math.pow(y1-y2, 2)
a=print("Distance is :",math.sqrt(a))