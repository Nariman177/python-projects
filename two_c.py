def main () :
    first_friends = int(input('Сіздің көрші достарыңыз қанша: '))
    second_friends = int(input("Мектепте қанша досыңыз бар: "))
    total = sum(first_friends, second_friends)
    print('Сіздің барлығы ', total, 'досыңыз бар.')
def sum(num1, num2):
    return num1 + num2
main ()
