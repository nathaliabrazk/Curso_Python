#Program will game even or odd with the computer. The game just stop when the user lose, showing the total of 
#consecutives victories who him conquered in the end of game
import random 
total = 0
win = 0
lose = 0
result = 0
print('=*=' * 20) 
print('                     LETS PLAY EVEN OR ODD')
print('=*=' * 20) 
while result != 'WINN':
    move = int(input('Type a number:'))
    op = str(input('You want even or odd?')).strip().upper()
    computer = random.randint(0,10)
    print(f'The computer played: {computer}')
    result = move + computer
    print(f'The result are: {result}')
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
