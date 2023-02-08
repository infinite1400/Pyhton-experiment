print("Enter the price and weight of 1st package\n")
p1=int(input())
w1=int(input())

print("Enter the price and weight of 2nd package\n")
p2=int(input())
w2=int(input())

r1=w1/p1
r2=w2/p2
if r1>r2:
    print("First packege has better price")
elif r1<r2:
    print("Second package has better price\n")
else:
    print("You can buy any package\n")
