# obiekt:
#
import random

# 1. globalne, które zmieniamy są problematyczne
SYMBOL_CROSS = 'X'
SYMBOL_CIRCLE = 'O'


# LOGIKA

def make_board():
    return [
        ['1', '2', '3'],
        ['4', '5', '6'],
        ['7', '8', '9']
    ]


def make_move_to_position(board, pos, symbol):
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


def is_position_taken(game, number):
    flat_list = [int(item) for sublist in game['board'] for item in sublist]
    return number not in flat_list

def is_position_valid(game, number):
    return number >= 1 and number <= 9 and not is_position_taken(game, number)

def get_valid_position_from_user(game):
    while True:
        number = get_valid_number_from_user()
        if(is_position_valid(game, number)):
            return number
        else:
            # Czy tutaj nie powinienem napisac czy chodzi o to, że jest out of range czy o to, że pozycja jest już zajęta?
            print("Position is not valid, try again.")


def print_make_move_prompt(game):
    current_player = "Cross" if game['is_current_player_cross'] == True else 'Circle'
    print("\nIt's " + current_player + " turn.")
    print("Enter where you want to make a move: ", end="")


def make_move(game):
    print_make_move_prompt(game)

    pos = get_valid_position_from_user(game)
    pass



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


def run_game(game):
    while True:
        print_game(game)  # pokazuje plansze, i komunikaty dla usera
        make_move(game)
        check_if_game_ended(game)


def main():
    game = make_game()  # <--- lokalna
    run_game(game)

if __name__ == "__main__":
    main()

# 1 2 3
# 4 5 6
# 7 8 9