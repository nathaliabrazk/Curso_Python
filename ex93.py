#DICIONARY
#Program that manage a use of a football player. The program will read the soccer player name and 
#how much matches him played. After will read the quantidy of goals made in each matches. After
#all this will be saved on a dicionary, including the total of goals madet during a champeonship
player = dict()
match = list()
player['nome'] = str(input('Player name: '))
tot = int(input(f'How much matches {player["nome"]} it played? '))
for c in range(0, tot):
    match.append(int(input(f'How much gols on match {c+1}: ')))
player['gols'] = match[:]
player['total'] = sum(match)
print('-=' * 30)
print(f'The player {player["nome"]} played {len(player["gols"])} matches')
for i,v in enumerate(player['gols']):
    print(f'  => On match {i+1}, did {v} gols')
print(f'Total of {player["total"]} gols')