# Игра в конфеты. Бот с интеллектом

from random2 import randint
current_move = randint(0, 1) # 0 - игрок, 1 - бот

print('Первым будет ходить' + (' игрок' if current_move == 0 else ' компьютер'))

remainder = 2021

while True:
    player = current_move % 2
    if player == 0:
        move = int(input('Очередь игрока. Сколько конфет вы возьмете? '))
        if move > 28 or move < 1 or move > remainder: 
            print('Вы ввели неверное число. Попробуйте еще раз. ')
            break
        remainder -= move
        print('Вы взяли', move, 'конфет(у, ы). Осталось', remainder)
        if remainder == 0:
            print('Игрок, вы выиграли! Можете забрать все конфеты')
            break
    else:
        move = max(1, remainder % 29)
        remainder -= move
        print('Компьютер взял ', move, ' конфет(у, ы). Осталось', remainder)
        if remainder == 0:
            print('К сожалению, вы проиграли')
            break
    current_move += 1