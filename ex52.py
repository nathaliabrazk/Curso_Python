#FOR
#Program who read a whole number and say if he is or not a prime number
n = int(input('Type a number:'))
total = 0
for c in range(1, n + 1):
   if c % 1 == 0 and c % c == 0:
      print('\033[33m',end='')
      total += 1
   else:
      print('\033[31m',end='')
      print('{}'.format(c),end='')
print('The number {} was divisible {} times'.format(n,total))   
if total == 2:
   print('The number is prime!')
else:
   print('The number is not prime!')

