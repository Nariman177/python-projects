

a = input ('введите первое число: ')
b = input ('введите второе число: ')
c = input ('введите третье число: ')
if a > b and a > c:
    print("min = ", a)
elif a > b < c:
    print("min", b)
elif a > c < b:
    print("max",c)
 
if b < a > c:
    print("max = ", a)
elif a < b > c:
    print("max = ", b)
elif a < c > b:
    print("min = ", c)
