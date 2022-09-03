# Напишите программу для проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

result = True
for x in range (2):
    for y in range (2):
        for z in range (2):
            #print(x, " ", y, " ", z)
            if not (x or y or z) != (not x and not y and not z):
                result = False
                break
print(result)