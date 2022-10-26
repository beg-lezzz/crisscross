from tictactoe import Board


def input_coord(board_now):
    while True:
        r = int(input("Введите номер строки: ")) - 1
        c = int(input("Введите номер столбца: ")) - 1

        add_new = (c, r)

        flag = 0
        if board_now != []:
            for i in board_now:
                if i == add_new:
                    flag = 1
                    print("Клетка уже занята")
            if flag != 1:
                    board_now.append(add_new)
                    return board_now
            else:
                input_coord(board_now)
        else:
            board_now.append(add_new)

        return board_now


def check_win(board_now, player):
    win = [[(0, 0), (0, 1), (0, 2)], 
            [(1, 0), (1, 1), (1, 2)], 
            [(2, 0), (2, 1), (2, 2)], 
            [(0, 0), (1, 0), (2, 0)], 
            [(0, 1), (1, 1), (2, 1)], 
            [(0, 2), (1, 2), (2, 2)], 
            [(0, 0), (1, 1), (2, 2)], 
            [(2, 0), (1, 1), (0, 2)]]

    check_board = []
    if player == 'X':
        for i in range(0, len(board_now), 2):
            check_board.append(board_now[i])
    else:
        for i in range(1, len(board_now), 2):
            check_board.append(board_now[i])


    for i in win:
        counter = 0
        for j in i:
            if j in check_board:
                counter += 1
        if counter == 3:
            return player


def print_board(board_now):
    board = Board(dimensions=(3, 3), x_in_a_row=3)
    if len(board_now) == 0:
        pass
    elif len(board_now) == 1:
        board.push(board_now[0])
    else:
        for i in board_now:
            board.push(i)
    print(board)


def main():
    board_now = []
    for i in range(9):
        if i % 2:
            player = 'O'
        else:
            player = 'X'
        print_board(board_now)
        print('Ход игрока ' + player)
        board_now = input_coord(board_now)
        if check_win(board_now, player) == None and i == 8:
            print_board(board_now)
            print('\nПобедила дружба')
            break
        elif check_win(board_now, player) == None:
            continue
        else:
            print_board(board_now)
            print(f'\nПобедил {player}')
            break


main()
