print("Enter month and year ")
month = int(input())
year = int(input())






if month > 12 and month < 0:
    print("Invalid input for month\n")
elif month == 1:
    print("The month",month,"Janurary ,",year," has 31 days")
elif month==2:
    days=28
    if year%400==0 and year%4==0:
        days=29
    print("The month",month,"Feburary ,",year," has",days,"days")
elif month==3:
    print("The month",month,"March ,",year," has 31 days")
elif month==4:
    print("The month",month,"April ,",year," has 31 days")
elif month==5:
    print("The month",month,"May ,",year," has 31 days")
elif month==6:
    print("The month",month,"June ,",year," has 31 days")
elif month==7:
    print("The month",month,"July ,",year," has 31 days")
elif month==8:
    print("The month",month,"August ,",year," has 31 days")
elif month==9:
    print("The month",month,"September ,",year," has 31 days")
elif month==10:
    print("The month",month,"October ,",year," has 31 days")
elif month==11:
    print("The month",month,"November ,",year," has 31 days")
elif month==12:
    print("The month",month,"December ,",year," has 31 days")
