from    random  import randint
N = 20
A = [0]*N
for i in range(N):
    A[i] = randint(0,200)
for i in range(N):    
    print("A[",i,"]=", A[i])
for i in A:
    if 9 < i < 100:
        print("Двухзначные Чисда ", i)
        









        
        

