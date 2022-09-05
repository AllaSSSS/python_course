#Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
#Найдите произведение элементов на указанных позициях. 
#Позиции хранятся в файле file.txt в одной строке одно число.

from random import randint

N = int(input('Введите число: '))
numbers = []
for i in range(N):
    numbers.append(randint(-N, N+1))
print(numbers)

