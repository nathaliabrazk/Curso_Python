#WHILE
n = 1
pair = 0
odd = 0
while n != 0:
    n = int(input('Type a number:'))
    print('If you want stop the program type 0.')
    if n != 0:
        if n % 2 == 0:
            pair += 1
        else:
            odd += 1
print('You typeD {} pair numbers and {} odd numbers'.format(pair,odd))