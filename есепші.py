import math
x = int(input("x="))
if x<=1:
    a = int(input("a="))
    y = 1 + math.sqrt(a + math.fabs(x))
    print("y = ", round(y))
elif 1<x<=7:
    a = int(input("b="))

    y = 2 + a * math.pow(x,2)+math.exp(x)
    print("y=", round(y))
elif x>7:
    b = int(input("a="))

    y = x * math.sqrt(1 + b * math.log(math.pow(x,2))* x)
    print("y=", round(y))
