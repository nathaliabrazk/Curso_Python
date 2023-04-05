#DICIONARY
#Improve the ex 93 to for what work with several users, including a system of vizualization of details
#of the use of each player
player = dict()
match = list()
details = list()
op = ''
while True: 
    player.clear()
    player['nome'] = str(input('Player name: '))
    tot = int(input(f'How much matches {player["nome"]} it played? '))
    match.clear()
    for c in range(0, tot):
        match.append(int(input(f'How much gols on match {c+1}: ')))
    player['gols'] = match[:]
    player['total'] = sum(match)
    details.append(player.copy())
    while True:
        op = str(input('Continue? ')).strip().upper()
        if op in 'YESNO':
            break
        print('Type just YES or NO!').strip().upper()
    if op == 'NO':
        break
#start of header
print('-=' * 30)
print('cod ', end='')
for i in player.keys():
    print(f'{i:<15}', end='') 
print()
#end of header

print('-' * 40)
for k, v in enumerate(details):
    print(f'{k:>4} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)