#Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
#Пример: - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


from functools import reduce

def sum_all(n):
    return list(reduce(lambda x, y: (x * y), range(1, k+1)) for k in range(1, n+1))

print(sum_all(3))
print(sum_all(4))