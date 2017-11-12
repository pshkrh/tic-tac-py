# Tic Tac Toe in Python
# Author: Pushkar Kurhekar

print("Welcome to Tic Tac Py, a simple Tic Tac Toe game made in Python.")

game_on = True

board = [' '] * 10


def choose_turn():
    player_turn = input("Which player would like to go first? Enter 1 for player 1 or 2 for Player 2.")
    player_turn = str(player_turn)
    return player_turn


def marker():
    mark = raw_input("Does player 1 want to be X or O?").upper()

    if mark == 'X':
        return 'X', 'O'
    else:
        return 'O', 'X'


def clear_board(board):
    del board[:]
    for i in range(0,11):
        board.append(' ')


def display(board):
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')


def set_position(board):
    pos = input("Enter position to place marker. (Between 1 and 9)")
    return pos


def place_marker(board, marker, pos):
    board[pos] = marker


def win(board,mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or  # across the top
            (board[4] == mark and board[5] == mark and board[6] == mark) or  # across the middle
            (board[1] == mark and board[2] == mark and board[3] == mark) or  # across the bottom
            (board[7] == mark and board[4] == mark and board[1] == mark) or  # down the middle
            (board[8] == mark and board[5] == mark and board[2] == mark) or  # down the middle
            (board[9] == mark and board[6] == mark and board[3] == mark) or  # down the right side
            (board[7] == mark and board[5] == mark and board[3] == mark) or  # diagonal
            (board[9] == mark and board[5] == mark and board[1] == mark))  # diagonal


def space_check(board, pos):
    return board[pos] == ' '


def tie(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True


def play():
    global game_on
    turn = choose_turn()

    p1, p2 = marker()

    print("Player " + turn + " will go first.")

    while game_on:
        if turn == "1":
            display(board)
            pos = set_position(board)
            place_marker(board, p1, pos)

            if win(board, p1):
                print("Congratulations, Player 1 has won!")
                game_on = False
                replay(board)
            else:
                if tie(board):
                    print("The game is tied!")
                    game_on = False
                    replay(board)
                else:
                    turn = "2"

        else:
            display(board)
            pos = set_position(board)
            place_marker(board, p2, pos)

            if win(board, p2):
                print("Congratulations, Player 2 has won!")
                game_on = False
                replay(board)
            else:
                if tie(board):
                    print("The game is tied!")
                    game_on = False
                    replay(board)
                else:
                    turn = "1"


def replay(board):
    global game_on
    x = input('Do you want to play again? Enter 1 for Yes, 0 for No: ')
    if x == 1:
        game_on = True
        clear_board(board)
        play()
    else:
        print("Thanks for Playing Tic Tac Py!")


play()