# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов

def create_poly_file (name):
    from random import randint
    polynomial = []
    degree = randint(1, 10)
    number = randint(-10, 10)
    for i in range(degree, 0):
        polynomial.append(str(number) + "*x^" + str(degree))
    
with open ('name', 'w') as file:
    file.write()
