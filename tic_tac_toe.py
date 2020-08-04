# obiekt:
#
import random
import math
# 1. globalne, które zmieniamy są problematyczne
SYMBOL_CROSS = 'X'
SYMBOL_CIRCLE = 'O'
WINNING_POSITIONS = [[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9],
                     [1, 4, 7],
                     [2, 5, 8],
                     [3, 6, 9],
                     [1, 5, 9],
                     [3, 5, 7]]

# LOGIKA

def make_board():
    return [
        ['1', '2', '3'],
        ['4', '5', '6'],
        ['7', '8', '9']
    ]

def convert_position_to_coordinates(pos):
    row = (pos-1) // 3
    col = (pos-1) % 3
    return row, col

def make_move_to_position(board, pos, symbol):
    row, col = convert_position_to_coordinates(pos)
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

def toss_a_coin():
    random_bit = random.getrandbits(1)
    return bool(random_bit)

def make_game():
    return {
        'board': make_board(),
        'history': make_history(),
        'is_current_player_cross': toss_a_coin()
    }


# KONTAKT ZE ŚWIATEM


def get_valid_number_from_user():
    while True:
        user_input = input()
        try:
            return int(user_input)
        except ValueError:
            print("That's not an int! Try again")

def flatten_board(board):
    return [item for sublist in board for item in sublist]

def is_position_taken(board, number):
    flat_list = flatten_board(board)
    return str(number) not in flat_list

def is_position_valid(board, number):
    return number >= 1 and number <= 9 and not is_position_taken(board, number)

def get_valid_position_from_user(board):
    while True:
        number = get_valid_number_from_user()
        if(is_position_valid(board, number)):
            return number
        else:
            # Czy tutaj nie powinienem napisac czy chodzi o to, że jest out of range czy o to, że pozycja jest już zajęta?
            print("Position is not valid, try again.")


def print_make_move_prompt(game):
    current_player = "Cross" if game['is_current_player_cross'] == True else 'Circle'
    print("\nIt's " + current_player + " turn.")
    print("Enter where you want to make a move: ", end="")

def get_current_player_symbol(game):
    if game['is_current_player_cross']:
        return 'X'
    else:
        return 'O'

def make_move(game):
    print_make_move_prompt(game)

    pos = get_valid_position_from_user(game['board'])
    make_move_to_position(game['board'], pos, get_current_player_symbol(game))



def print_row(i, row):
    for element in row:
        print(element, end="")
    print()

def print_board(board):
    for i, row in enumerate(board):
        print_row(i, row)

def print_game(game):
    board = game['board']
    print_board(board)

def get_symbol_from_pos(board, pos):
    row, col = convert_position_to_coordinates(pos)
    return board[row][col]

def check_if_position_has_three_of_a_kind_symbols(position, board):
    three_symbols = []
    for pos in position:
        three_symbols.append(get_symbol_from_pos(board, pos))

    if all(elem == three_symbols[0] for elem in three_symbols):
        return True


def is_won(board):
    for position in WINNING_POSITIONS:
        if check_if_position_has_three_of_a_kind_symbols(position, board):
            return True
    return False

def get_winning_player_name(game):
    return get_current_player_symbol(game)

def check_if_game_ended(game):
    if(is_won(game['board'])):
        print("Player: " + get_winning_player_name(game) + " won!")

def change_players(game):
    game['is_current_player_cross'] = not game['is_current_player_cross']

def run_game(game):
    while True:
        print_game(game)  # pokazuje plansze, i komunikaty dla usera
        make_move(game)
        check_if_game_ended(game)
        change_players(game)


def main():
    game = make_game()  # <--- lokalna
    run_game(game)

if __name__ == "__main__":
    main()

# 1 2 3
# 4 5 6
# 7 8 9