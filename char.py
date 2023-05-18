string = "Весна пришла и птицы прилетают"
a = 0
p = 0
for i in string:
    if i != " ":
        a += 1  
p = string.count('а') + string.count('п') 
print("Количество букв = ", a ,"Количество п = ", string.count('п'), "Количество а = ", string.count('а'), "Общее количество = ", p)

 


