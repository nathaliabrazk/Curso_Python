#Program will game pair or odd with the computer. The game just stop when the user lose, showing the total of 
#consecutives victories who him conquered in the end of game
import random 
total = 0
win = 0
lose = 0
result = 0
print('=*=' * 20) 
print('                     LETS PLAY PAIR OR ODD')
print('=*=' * 20) 
while result != 'WIN':
    move = int(input('Type a number:'))
    op = str(input('You want pair or odd?')).strip().upper()
    if op != 'PAIR' or op != 'ODD':
        print('Invalid!\n(type just even or odd)')
    computer = random.randint(0,10)
    print(f'The computer played: {computer}')
    result = move + computer
    print(f'The result are: {result}')
    print(f'{op}')
    if op == 'PAIR' and result % 2 == 0:
        result = 'WIN'
        win += 1
        print('USER WIN')
    else:
        print('THE COMPUTER WIN!\nYOU LOSE!')
        break
    if op == 'ODD' and result % 2 == 1:
        result = 'WIN'
        win += 1
        print('USER WIN')
    else:
        print('THE COMPUTER WIN!\nYOU LOSE!')
        break
print(f'Total of your consecutive victories:{win}')
