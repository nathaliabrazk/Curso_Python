#DICIONARY
#Improve the ex 93 to for what work with several users, including a system of vizualization of details
#of the use of each player
player = dict()
match = list()
op = ''
while True: 
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