# 1. Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

def multiply_pairs(lst):
    l = len(lst)
    return list(map(lambda x, y: lst[x] * lst[y],
        list(range(0, (l+1)//2)),
        list(range(l-1, 0, -1))))


print(multiply_pairs([2, 3, 4, 5, 6]))
print(multiply_pairs([2, 3, 5, 6]))
