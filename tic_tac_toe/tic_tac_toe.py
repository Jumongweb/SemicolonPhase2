board = ['-', '-', '-',
         '-', '-', '-',
         '-', '-', '-']


def print_game(board):
    print(board[0] + '|' + board[1] + '|' + board[2])
    print("-----")
    print(board[3] + '|' + board[4] + '|' + board[5])
    print("-----")
    print(board[6] + '|' + board[7] + '|' + board[8])


player_one_symbol = 'X'
# player_two_symbol = 'O'
# def prompt_player():
#     player_one_move = input("Player_one. Enter your move: ")
#     player_two_move = input("player_two. Enter your move: ")
player_move = input('Enter your move: ').upper()


def mark_board(board, player_symbol):
    try:
        match player_move:
            case 1:
                board[0] = player_symbol
            case 2:
                board[1] = player_symbol
            case 3:
                board[2] = player_symbol
            case 4:
                board[3] = player_symbol
            case 5:
                board[4] = player_symbol
            case 6:
                board[5] = player_symbol
            case 7:
                board[6] = player_symbol
            case 8:
                board[7] = player_symbol
            case 9:
                board[8] = player_symbol
    except ValueError:
        print("Invalid. Entry should be a number between 1 - 9")
    mark_board(board, player_symbol)
