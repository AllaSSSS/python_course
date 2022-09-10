# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением 
# дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

def Frac_part(x):       # Получение дробной части числа
    return (x - int(x))

def Diff_max_min (lst):
    max = Frac_part(lst[0])
    min = Frac_part(lst[0])
    for i in range(0, len(lst)):
        f = Frac_part(lst[i])
        if f > max: max = f   
        if f < min: min = f
    return (max-min)

print("%.2f" % Diff_max_min([1.1, 1.2, 3.1, 5, 10.01])) # Результат при 5 = float (логичный)

result = Diff_max_min([1.1, 1.2, 3.1, 5, 10.01])    
print(int(result*100)/100)                              # Результат, как в примере
