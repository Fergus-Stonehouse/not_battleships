import random

def game_menu():
    print("Welcome to Not Battleships\n")
    print("Main Menu\n")
    print("Play a Game - Press 1\n")
    print("How to Play - Press 2\n")
    print("End Program - Press 3\n")
    while True:
        game_menu_options = input("1, 2, or 3?: \n")
        if len(game_menu_options) !=1 or not game_menu_options.isdigit():
            print("Menu Options are limited to a number between 1 and 3, please")
            continue

        game_menu_options = int(game_menu_options)

        if game_menu_options >=1 and game_menu_options <=3:
            if game_menu_options == 1:
                break
            elif game_menu_options == 2:
                instructions()
            elif game_menu_options == 3:
                break
        else:
            print('Please choose 1, 2 or 3 instead.\n')


def instructions():
    print("How to Play\n")
    print("\n")
    print("Not Battleships plays in the same way as a normal game of Battleships:\n")
    print("The players have a board with their ships hidden from the other player.\n")
    print("In this game the ships have been randomly placed for both player and the computer.\n")
    print("The player and the computer take turns picking out the X and then the Y axis for their salvo.\n")
    print("If the coordinates of the shot coincide with the location of a Ship, the Ship is destroyed.\n")
    print("The winner is the player who destroys the other fleet.\n")
    print("\n")
    print("Good Hunting!\n")
    print("\n")
    game_menu()


game_menu()

def get_player_name():
    """
    Function to get the player's name and return it to the game and validate the input
    """
    while True:
        player_one = input("Please enter your name: \n")
        if len(player_one) <1:                          # make sure user has actually put entered a name
            print(f"No, really, please enter your name... I want to know the name of the person I'm about to thrash...\n")
        elif len(player_one) <2:                        # Try to get the user's initials at least
            print(f"Go on, just your initials will do... Minimum 2 letters, please...\n")
        elif not player_one.isalpha():                      # ensure that the player has entered letters for their name
            print(f"Let's stick to letters for the time being, Mr Musk...\n")
        else:
            return player_one
 

def game_size_option():
    """
    Function to provide the user the choice of game board size and validate the input
    """
    print('What size of game board would you like?\n')
    print('Press 1 for 4 x 4\n')
    print('Press 2 for 5 x 5\n')
    print('Press 3 for 6 x 6\n')
    while True:
        game_size_option = input("1 / 2 / 3? ")             # ensure the user is only inputting a single digit
        if len(game_size_option) !=1 or not game_size_option.isdigit():
            print("We just need a single number between 1 and 3, please\n")
            continue                        
        game_size_option = int(game_size_option)
        if game_size_option >=1 and game_size_option <=3:    # ensure the player is inputting a number 1 - 3
            return game_size_option
        else:
            print('Please choose 1, 2 or 3 instead.\n')       # if input outside numerical options, loop to function start


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
    print('Press 1 for 4\n')
    print('Press 2 for 5\n')
    print('Press 3 for 6\n')
    while True:
        get_ship_option = input("1 / 2 / 3? \n")             # ensure the user is only inputting a single digit
        if len(get_ship_option) !=1 or not get_ship_option.isdigit():
            print("We just need a single number between 1 and 3, please\n")
            continue
        get_ship_option = int(get_ship_option)
        if get_ship_option >=1 and get_ship_option <=3:    # ensure the player is inputting a number 1 - 3
                return get_ship_option
        else:
            print('Please choose 1, 2 or 3 instead.\n')


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

def make_specific_boards():
    player_board = build_game_board(game_size)
    computer_board = build_game_board(game_size)
    return player_board, computer_board

player_board, computer_board = make_specific_boards()

def position_player_ships(ship_num, player_board):
    """
    Function to randomly place the player's ships on their board
    """
    player_ship_coords = set()                      # Make a set to store the coordinates of the player's positions
    ships_placed = 0                               # start counting how many ships have been placed on their board
    while ships_placed < ship_num:
        row = random.randint(0, len(player_board) - 1)
        column = random.randint(0, len(player_board[0]) - 1)
        player_coords = (row, column)               # get the coordinates of the Player's ships
        if player_coords not in player_ship_coords and player_board[row][column] == " - ":
            player_board[row][column] = " S "       # " S " marks the a Ship
            player_ship_coords.add(player_coords)   # Add the new ship coordinates to the set of ship coordinates
            ships_placed +=1
    return player_board

def position_computer_ships(ship_num, computer_board):
    """
    Function to randomly place the computer's ships on their board
    """
    computer_ship_coords = set()                        # Make a set to store the coordinates of the computer's positions
    ships_placed = 0                                   # start counting how many ships have been placed on the board
    while ships_placed < ship_num:
        row = random.randint(0, len(computer_board) - 1)
        column = random.randint(0, len(computer_board[0]) - 1)
        computer_coords = (row, column)                 # get the coordinates of the computer's ships
        if computer_coords not in computer_ship_coords and computer_board[row][column] == " - ":
            computer_board[row][column] = " S "         # " S " marks the a Ship
            computer_ship_coords.add(computer_coords)   # Add the new ship coordinates to the set of ship coordinates
            ships_placed +=1
    return computer_board
    

def display_current_boards(player_board, computer_board):
    """
    Function for displaying the boards
    """
    print(f"{player_one}'s Board \n")
    for row in player_board:
        print(" ".join(row))
    print("\n")
    print("Computer's Board \n")
    for row in computer_board:
        print(" ".join(row))
    print("\n")


player_board, computer_board = make_specific_boards()
player_board = position_player_ships(ship_num, player_board)
computer_board = position_computer_ships(ship_num, computer_board)
display_current_boards(player_board, computer_board)

def player_turn(player_board, computer_board):
    global previous_player_turn
    """
    Function for the player to take their turn
    """
    print(f"\nTake your shot, {player_one}!\n")
    print(f"Enter a number for each axis between 1 and {game_size}.\n")

    valid_shot = False

    while not valid_shot:
        input_x = int(input("\nEnter the X axis of your shot: \n"))                     # Get the user's x axis
        if (input_x <= 0 or input_x > game_size) or (input_x, 0) in previous_player_turn:    # validate the shot
            print("Wait... you're WAAAAY off the board... try again.\n")
        else:
            while True:
                input_y = int(input("\nEnter the Y axis of your shot: \n"))                     # Get the user's y axis
                if (input_y <= 0 or input_y > game_size) or (input_x, input_y) in previous_player_turn:    # validate the shot
                    print("Wait... Either you've tried that before OR you're WAAAAY off the board... try again.\n")
                else:
                    break
            valid_shot = True
    
    previous_player_turn.add((input_x, input_y))                # record the shot for later turns
    if computer_board[input_x][input_y] == " S ":              # check if Ship is at coordinates
        computer_board[input_x][input_y] = " H "               # mark location with " H " if a HIT
    else:
        computer_board[input_x][input_y] = " M "               # mark location with " M " if a MISS

previous_player_turn = set()    
player_turn(player_board, computer_board)

display_current_boards(player_board, computer_board)
