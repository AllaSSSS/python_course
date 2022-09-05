#Реализуйте алгоритм перемешивания списка.

import random
from random import randint
list_1 = []
for i in range(10):
    list_1.append(randint(-100, 100))
print(list_1)
random.shuffle(list_1)
print(list_1)

list_2 = ['каждый', 'охотник', 'желает', 'знать', 'где', 'сидит', 'фазан']
print(list_2)
random.shuffle(list_2)
print(list_2)