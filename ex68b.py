#BREAK
from random import randint 
v = 0
while True:
    user = int(input('Type a number:'))
    computer = randint(0,11)
    result = user + computer
    type = ' '
    while type not in 'OP':
        type = str(input('Odd or pair (O\P)? ')).strip().upper()[0]
    print(f'You play {user} and the computer play {computer}. Total = {result}', end='')
    print(' PAIR!' if result % 2 == 0 else ' ODD!')
    if type == 'P':
        if result % 2 == 0:
            print('YOU WON!\nComputer lose...')
            v += 1
        else:
            print('YOU LOSE!\nComputer win...')
            break
    elif type == 'O':
        if result % 2 == 1:
            print('YOU WON!\nComputer lose...')
        else:
            print('YOU LOSE!\nComputer win...')
            break
    print('Lets play again :)')
print(f'GAME OVER :(\nYou won {v} times!')