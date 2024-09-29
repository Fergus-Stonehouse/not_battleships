def get_player_name():
    """
    Function to get the player's name and return it to the game
    """
    player_one = input("Please enter your name: \n")
    if player_one.isalpha():                            # ensure that the player has entered letters for their name
        return player_one
    else:
        print("Let's stick to letters for the time being, Mr Musk...")
        return get_player_name()                        # If letters haven't been used, return to start of function

def game_size_option():
    """
    Function to provide the user the choice of game board size
    """
    print('What size of game board would you like?')
    print('Press 1 for 4 x 4')
    print('Press 2 for 5 x 5')
    print('Press 3 for 6 x 6')
    game_size_option = input("1 / 2 / 3? ")
    try:                                                # ensure the player is inputting a number 1 - 3
        game_size_option = int(game_size_option)
        if 1<= game_size_option <=3:
            return game_size_option
        else:
            print('Please choose 1, 2 or 3 instead.')
            return game_size_option()                   # if input outside numerical options, loop to function start
    except ValueError:
        print("Let's stick to whole numbers, please...")
        return game_size_option()                       # if input isn't a number, raise error and restart function
    
def get_game_size(game_size_option):
    if game_size_option = 1:
        game_size = 
    
    return game_size

def get_ship_num():
    """
    Function to provide the user the choice of how many ships will populate the game board
    """
    print('How many ships would you like?')
    print('Press 1 for 4')
    print('Press 2 for 5')
    print('Press 3 for 6')
    ship_num = input("1 / 2 / 3? ")
    return ship_num

def read_to_play():
    """
    Function to determine if the player is happy with game parameters
    """
    start_game = input('Y / N: ')
    return start_game

player_one = get_player_name()
game_size = get_game_size()
ship_num = get_ship_num()

print(f'Okay, {player_one}, you want a {game_size} with {ship_num} ships. Are you ready? {start_game}')
start_game = read_to_play()
