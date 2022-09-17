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

    