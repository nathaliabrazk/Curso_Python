#DICIONARY
#Program that manage a use of a football player. The program will read the soccer player name and 
#how much matches him played. After will read the quantidy of goals made in each matches. After
#all this will be saved on a dicionary, including the total of goals madet during a champeonship
player = dict()
matches = list()
player['name'] = str(input('Name:'))
totalMatches = int(input(f'How many matches the player {player["name"]} it played?'))
for c in range(1, totalMatches):
    player['gols'] = int(input(f'How many gols the player {player["name"]} did on matche ({c}):'))
    player['count'] = sum(matches)
print('=-' * 30)
print(f'Ther player {player["name"]} play {len(player["gols"])} matches')
for i, v in enumerate(player['gols']):
    print(f'=> On match {i} did {v} gols')
