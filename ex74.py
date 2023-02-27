#Program will to generate 5 random numbers and and put in a tuple. Then show the list of generate numbers and 
#indicate the biggets and the smallest value
from random import randint
numbers = (randint(1,10), randint(1,10), 
     randint(1,10), randint(1,10))
print('The random numbers: ', end='')
for n in numbers:
    print(f'{n}', end='')
print(f'\nThe smallest value = {min(numbers)}\nThe biggest value = {max(numbers)}')