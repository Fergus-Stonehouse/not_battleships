# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
def get_player_name():
    """
    Function to get the player's name and return it to the game
    """
    player_one = input("Please enter your name: \n")
    return player_one

def get_game_size():
    """
    Function to provide the user the choice of game board size
    """
    print('What size of game board would you like?')
    print('Press 1 for 4 x 4')
    print('Press 2 for 5 x 5')
    print('Press 3 for 6 x 6')
    game_size = input("1 / 2 / 3? ")
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
    start_game = input('Y / N: ')
    return start_game

player_one = get_player_name()
game_size = get_game_size()
ship_num = get_ship_num()
start_game = read_to_play()

print(f'Okay, {player_one}, you want a {game_size} with {ship_num} ships. Are you ready? {start_game}')