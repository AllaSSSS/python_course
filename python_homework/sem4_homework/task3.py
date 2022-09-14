# Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

import random
from random import randint
lst = []
for i in range(15):
    lst.append(randint(0, 10))
print(lst)

def Create_list(orig_lst):
    new_list = []
    for i in orig_lst:
        if orig_lst.count(i) == 1:
            new_list.append(i)
    return new_list

print(Create_list(lst))