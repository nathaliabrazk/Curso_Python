#Program who read a whole number and say if he is or not a prime number
n = int(input('Type a number:'))
total = 0
for c in range(1, n + 1):
 if c % 1 == 0 and c % c == 0:
    total += 1
 else:
    print('{} is not a prime number'.format(n))
print('The number {} was divisible {} times'.format(n,total))