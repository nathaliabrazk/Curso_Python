#Program will game pair or odd with the computer. The game just stop when the user lose, showing the total of 
#consecutives victories who him conquered in the end of game
import random 
total = 0
victory = 0
result = ''
print('=*=' * 20) 
print('                     LETS PLAY PAIR OR ODD')
print('=*=' * 20) 
while True:
    user = int(input('Type a number:'))
    op = str(input('You want pair or odd?')).strip().upper()
    computer = random.randint(0,10)
    while result != 'WIN':
        result = user + computer
        print(f'You play {user} and the computer played: {computer}, result = {result}',end='')
        print(f' {op}')
    if op == 'PAIR' and result % 2 == 0:
        result = 'WIN'
        victory += 1
        print('USER WIN')
    else:
        print('THE COMPUTER WIN!\nYOU LOSE!')
        break
    if op == 'ODD' and result % 2 == 1:
        result = 'WIN'
        victory += 1
        print('USER WIN')
    else:
        print('THE COMPUTER WIN!\nYOU LOSE!')
        break
print(f'Total of your consecutive victories:{victory}')
