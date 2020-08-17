import random

BOARD_WIDTH = 10
BOARD_HEIGHT = 8
MINES = 10
MINE_SYMBOL = 'O'
EMPTY_FIELD_SYMBOL = 'E'
# pierwsza wspolrzedna to y a druga to x

'''
  1 2 3 4 5 6 7 8 9 10
a 
b
c
d
e
f
g
h

'''


# KONTAKT ZE ŚWIATEM

# LOGIKA


def generate_row():
    return [EMPTY_FIELD_SYMBOL for x in range(BOARD_WIDTH)]


def generate_board():
    return [generate_row() for x in range(BOARD_HEIGHT)]


def rand_positions(n):
    size = BOARD_HEIGHT * BOARD_WIDTH
    positions = list(range(size))
    random.shuffle(positions)
    return positions[:n]


def to_cords(positions):
    cords = []
    for pos in positions:
        row = (pos - 1) // BOARD_WIDTH
        col = (pos - 1) % BOARD_HEIGHT
        cord = (row, col)
        cords.append(cord)
    return cords





def fill_board_with_mines(empty_board):
    ten_random_positions = rand_positions(10)
    ten_random_cords = to_cords(ten_random_positions)
    for cord in ten_random_cords:
        empty_board[cord[0]][cord[1]] = MINE_SYMBOL
    return empty_board


def make_game():
    board = generate_board()
    board_with_mines = fill_board_with_mines(generate_board())  # list(board)
    return {"player_view": board, "board": board_with_mines}  # <---


# KONTAKT ZE ŚWIATEM

def show_row(row):
    for symbol in row:
        print(symbol, end=' ')
    print()

def show_board(player_view):
    print('   1 2 3 4 5 6 7 8 9 10')
    column_letters = list('ABCDEFGHIJ')
    for row in player_view:
        print(column_letters.pop(0), end='  ')
        show_row(row)


def make_move(game):
    pass


def is_game_ended(game):
    pass


def run_game(game):
    show_board(game['player_view'])
    make_move(game)
    if is_game_ended(game):
        pass


def main():
    game = make_game()  # <--- lokalna
    run_game(game)


if __name__ == "__main__":
    main()
