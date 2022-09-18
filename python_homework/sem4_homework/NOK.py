
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

def Find_GCD(a, b): # GCD = greatest common divisor
    while a != b:
        print(a, " ", b)
        if a > b: a -= b
        else: b -= a
    return a

print("Наименьшее общее кратное чисел", a, "и", b, "равно", a * b // Find_GCD(a, b))

# x = int(input('Введите первое число: ')) 
# y = int(input('Введите второе число: ')) 
# if x > y: k = x
# else: k = y
# while(True):
#     if (k % x == 0) and (k % y == 0):
#         res = k
#         break
#     k += 1
# print(f'Наименьшее общее кратное двух чисел равно: {res}')

