import io
word = u'Sattar'
with io.open('students.txt', encoding='utf-8') as file:
    for line in file:
        if word in line:
             print(line, end = ' ')
