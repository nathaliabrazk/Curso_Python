#Program that plays jokenpô with you
from random import randint
itens = ('Stone', 'Paper', 'Scissors')
computer = randint(0, 2)
print('-*-' * 20) 
print('                        JOKENPÔ MENU')
print('-*-' * 20)
print('Stone - [1]')
print('Paper - [2]')
print('Scissors - [3]')
player = int(input('Type your move:'))
print('Computer move:{}'.format(itens[computer]))
print('Player move:{}'.format(itens[computer]))