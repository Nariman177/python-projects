def sum(*numbers):
    result = 1
    for n in numbers:
        result = result * n
    print(f"sum = {result}")
 
 
sum(-1, 2, 4, -6, 7, 20, 30, -5, 4, 1)
