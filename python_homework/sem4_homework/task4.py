# Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример: - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0  

k = int(input("Задайте степень k: "))

import ast
import random
from random import randint
coefficients = []
for i in range(k+1):
    coefficients.append(randint(-10, +10))
print(coefficients)

output = ""
for i in range(k, -1, -1):
    c = coefficients[i]
    if c != 0: 
        if output != "": output += (" + " if c > 0 else " - ")
        else:
            if c < 0: output += "-"
        if c != 1 and c != -1: 
            output += str(abs(c))
            if i > 0: output += "*"   
        if i > 0: output += ("x" if i == 1 else "x^" + str(i))

print(output)

with open ('polynomials.txt', 'w') as file:
    file.write(output)
#for i in range(k, 0, -1):
#     c = coefficients[i]
#     if c != 0:
#         file.write(str(c) + "*x^" + str(i))
# if coefficients[0] != 0: file.write(str(coefficients[0]))
# file(close)

    