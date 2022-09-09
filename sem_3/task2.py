# В текстовом файле посчитать количество строк, 
# а также для каждой отдельной строки определить количество в ней символов и слов.

from audioop import lin2alaw


lines = 0
with open('/Users/allasoloveva/Desktop/Geek/python_VSD/python_course/sem_3/file1.txt') as file:
    for line in file:
        lines += 1
        symbols = 0
        words = 0
        for s in line:
            symbols += 1
            if s != ' ' and symbols == 0:
                words += 1
                symbols = 1
            elif s == ' ':
                symbols = 0               
        print(len(line.rstrip()))
print('Общее количество строк ', lines)
#print(len(line))
print(words)

f = open('textfile.txt','r')
countLines = 0
countwordsInLines = []
countCharsInLines = []
for line in f:
    countLines+=1
    if line != '\n':
        countwordsInLines.append(line.count(' ') + 1)
    else:
        countwordsInLines.append(0)
    countCharsInLines.append(line.count('') -2)
f.close()
print(countLines)
print(countwordsInLines)
print(countCharsInLines)

# f = open('article.txt','r')
# line = 0
# for i in f:
#     line += 1
#
#     flag = 0
#     word = 0
#     for j in i:
#         if j != ' ' and flag == 0:
#             word += 1
#             flag = 1
#         elif j == ' ':
#             flag = 0
#
#     print(len(i), 'симв.', word, 'сл.')
# print(line, 'стр.')
# f.close()