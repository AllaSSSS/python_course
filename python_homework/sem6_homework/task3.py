# 3. Напишите программу для проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

table = list([bool(x & 4), bool(x & 2), bool(x & 1)] for x in range(8))
print(table)
a = (not (x[0] or x[1] or x[2]) for x in table)
b = ((not x[0] and not x[1] and not x[2]) for x in table)
print(sum(map(lambda y: 1, filter(lambda x: (x[0] == x[1]), zip(a, b)))) == 8)