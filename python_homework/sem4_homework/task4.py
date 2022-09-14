# Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример: - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0  

k = int(input("Задайте степень k: "))

import random
from random import randint
coefficients = []
for i in range(k+1):
    coefficients.append(randint(0, 100))
print(coefficients)

polynomials = []
for i in range(k, 0, -1):
    c = coefficients[i]
    if c != 0: 
        polynomials.append(str(c) + "*x^" + str(i))
if coefficients[0] != 0: polynomials.append(str(coefficients[0]))

print(" + ".join(polynomials))