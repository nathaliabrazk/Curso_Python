#COMPOUND LIST
#Program will help a player from MEGASENA to create guesses. The program will ask how many games will be generated
#and will draw 6 numbers between 1 and 60 for each game, registering all in a compound list
from random import randint 
lista = list()
games = list()
print('-' * 30)
print('           MEGA SENA          ')
print('-' * 30)
quant = int(input('Type how many games will be generate: '))
tot = 1#need be initialized with 1 or the program will generate 1 more game
while tot <= quant:
    count = 0#variable to regist the quantidy of numbers on the list
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            count += 1 
            if count >= 6:
                break
    lista.sort()#method to organize the numbers 
    games.append(lista[:])#copy of the list 
    lista.clear()
    tot += 1
print('-=' * 3, f'PRIZE DRAW {quant} GAMES', '-=' * 3) 
for i, l in enumerate(games):
    print(f'Game {i}: {l}')