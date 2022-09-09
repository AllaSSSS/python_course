# Напишите функцию to_dict(lst), которая принимает аргумент в виде списка и возвращает словарь, 
# в котором каждый элемент списка является и ключом и значением. 
# Предполагается, что элементы списка будут соответствовать правилам задания ключей в словарях.
# Тесты
# print(to_dict([1, 2, 3, 4]))
# print(to_dict(['grey', (2, 17), 3.11, -4]))

def to_dict(lst):
    return {element: element for element in lst}

# Тесты
print(to_dict([1, 2, 3, 4]))
#print(to_dict(['grey', (2, 17), 3.11, -4])