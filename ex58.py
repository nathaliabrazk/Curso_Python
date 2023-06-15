#WHILE
#Improve the ex 28 where the computer gonna "think" in a number between 1 and 10. But now the user go try guess
#until hit, showing in the end how many guesses were needed to get yhe right answer
import random
from time import sleep
t = 1
computer = random.randint(0,10)
print('HELLO, Im your computer!\nIm thinking in a number between 1 and 10')
sleep(1)
user = int(input('Try guess the number i thought:'))
sleep(1.5)
while user != computer:
    user = int(input('WRONG!\nTry again:'))
    sleep(1.5)
    t += 1
print('YOU WIN!\nThe number of tryes you need to win:{}'.format(t))