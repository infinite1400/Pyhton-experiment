print("Enter the todays day 0-monday 1-tuesday .... 6-sunday\n")
x=int(input())
print("The number of days after today you want to know the day of ?\n")
y=int(input())
y=y+1
z=x+y
z=z%7

if z==0:
    print("Sunday")
elif z==1:
    print("Monday")
elif z==2:
    print("Tuesday")
elif z==3:
    print("Wednesday")
elif z==4:
    print("Thursday")
elif z==5:
    print("Friday")
elif z==6:
    print("Saturday")