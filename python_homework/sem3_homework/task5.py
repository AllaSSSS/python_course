# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так:
#  [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

def Fibo(n):
    if n < 0:
        if n % 2 != 0: 
            return Fibo(-n) 
        else:
            return -Fibo(-n)
    if n < 2: return n
    else: 
        return Fibo(n-2) + Fibo(n-1)

def ListFibo(k):
    arr = []
    for i in range(-k, k+1):
        arr.append(str(Fibo(i)))
    return arr

print(', '.join(ListFibo(8)))