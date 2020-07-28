# obiekt:
#

# 1. globalne, które zmieniamy są problematyczne
SYMBOL_CROSS = 'X'
SYMBOL_CIRCLE = 'O'


# LOGIKA

def make_board():
    return [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ]


def make_move(board, pos, symbol):
    row, col = pos
    board[row][col] = symbol


def is_line(board, symbol):
    pass


# symbol gracza albo None

def get_winner(board):
    if is_line(board, SYMBOL_CROSS):
        return SYMBOL_CROSS
    elif is_line(board, SYMBOL_CIRCLE):
        return SYMBOL_CIRCLE
    else:
        return None


def make_history():
    return None


def is_end(game):
    pass


def make_game():
    return {
        'board': make_board(),
        'history': make_history()
    }


# KONTAKT ZE ŚWIATEM


def get_valid_number_from_user():
    while True:
        text = input()


def get_valid_position_from_user():
    while True:
        number = get_valid_number_from_user()


def make_move(game):
    # komunikat

    pos = get_valid_position_from_user()


def print_game(game):
    board = game['board']
    print_board(board)


def run_game(game):
    while True:
        print_game(game)  # pokazuje plansze, i komunikaty dla usera
        make_move(game)


def main():
    game = make_game()  # <--- lokalna
    run_game(game)

# 1 2 3
# 4 5 6
# 7 8 9