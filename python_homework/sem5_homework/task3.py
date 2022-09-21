#3.Создайте программу для игры в "Крестики-нолики".

board = list(range(1, 10))
moves = list(range(0, 9))

lines = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]

def draw_board(board):
    print('-------------')
    off = 0
    for i in range(3):
        row = i*3
        print("|", board[row + 0], "|", board[row + 1], "|", board[row + 2], "|")
        print("-------------")

draw_board(board)

for n in range (0, 10):
    i = n%2
    while True:
        m = int(input('Ход ' + str(i+1) + '-го игрока: '))-1
        if m in moves: break
        print('Клетка не доступна')
    sign = 'X' if i == 0 else 'O'
    board[m] = sign
    draw_board(board)
    moves.remove(m)
    win = False
    for l in lines:
        if board[l[0]] == sign and board[l[1]] == sign and board[l[2]] == sign:
            win = True
            break
    if win:
        print(str(i+1) + '-й игрок победил!')
        break
    if len(moves) == 0:
        print('Ничья')
        break

