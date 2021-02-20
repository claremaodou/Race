# Race Program
# Implementing a simple 2 player racing game. 
# Roll a 6-sided die and move the player based on the value of the die. 
# In order to win the game a player must move their game piece exactly onto
# the last position without overshooting the last position. 

import random

def rolling_dice(player):
    # rolls the dice and sets the amount to move
    # -player is playerx or playero
    input('Player '+ player+' press enter to roll!')
    move = random.randint(1,6) 
    print('Player', player, 'rolled a', move)
    return move

def set_start(start, position_x, position_o):
    # sets the starting position of the players
    # - start is starting position
    # - position_x is the position of player x
    # - position_y is the position of player y
    print('Players start at starting position')
    position_x[start] = 'x'
    position_o[start] = 'o'
    print('*'*36)   
    print('Player x:',*position_x, sep=' ')
    print('Player o:', *position_o, sep=' ')
    print('*'*36)

def update_position(start, spaces, position_player, player): 
    # updates the position of the players
    # - start is starting position
    # - spaces is the new position
    # - position_player is the position of player x or o
    # - player is x or o
    position_player[start] = '-'
    position_player[spaces] = player
    return position_player

def display(position_player, position_player2):
    # displays the player's positions
    # - position_player is the position of player x 
    # - position_player2 is the position of player o
    print('*'*36)
    print('Player x:',*position_player, sep=' ')  
    print('Player o:', *position_player2, sep=' ')
    print('*'*36)   
    
def update_spaces(start, move):
    # updates the spaces the player moves
    # - start is starting position
    # - move is the amount of spaces to move
    spaces = start + move 
    return spaces

def check_overshot(spaces, player):
    # checks if the player went over the spaces
    # - start is starting position
    # - player is x or o
    if spaces > 12:
        print('The roll was too high, player',player, 
            'has been sent to the start')
        spaces = 0 
    return spaces
        
def check_correct(spaces, player):
    # check of the player has won
    # - start is starting position
    # - player is x or o    
    if spaces == 12:
        print('Player', player, 'has won!')  
        exit()
        
def starting_position(start, move, spaces):
    # re-sets the starting position after each roll
    # - start is starting position
    # - move is the amount of spaces to move
    # - player is x or o     
    start = start + move      
    if spaces == 0:
        start = 0
    return start

def main():
    # main program code
    # initialize variables
    start_x = 0
    start_o = 0
    spaces_x = 0
    spaces_o = 0
    counter = 0
    position_x = ['-']*13  
    position_o = ['-']*13    
    set_start(0, position_x, position_o)
    while True:
        
        counter += 1   
        if counter % 2 != 0:
            # player x's turn to move
            move = rolling_dice('x')  
            spaces_x = update_spaces(start_x, move)
            spaces_x = check_overshot(spaces_x, 'x')
            postion_player_x = update_position(start_x, spaces_x, position_x, 'x')
            display(position_x, position_o)
            start_x = starting_position(start_x, move, spaces_x)
            check_correct(spaces_x, 'x')
        else:
            # player o's turn to move
            move = rolling_dice('o')  
            spaces_o = update_spaces(start_o, move)
            spaces_o = check_overshot(spaces_o, 'o')
            postion_player_o = update_position(start_o, spaces_o, position_o, 'o')
            display(position_x, position_o)
            start_o = starting_position(start_o, move, spaces_o)    
            check_correct(spaces_o, 'o')
main()
