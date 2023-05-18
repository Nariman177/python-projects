def main():
    infile = open('students.txt','r')
    num1 = int(infile.readline()) 
    num2 = int(infile.readline())
    num3 = int(infile.readline())
    infile.close() 
    total = num1 + num2 + num3
    print ('Сандар:', num1, num2, num3)
    print('Олардың қосындысы:', total)
main()
