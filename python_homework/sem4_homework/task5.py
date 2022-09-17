# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов


def get_list(file):
    with open (file, 'r') as f:
        lst = []
        for line in f:
            line = line.replace("+ ", "")
            line = line.replace("- ", "-")
            for word in line.split(' '):
                lst.append(word)
        return lst

lst1 = get_list('polyfile1.txt')
lst2 = get_list('polyfile2.txt')
print(lst1)
print(lst2)

def get_items(lst):
    items = [0] * 10
    for i in range(len(lst)-1, -1, -1):
        x = lst[i]
        if '*x^' in x:
            parts = x.split('*x^') # 8*x^7 => ['8', '7']
            coef  = int(parts[0])
            index = int(parts[1])
            items[index] = coef
        elif x.endswith('*x'):
            items[1] = int(x[:-2])
        else:
            items[0] = int(x)

    return items

def format_polynomial(coefs):
    output = ""
    for i in range(len(coefs)-1, -1, -1):
        c = coefs[i]
        if c != 0: 
            if output != "": output += (" + " if c > 0 else " - ")
            else:
                if c < 0: output += "-"
            if c != 1 and c != -1: 
                output += str(abs(c))
                if i > 0: output += "*"   
            if i > 0: output += ("x" if i == 1 else "x^" + str(i))
    return output


add1 = get_items(lst1)
add2 = get_items(lst2)

sum = []
for i in range(10):
    sum.append(add1[i] + add2[i])
print(format_polynomial(add1))
print(format_polynomial(add2))  
print(format_polynomial(sum))

with open ('poly_sum.txt', 'w') as file:
    file.write(format_polynomial(sum))

# lst_sum = max(lst1, lst2)
# print(len(lst_sum))

    



# from ast import pattern
# import re

#from task4 import *

# p = "+8*x^3 - 10*x + 2"
# p = "8*x^3 - 7*x^2 + 10*x + 2"
# p = p.replace(" ", "")

# # if p[0] != '+' and p[0] != '-':
# #     p = '+' + p

# print(p)

# pattern = re.compile(r'([\+\-]?[0-9]+)(\*x(?:\^([0-9]+))?)?')

# for match in re.finditer(pattern, p):
#     idx = match.group(3)
#     if idx == None: idx = 0 if match.group(2) == None else 1
#     print(match.group(1), " ^", idx)





# def parse_polynomial(s):
#     return re.split('\s+\+\-')


# k = int(input("Задайте степень k: "))
# c1 = create_polynomial(k)
# c2 = create_polynomial(k)
# c_sum = []

# for i in range(0, k+1):
#     c_sum.append(c1[i] + c2[i])

# print(c1)
# print(c2)
# print(c_sum)
    
# with open ('polyfile1', 'w') as file:
#     file.write(format_polynomial())
