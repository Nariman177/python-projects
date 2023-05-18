from    random  import randint
N = 20     
A = [0]*N
count = 0
for i in range(N):
    A[i] = randint(0,200)
for i in range(N):
    print("A[",i,"]=", A[i])
B = [x for x in A
     if x % 10 == 0]
print(len(B))



