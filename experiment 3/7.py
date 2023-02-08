print("Enter the number")
num=int(input())
if num%5==0 and num%6==0:
    print("The given number is divisible by both 5 and 6\n")
elif num%5==0 and num%6!=0:
    print("Number is divisible by 5 only")
elif num%5!=0 and num%6==0:
    print("Number is divisible by 6 only")