from    random  import randint
N = 20
A = [0]*N
count = 0
for i in range(N):
    A[i] = randint(10,100)
for i in range(N):    
    print("A[",i,"]=", A[i])
for i in range(N):  
   if (A[i] + A[i]) % 3 == 0:
       count += 1
print(count)
