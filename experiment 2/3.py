print("enter number")
x = int(input())
a = int(0)
while x > 0:
    a=a*10+x%10
    x=int(x/10)
print("the reverse number is:",a)