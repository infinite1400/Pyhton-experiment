print("enter a number")
x = input()
x = int(x)
sum = 0
for num in range(2, x + 1):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
            sum += num
            print(num)

print("Sum is :",sum)