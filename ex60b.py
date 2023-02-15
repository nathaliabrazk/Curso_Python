#Program who read a number and show your factorial 
n = int(input('Type the number to show your factorial:'))
c = n
f = 1
print('Calculing {}! = '.format(c), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))
