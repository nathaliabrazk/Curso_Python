#DICIONARY
#Program where 4 users throuw dice and have random results. Store this data on a dicionary. After place
#this dicionary in order, knowing that the winner is the one with the highest number on the dice
from random import randint# library to random numbers
from time import sleep
game = {'Player 1': randint(0,10),
        'Player 2': randint(0,10),
        'Player 3': randint(0,10),
        'Player 4': randint(0,10)}
print('========- Rafled values -=========')
for k, v in game.items():
    print(f'{k} play: {v}')
    sleep(0.5)
ranking = sorted(game.items(), key=lambda item: item[1], reverse=True)#putting the dicionary in order
print('==========- RANKING -=========')
for i,v in enumerate(ranking):
    print(f'{i+1}º Position = {v[0]} with = {v[1]}')
    sleep(0.5)
