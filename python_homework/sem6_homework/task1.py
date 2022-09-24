# Дана последовательность чисел. 
# Получить список уникальных элементов заданной последовательности.
# Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]

lst = [1, 2, 3, 5, 1, 5, 3, 10]
result = list(filter(lambda x: sum(y == x for y in lst) == 1, lst))
print(result)