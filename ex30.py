#CONDITIONAL
#Program will read a number and say if he is ODD or EVEN 
n = int(input('Type a number:'))
if n % 2 == 0:
    print('The number: {} is ODD!'.format(n))
else:
    print('The number: {} is EVEN'.format(n))