import random


# WELCOME MESSAGE
print('\n🎮 WELCOME TO ROCK, PAPER & SCISSORS 🎮\n')

# ALLOW PLAYER TO PICK NUMBER OF ROUNDS OF GAME AND PICK A RANDOM PLAYER TO GO UP AGAINST THEM
no_of_games = int(input('How many rounds do you wish to play for?: '))
list_of_players = ['Mordock', 'Kakashi', 'Inaki', 'Andre', 'Jean', 'Josh', 'Lily', 'Jade', 'Abigail', 'Ankur']

# DISPLAY A MESSAGE ALONG WITH A COUNTDOWN SIGNIFYING SEARCH FOR A PARTNER
print('Searching for opponent...')
import countdown
countdown.countdown_time()
random_player = random.choice(list_of_players)
print(random_player, 'accepted your challenge.\n')


# COUNTDOWN TO MATCH
print('Match starting in...')
countdown.countdown_match()

game_choices = ['ROCK', 'PAPER', 'SCISSORS']
player_score = 0
random_player_score = 0

while no_of_games > 0:
    player_pick = input('Pick your move(R - ROCK, P - PAPER, S - SCISSORS): ' )
    if player_pick.lower() == 'r':
        print('You played: ROCK')
    elif player_pick.lower() == 'p':
        print('You played: PAPER')
    elif player_pick.lower() == 's':
        print('You played: SCISSORS')
    else:
        print('Wrong input. Try again!')
        break
    countdown.countdown_match()
    random_player_pick = random.choice(game_choices)
    print(random_player,'played: ', random_player_pick,'\n')
    
    if (random_player_pick == 'ROCK') and (player_pick.lower() == 'r'):
        print('DRAW!\n')
    elif (random_player_pick == 'ROCK') and (player_pick.lower() == 'p'):
        print('PAPER beats ROCK!\n')
    elif (random_player_pick == 'ROCK') and (player_pick.lower() == 's'):
        print('ROCK beats SCISSORS!\n')
    elif (random_player_pick == 'PAPER') and (player_pick.lower() == 'r'):
        print('PAPER beats ROCK!\n')
    elif (random_player_pick == 'PAPER') and (player_pick.lower() == 'p'):
        print('DRAW!\n')
    elif (random_player_pick == 'PAPER') and (player_pick.lower() == 's'):
        print('SCISSORS beats PAPER!\n')
    elif (random_player_pick == 'SCISSORS') and (player_pick.lower() == 'r'):
        print('ROCK beats SCISSORS!\n')
    elif (random_player_pick == 'SCISSORS') and (player_pick.lower() == 'p'):
        print('SCISSORS beats PAPER!\n')
    elif (random_player_pick == 'SCISSORS') and (player_pick.lower() == 's'):
        print('DRAW!\n')
    
    no_of_games -= 1
