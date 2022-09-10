# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением 
# дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

def Fraction(x): 
    return x - int(x)

def Diff_max_min(lst):
     max = Fraction(lst[0])
     min = Fraction(lst[0])
     for i in range(0, len(lst)):
        f = Fraction(lst[i])
        if f > max: max = f
        if f < min: min = f
     return (max-min)

result = Diff_max_min([1.1, 1.2, 3.1, 5, 10.01])
print("%.2f" % Diff_max_min([1.1, 1.2, 3.1, 5, 10.01])) 
print(int(result*100)/100)
