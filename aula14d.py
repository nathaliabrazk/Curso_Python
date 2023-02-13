#WHILE
n = 1
pair = 0
odd = 0
while n != 0:
    n = int(input('Type a number:'))
    if n % 2 == 0:
        pair += 1
    else:
        odd += 1
print('You type {} pair numbers and {} odd numbers'.format(pair,odd))