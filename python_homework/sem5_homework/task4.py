# 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Кодирование длин серий (RLE) — это простая форма сжатия данных без потерь, 
# которая выполняется для последовательностей с одним и тем же значением, 
# повторяющимся много раз подряд.

import re

def compress(txt):
    output = ''
    last_char = ''
    count = 0
    for c in txt:
        if c == last_char:
            count += 1
        else:
            if count > 0:
                output += str(count) + last_char
            last_char = c
            count = 1
    if count > 0:
        output += str(count) + last_char
    return output

def decompress(comp):
    output = ''
    matcher = re.compile(r'(\d+)([\wа-яА-ЯёЁ])')
    for match in matcher.finditer(comp):
        count = int(match.group(1))
        char = match.group(2)
        output += char * count
    return output

print(compress('dddkkkkkkkkyffff'))
print(decompress('3d8k1y4f'))
print(decompress('3а5г8ю'))