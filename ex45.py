#Program that plays jokenpô with you
from random import randint
itens = ('Stone', 'Paper', 'Scissors')
computer = randint(0, 2)
print('-*-' * 20) 
print('                        JOKENPÔ MENU')
print('-*-' * 20)
print('Stone - [0]')
print('Paper - [1]')
print('Scissors - [2]')
user = int(input('Type your move: '))
print('Computer it played: {}'.format(itens[computer]))
print('User it played: {}'.format(itens[user]))

if computer == 0: #Computer it played Stone
    if user == 0:
        print('TIE IN THE GAME!')
    elif user == 1:
        print('USER WIN!')
    elif user == 2:
        print('COMPUTER WIN!')
    else:
        print('INVALID MOVE!')

elif computer == 1: #Computer it played paper
    if user == 0:
        print('COMPUTER WIN!')
    elif user == 1:
        print('TIE IN THE GAME!')
    elif user == 2:
        print('USER WIN!')
    else:   
        print('INVALID MOVE!')

elif  computer == 2: #Computer it played scissors
    if user == 0:
        print('USER WIN!')
    elif user == 1:
        print('COMPUTER WIN!')
    elif user == 2:
        print('TIE IN THE GAME!')
    else:
        print('INVALID MOVE!')