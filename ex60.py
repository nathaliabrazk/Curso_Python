#Program who read a number and show your factorial 
from math import factorial
n = int(input('Type the number for show your factorial:'))
f = factorial(n)
print('Calculing {}! = {}'.format(n, f))