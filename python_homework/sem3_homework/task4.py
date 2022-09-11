# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

def DecToBin(number):
    binary = ''
    while number > 0:
        binary += str(number % 2)
        number //= 2
    return binary

print(DecToBin(45))
print(DecToBin(3))
print(DecToBin(2))

# def DecToBin(n):
#     if n==0: return ''
#     else:
#         return DecToBin(n//2) + str(n%2)