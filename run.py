def game_menu():
    """
    Function to welcome the player to the game and provide intial options
    """
    print("Welcome to Not Battleships\n")
    print("Main Menu")
    print("Play a Game - Press 1")
    print("How to Play - Press 2")
    print("End Program - Press 3")
    while True:
        game_menu_options = input("1, 2, or 3?: \n")
        if len(game_menu_options) !=1 or not game_menu_options.isdigit():
            print("Menu Options are limited to a number between 1 and 3, please")
            continue
            if game_menu_options == 1:
                get_player_name()
            elif game_menu_options == 2:
                print("Boilerplate for game instructions")
                continue
            elif game_menu_options == 3:
                break


def get_player_name():
    """
    Function to get the player's name and return it to the game and validate the input
    """
    while True:
        player_one = input("Please enter your name: \n")
        if len(player_one) <1:                          # make sure user has actually put entered a name
            print("No, really, please enter your name... I want to know the name of the person I'm about to thrash...")
        elif len(player_one) <2:                        # Try to get the user's initials at least
            print("Go on, just your initials will do... Minimum 2 letters, please...")
        elif not player_one.isalpha():                      # ensure that the player has entered letters for their name
            print("Let's stick to letters for the time being, Mr Musk...")
        else:
            return player_one
 

def game_size_option():
    """
    Function to provide the user the choice of game board size and validate the input
    """
    print('What size of game board would you like?')
    print('Press 1 for 4 x 4')
    print('Press 2 for 5 x 5')
    print('Press 3 for 6 x 6')
    while True:
        game_size_option = input("1 / 2 / 3? ")             # ensure the user is only inputting a single digit
        if len(game_size_option) !=1 or not game_size_option.isdigit():
            print("We just need a single number between 1 and 3, please")                                  
        game_size_option = int(game_size_option)
        if game_size_option >=1 or game_size_option <=3:    # ensure the player is inputting a number 1 - 3
            return game_size_option
        else:
            print('Please choose 1, 2 or 3 instead.')       # if input outside numerical options, loop to function start                   


def get_game_size(game_size_option):
    """
    Function to translate the user's choice in to the dimensions of the game board
    """
    if game_size_option == 1:                            # if player inputs 1 then the size = 4 x 4 game board etc.
        game_size = 4
    elif game_size_option == 2:
        game_size = 5
    elif game_size_option == 3:
        game_size = 6
    
    return game_size


def ship_num_option():
    """
    Function to provide the user the choice of how many ships will populate the game board and validate the input
    """
    print('How many ships would you like?')
    print('Press 1 for 4')
    print('Press 2 for 5')
    print('Press 3 for 6')
    while True:
        get_ship_option = input("1 / 2 / 3? ")             # ensure the user is only inputting a single digit
        if len(get_ship_option) !=1 or not get_ship_option.isdigit():
            print("We just need a single number between 1 and 3, please")
        get_ship_option = int(get_ship_option)
        if get_ship_option >=1 or get_ship_option <=3:    # ensure the player is inputting a number 1 - 3
                return get_ship_option
        else:
            print('Please choose 1, 2 or 3 instead.')


def get_ship_num(get_ship_option):
    """
    Function to translate the user's choice in to the number of ships on the game board for the players
    """
    if get_ship_option == 1:                            # if player inputs 1 then the number of ships = 4 etc.
        ship_num = 4
    elif get_ship_option == 2:
        ship_num = 5
    elif get_ship_option == 3:
        ship_num = 6
    
    return ship_num


player_one = get_player_name()

game_size_option = game_size_option()
game_size = get_game_size(game_size_option)

ship_num_option = ship_num_option()
ship_num = get_ship_num(ship_num_option)

print(f'Okay, {player_one}, you want a {game_size} x {game_size} game board with {ship_num} ships. \n')


def build_game_board(game_size):
    """
    Function to build the initial game board based on user's choice
    """
    game_board=[]                           # make the list for the game board(s)
    for row in range(game_size):            # use the user's choice to iterate the rows
        rows = []
        for column in range(game_size):     # use the user's choice to iterate the columns
            rows.append(" - ")              # empty (or secret) spaces on the board markeed with a -
        game_board.append(rows)             # add the newly populated row to the game board
    return game_board

game_board = build_game_board(game_size)
player_board = game_board
computer_board = game_board


def display_current_boards(game_board):
    """
    Function for boilerplate display of a board
    """
    for row in game_board:
        print(" ".join(row))

display_boards = display_current_boards(game_board)
# def start_game():
