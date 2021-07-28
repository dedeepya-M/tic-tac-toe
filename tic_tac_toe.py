import random

game_on = True
winner = None
board = ["_", "_", "_",
         "_", "_", "_",
         "_", "_", "_"]
lis = [0, 1, 2, 3, 4, 5, 6, 7, 8]
#l1 = []


def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2] + "     " + "0" + " | " + "1" + " | " + "2")
    print(board[3] + " | " + board[4] + " | " + board[5] + "     " + "3" + " | " + "4" + " | " + "5")
    print(board[6] + " | " + board[7] + " | " + board[8] + "     " + "6" + " | " + "7" + " | " + "8")


def board1():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


def user_turn():
    global lis
    go = True
    print("your turn:")
    print("enter a value form 0 to 8:")
    pos = int(input())
    while go:
        if pos not in lis:
            print("position already taken !\n enter again:")
            pos = int(input())
        else:
            go = False

    lis.remove(pos)
    #l1.append(pos)
    board[pos] = "X"
    board1()
    return


def comp_turn():
    global lis
    print("my turn")
    pos = random.choice(lis)
    lis.remove(pos)
    #l1.append(pos)
    board[pos] = "O"
    board1()
    return


def check_for_game():
    check_win()
    check_tie()
    return


def check_win():
    global winner
    r_win = check_r()
    c_win = check_col()
    d_win = check_d()
    if r_win:
        winner = r_win
    elif c_win:
        winner = c_win
    elif d_win:
        winner = d_win
    else:
        winner = None
    return


def check_r():
    global game_on
    row_1 = board[0] == board[1] == board[2] and board[0] != "_"
    row_2 = board[3] == board[4] == board[5] and board[3] != "_"
    row_3 = board[6] == board[7] == board[8] and board[6] != "_"

    if row_1 or row_2 or row_3:

        game_on = False
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]

    else:
        return None


def check_col():
    global game_on
    col_1 = board[0] == board[3] == board[6] and board[0] != "_"
    col_2 = board[1] == board[4] == board[7] and board[4] != "_"
    col_3 = board[2] == board[5] == board[8] and board[5] != "_"

    if col_1 or col_2 or col_3:

        game_on = False
    if col_1:
        return board[0]
    elif col_2:
        return board[1]
    elif col_3:
        return board[2]

    else:
        return None


def check_d():
    global game_on
    diagonal_1 = board[0] == board[4] == board[8] and board[0] != "_"
    diagonal_2 = board[2] == board[4] == board[6] and board[2] != "_"
    if diagonal_1 or diagonal_2:

        game_on = False
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[2]

    else:
        return None


def check_tie():
    global game_on
    if "_" not in board:
        game_on = False
    return
def check_to_break():
    if not game_on:
        return 0
    else:
        return 1
def play_game():
    display_board()
    while game_on:
        user_turn()
        check_for_game()
        q = check_to_break()
        if q == 0:
            break
        comp_turn()
        check_for_game()
    if winner == "X":
        print("you won!")
    elif winner == "O":
        print("better luck next time!")
    elif winner is None:
        print("TIE!")


play_game()
