import random

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
POTENTIAL_SYMBOLS = [SYMBOL_CIRCLE, SYMBOL_CROSS]


# LOGIKA

def make_board():
    return [
        ['1', '2', '3'],
        ['4', '5', '6'],
        ['7', '8', '9']
    ]


def convert_position_to_coordinates(pos):
    row = (pos - 1) // 3
    col = (pos - 1) % 3
    return row, col


def make_move_to_position(board, pos, symbol):
    row, col = convert_position_to_coordinates(pos)
    board[row][col] = symbol


# def make_queue(a, b):
#     return [a, b]

# def rotate(queue):
#     a, b = queue
#     queue[0] = b
#     queue[1] = a

# symbol gracza albo None


# 1. wybieramy listę
# 2. słownik jako struktura dla pojedynczego zdarzenia (jakie trzymamy w liscie)


def make_history():
    return None


def get_starting_player_symbol(potential_symbols):
    return random.choice(potential_symbols)


def get_initial_next_symbols(current_symbol, potential_symbols):
    copy = list(potential_symbols)
    copy.remove(current_symbol)
    return copy


def make_game():
    initial_state = {
        'board': make_board(),
        'history': make_history(),
        # todo: powtarzanie funkcjonalnosci kolejnosci
        'current_symbol': get_starting_player_symbol(POTENTIAL_SYMBOLS)  # ???
    }

    # todo: w prostszy sposob zaimplementowac kolejke
    initial_state['next_symbols'] = get_initial_next_symbols(initial_state['current_symbol'], POTENTIAL_SYMBOLS)

    # initial_state['queue'] = make_queue(SYMBOL_CIRCLE, SYMBOL_CROSS)

    return initial_state


# todo: te funkcje (is_game_ended, is_line, change_players) sa logika
# i kilka nastepnych
def is_game_ended(game):
    for line_positions in WINNING_POSITIONS:
        if is_line(game, line_positions):
            return True
    return False


def change_players(game):
    game['next_symbols'].append(game['current_symbol'])
    game['current_symbol'] = game['next_symbols'].pop(0)


def is_line(game, line):
    for place in line:
        row, col = convert_position_to_coordinates(place)
        if game['board'][row][col] != game['current_symbol']:
            return False
        # board[]
    return True


def get_symbol_from_pos(board, pos):
    row, col = convert_position_to_coordinates(pos)
    return board[row][col]


def check_if_position_has_three_of_a_kind_symbols(position, board):
    three_symbols = []
    for pos in position:
        three_symbols.append(get_symbol_from_pos(board, pos))

    return all(elem == three_symbols[0] for elem in three_symbols)


def is_position_valid(board, number):
    return (
            1 <= number <= 9 and
            not is_position_taken(board, number)
    )


def flatten_board(board):
    return [item for sublist in board for item in sublist]


def is_position_taken(board, number):
    row, col = convert_position_to_coordinates(number)
    return not board[row][col].isdigit()


# KONTAKT ZE ŚWIATEM


def get_valid_number_from_user():
    while True:
        user_input = input()
        try:
            return int(user_input)
        except ValueError:
            print("That's not an int! Try again")

    # flat_list = flatten_board(board)
    # return str(number) not in flat_list


def get_valid_position_from_user(board):
    while True:
        number = get_valid_number_from_user()
        if is_position_valid(board, number):
            return number
        else:
            # Czy tutaj nie powinienem napisac czy chodzi o to, że jest out of range czy o to, że pozycja jest już zajęta?
            print("Position is not valid, try again.")


def player_prompt(symbol):
    return (
            "It's " + symbol + " turn.\n" +
            "Enter where you want to make a move: "
    )


def make_move(game):
    print(player_prompt(game['current_symbol']))

    pos = get_valid_position_from_user(game['board'])
    make_move_to_position(game['board'], pos, game['current_symbol'])


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


def end_game(game):
    print_win_status(game)
    exit()  # todo: <--- lepiej przesunąć gdzieś indziej


def print_win_status(game):
    print("Player: " + game['current_symbol'] + " won!")


# def get_winner(board):
#     if is_line(board, SYMBOL_CROSS):
#         return SYMBOL_CROSS
#     elif is_line(board, SYMBOL_CIRCLE):
#         return SYMBOL_CIRCLE
#     else:
#         return None


def run_game(game):
    while True:
        print_game(game)  # pokazuje plansze, i komunikaty dla usera
        make_move(game)
        if is_game_ended(game):
            end_game(game)
        change_players(game)


def main():
    game = make_game()  # <--- lokalna
    run_game(game)


if __name__ == "__main__":
    main()


# 1 2 3
# 4 5 6
# 7 8 9


# TESTY PY.TEST


def test_is_position_valid():
    assert is_position_valid(make_board('''X__O__X__'''), 2)
    assert is_position_valid(make_board('''X__O__X__'''), 2)
    assert is_position_valid(make_board('''X__O__X__'''), 2)
    assert is_position_valid(make_board('''X__O__X__'''), 2)



