#Program who read a number and show your factorial 
n = int(input('Type the number to show your factorial:'))
c = n
print('Calculing {}! = '.format(c), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    c -= 1
