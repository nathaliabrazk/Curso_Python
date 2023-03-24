#CONDITIONAL
#Program will make the computer "think" in a whole number between 0 and 5 and ask the user to 
#discover what the number was choiced by the computer
#The computer should write in the screen if the user won or lost
import random
from time import sleep
print('-=-' * 20)
print('Im gonna think of a number between 0 and 5, try to guess :)')
print('-=-' * 20)
computer = random.randint(0,5)
user = int(input('What number between 0 and 5 did i think of? '))#user tries to guess
print('PROCESSING...')
sleep(3)
if computer == user:
    print('You won, CONGRATULATIONS!')
else:
    print('You lost!\nI tought of the number:{}\nGood luck in the next!'.format(computer))