A = int(input("введите количество учеников:  "))
for c in range(1,A+1):
    print(c, end =" ")
    N = int(input("введите рост ученика:  "))
    
    if N >= 140:
        print ("Аласа емес окушы")
    if N < 140:
        print("Аласа бойлы")
