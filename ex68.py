#Program will game pair or odd with the computer. The game just stop when the user lose, showing the total of 
#consecutives victories who him conquered in the end of game
from random import randint
total = 0
victory = 0
result = ''
op = ''
print('-' * 60) 
print('                     LETS PLAY PAIR OR ODD')
print('-' * 60)
n = int(input('Type a number:'))
computer = randint(0,11)
while True:
    op = str(input('You want pair or odd?')).strip().upper()
    n = int(input('Type a number:'))
    if n + computer % 2 == 0 and type == 'PAIR':
        result = 'WIN'
    elif n + computer % 2 == 1 and type == 'ODD':
        result = 'WIN'
        if result != 'WIN':
            print(f' You play: {n} computer play: {computer}\nResult = {result}\nUSER LOSE')
            break
print('end of game')
print(f'Victories: {victory}')

