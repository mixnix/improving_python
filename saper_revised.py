# import copy

# BOARD_WIDTH = 3
# BOARD_HEIGHT = 3

# def generate_row():
#     return [' ' for x in range(BOARD_WIDTH)]

# def generate_board():
#     return [generate_row() for x in range(BOARD_HEIGHT)]


# b1 = generate_board() # <-- lista list
# # b2 = list(b1)  # nowę listę (ale tych samych list)

# b2 = copy.deepcopy(b1)

# b2[0][0] = 9
# b2.append(100)

# print(b1)


import random

BOARD_WIDTH = 10
BOARD_HEIGHT = 8
MINES = 10

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
    return [' ' for x in range(BOARD_WIDTH)]


def generate_board():
    return [generate_empty_row() for x in range(BOARD_HEIGHT)]


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


# def convert_positions_to_cords(positions):
#     cords = []
#     for pos in positions:
#         cords.append(make_cord(pos))
#     return cords


MINE_SYMBOL = 'O'


def fill_board_with_mines(empty_board):
    ten_random_positions = rand_positions(10)
    ten_random_cords = convert_positions_to_cords(ten_random_positions)
    for cord in ten_random_cords:
        empty_board[cord['row']][cord['col']] = MINE_SYMBOL
    return empty_board


# def generate_board():
#     return empty_board, board_with_mines


# public_board
# private_board

def make_game():
    board = generate_board()
    board_with_mines = fill_board_with_mines(generate_board())  # list(board)
    return {"player_view": board, "board": board_with_mines}  # <---


# KONTAKT ZE ŚWIATEM

def make_move(game):
    pass


def is_game_ended(game):
    pass


def run_game(game):
    make_move(game)
    if is_game_ended(game):
        pass


def main():
    game = make_game()  # <--- lokalna
    run_game(game)


if __name__ == "__main__":
    main()
