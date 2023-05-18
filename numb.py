def main():
    num_days = int(input('Неше күндік сатылым есептеледі?  '))
    sales_file = open('students.txt', 'w')
    for count in range(0, num_days + 1):
        sales = float(input('№' + str(count) + 'күнгі сатылым мөлшерін енгіз: ')) 
        sales_file.write(str(sales) + '\n') 
    sales_file.close()
    print('Мәліметтер students.txt файлына жазылады')
main()
    
    
