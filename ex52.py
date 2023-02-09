#Program who read a whole number and say if he is or not a prime number
n = int(input('Type a number:'))
if n % 1 == 0 and n % n == 0:
    print('{} is a PRIME NUMBER!'.format(n))
else:
    print('{} is not a prime number'.format(n))