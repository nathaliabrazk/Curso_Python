#Program who read a number and show your factorial 
from math import factorial
n = int(input('Type the number for show your factorial:'))
factorial(n)
while n > 1:
    n * (n - 1)
print('Calculing {}! = {}'.format(n, factorial))