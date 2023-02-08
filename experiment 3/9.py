print("Enter hexa character")
str=input()
str=str[::-1]
mul=1;
decimal=int(0)
for i in str:
    if i=='A':
        decimal+=10*mul
    elif i=='B':
        decimal+=11*mul
    elif i=='C':
        decimal+=12*mul
    elif i=='D':
        decimal+=13*mul
    elif i=='E':
        decimal+=14*mul
    elif i=='F':
        decimal+=15*mul
    elif i=='0':
        decimal+=0*mul
    elif i=='1':
        decimal+=1*mul
    elif i=='2':
        decimal+=2*mul
    elif i=='3':
        decimal+=3*mul
    elif i=='4':
        decimal+=4*mul
    elif i=='5':
        decimal+=5*mul
    elif i=='6':
        decimal+=6*mul
    elif i=='7':
        decimal+=7*mul
    elif i=='8':
        decimal+=8*mul
    elif i=='9':
        decimal+=9*mul
    mul*=16;
print(decimal)
    
    
    