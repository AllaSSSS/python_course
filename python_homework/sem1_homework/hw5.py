# Напишите программу, которая принимает на вход координаты двух точек и 
# находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

import math
xA = float(input('Введите координату x точки A: '))
yA = float(input('Введите координату y точки A: '))
xB = float(input('Введите координату x точки B: '))
yB = float(input('Введите координату y точки B: '))
print('Расстояние между точками равно: %.2f'% math.sqrt((xB - xA)**2 + (yB - yA)**2))