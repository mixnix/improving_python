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


# LOGIKA

def generate_empty_row():
    return [' ' for x in range(BOARD_WIDTH)]


def generate_empty_board():
    return [generate_empty_row() for x in range(BOARD_HEIGHT)]


def get_random_positions(n):
    number_of_positions = BOARD_HEIGHT * BOARD_WIDTH
    possible_positions = list(range(number_of_positions))
    random.shuffle(possible_positions)
    return [possible_positions.pop() for i in range(n)]


def convert_positions_to_cords(random_positions):
    return [{"row": (pos - 1) // BOARD_WIDTH, "col": (pos - 1) % BOARD_HEIGHT} for pos in random_positions]


def fill_board_with_mines(empty_board):
    ten_random_positions = get_random_positions(10)
    ten_random_cords = convert_positions_to_cords(ten_random_positions)
    for cord in ten_random_cords:
        empty_board[cord['row']][cord['col']] = 'O'
    return empty_board


def generate_board():
    empty_board = generate_empty_board()
    board_with_mines = fill_board_with_mines(list(empty_board))
    return empty_board, board_with_mines


def make_game():
    player_view, board = generate_board()
    return {"player_view": player_view, "board": board}


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
