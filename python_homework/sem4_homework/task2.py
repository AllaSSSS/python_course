# Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.

N = int(input("Введите число: "))
lst = []

def Factoring(n):
    for i in range (2, n+1):
        while n % i == 0: 
            lst.append(str(i))
            n //= i
    return lst

print(" * ".join (Factoring(N)))
