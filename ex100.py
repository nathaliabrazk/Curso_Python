#FUNCTION
#Program who have a list calling numbers and two functions calling prizeDraw() and sumPair(). The first function
#gonna raffle 5 numbers and insert them inside the list and the second function gonna show the sum of all the pair
#values sorted for the last function
from random import randint
from time import sleep
#first function
def prizeDraw(list):
    print('Raffling numbers')
    for count in range(0, 5):
        n = randint(1, 10)
        list.append(randint(1, 10))
        print(f'{n} ', end='', flush=True)
        sleep(0.3)
    print('Finish')
#second function 
def sumPair():
    numbers = list()
    prizeDraw(numbers)
    print(numbers)