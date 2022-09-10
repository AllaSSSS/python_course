# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

def DecToBinary(number):
    binary = []
    while number > 0:
        binary.append(number % 2)
        number //= 2
    print(binary)

DecToBinary(45)