#FUNCTION
#Program who have a list calling numbers and two functions calling prizeDraw() and sumPair(). The first function
#gonna raffle 5 numbers and insert them inside the list and the second function gonna show the sum of all the pair
#values sorted for the last function
from random import randint
from time import sleep

#first function
def raffle(lista):
    print('Raffling 5 numbers from the list: ', end='')
    for count in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} ', end='', flush=True)
        sleep(0.3)
    print('Finish')

#second function 
def sumPair(lista):
    sum = 0
    for value in lista:
        if value % 2 == 0:
            sum += value
    print(f'Adding pair numbers from {lista}, we have {sum}')

numbers = list()
raffle(numbers)
sumPair(numbers)