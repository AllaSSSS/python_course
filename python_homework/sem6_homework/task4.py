#Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#Пример: - 6782 -> 23; - 0,56 -> 11

def sum_digits(n):
    return sum(int(x) for x in filter(lambda x: x.isdigit(), (i for i in str(n))))

print(sum_digits(6782))
print(sum_digits(0.56))