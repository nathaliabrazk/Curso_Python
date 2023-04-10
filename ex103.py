#FUNCTION PT 2
#Program who has a function calling token(), who recives two optional parameters: the name of a player and 
#how many gols him scored. The program need be able of show the token of of the player, even if some data
#has not been informed
def token(n = 'unknown', g = 0):
    print(f'{n} did {g} gols on championship')
#main
name = str(input('Player game: '))
gols = str(input(f'How many gols {name} did? '))
if gols.isnumeric():
    gols = int(gols)
else:
    g = 0
if name.strip() == '':
    token(g = gols)
else:
    token(name, gols)
