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
            continue
        try:                                                # ensure the player is inputting a number 1 - 3
            game_size_option = int(game_size_option)
            if 1<= game_size_option <=3:
                return game_size_option
            else:
                print('Please choose 1, 2 or 3 instead.')       # if input outside numerical options, loop to function start                   
        except ValueError:
            print("Let's stick to whole numbers, please...")    # if input isn't a number, raise error and restart function
            continue
    
def get_game_size(game_size_option):
    """
    Function to translate the user's choice in to the dimensions of the game board
    """
    if game_size_option == 1:                            # if player inputs 1 then the size = 4 x 4 game board etc.
        game_width = 4
        game_height = 4
        game_size = "4 x 4"
    elif game_size_option == 2:
        game_width = 5
        game_height = 5
        game_size = "5 x 5"
    elif game_size_option == 3:
        game_width = 6
        game_height = 6
        game_size = "6 x 6"
    
    return game_width, game_height, game_size

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
            continue
        try:                                                # ensure the player is inputting a number 1 - 3
            get_ship_option = int(get_ship_option)
            if 1<= get_ship_option <=3:
                return get_ship_option
            else:
                print('Please choose 1, 2 or 3 instead.')
                continue                   # if input outside numerical options, loop to function start
        except ValueError:
            print("Let's stick to whole numbers, please...")
            continue                       # if input isn't a number, raise error and restart function

def get_ship_num(get_ship_option):
    """
    Function to translate the user's choice in to the number of ships on the game board for the players
    """
    if get_ship_option == 1:                            # if player inputs 1 then the number of ships = 4 etc.
        num_of_ships = 4
        ship_num = "4"
    elif get_ship_option == 2:
        num_of_ships = 5
        ship_num = "5"
    elif get_ship_option == 3:
        num_of_ships = 6
        ship_num = "6"
    
    return num_of_ships, ship_num



player_one = get_player_name()
print(player_one)

game_size_option = game_size_option()
game_size = get_game_size(get_game_size)
print(game_size)

ship_num_option = ship_num_option()
num_of_ships = get_ship_num(ship_num_option)
ship_num = get_ship_num(ship_num_option)
print(ship_num)

# start_game = read_to_play()

print(f'Okay, {player_one}, you want a {game_size} with {ship_num} ships.')

"""
def read_to_play():
   
    Function to determine if the player is happy with game parameters
    
    ready_player_one = input(' Are you ready? Y / N: ').lower
    if ready_player_one == y:
        start_game()
    else:
"""

