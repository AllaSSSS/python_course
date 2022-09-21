# 2. Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# right_move = 50 % 29
# print('Первым ходом нужно брать ' + str(right_move) + ' конфет')

# #Игра
# remainder = 2021

# while remainder != 0:
#     for i in range (1, 3):
#         move = int(input('Очередь ' + str(i) + '-го игрока. ' + 'Сколько конфет вы возьмете? '))
#         if move > 28 or move < 1 or move > remainder: 
#             print('Вы ввели неверное число. Попробуйте еще раз. ')
#             break
#         remainder -= move
#         print('Вы взяли', move, 'конфет(у, ы). Осталось', remainder)
#         if remainder == 0:
#             print(str(i) + '-й игрок, вы выиграли! Можете забрать все конфеты')
#             break

# a) Добавьте игру против бота

# from random import randint
# current_move = randint(0, 1) # 0 - игрок, 1 - бот

# remainder = 2021
# print('Первым будет ходить' + (' игрок' if current_move == 0 else ' компьютер'))

# while True:
#     player = current_move % 2
#     if player == 0:
#         move = int(input('Очередь игрока. Сколько конфет вы возьмете? '))
#         if move > 28 or move < 1 or move > remainder: 
#             print('Вы ввели неверное число. Попробуйте еще раз. ')
#             break
#         remainder -= move
#         print('Вы взяли', move, 'конфет(у, ы). Осталось', remainder)
#         if remainder == 0:
#             print('Игрок, вы выиграли! Можете забрать все конфеты')
#             break
#     else:
#         move = randint(1, 29)
#         remainder -= move
#         print('Компьютер взял ', move, ' конфет(у, ы). Осталось', remainder)
#         if remainder == 0:
#             print('К сожалению, вы проиграли')
#             break
#     current_move += 1


# b) Подумайте как наделить бота "интеллектом"

from random import randint
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