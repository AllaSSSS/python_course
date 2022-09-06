#Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
#Найдите произведение элементов на указанных позициях. 
#Позиции хранятся в файле file.txt в одной строке одно число.

from random import randint
N = int(input('Введите число: '))
numbers = []
for i in range(N):
    numbers.append(randint(-N, N))
print(numbers)

product = 1
with open('file.txt') as file:
    for pos in file:
        if int(pos) <= N and int(pos) >= -N:
            product *= numbers[int(pos)]
        else: product *= 1
print(product)