# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

def Product_pairs(lst):
    product = []
    k = (len(lst)+1) // 2

    for i in range(0, k):
        product.append(lst[i]*lst[len(lst)-1-i])
    return product

print(Product_pairs([2, 3, 4, 5, 6]))
print(Product_pairs([2, 3, 5, 6]))