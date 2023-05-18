from random import randint
max=0
min = 0
Avg = 0
sum = 0
n = 0
a = 0
for i in range(20):
     b=randint(0,200)
     sum = sum + b
     n = n + 1
     if b > max: max=b
     if b < min: min=b
     if b > 0:
          a=a + b
     print (b)

Avg = sum / n
print("Max = ", max)
print("Min = ", min)
print("avg = ", Avg)
print("plus = ", a)
     

   



 
