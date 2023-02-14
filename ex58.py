#Improve the ex 28 where the computer go "think" in a number between 1 and 10. But now the user go try guess
#until hit, showing in the end how many guesses were needed to get yhe right answer
import random
from time import sleep
computer = random.randint(1,10)
print('Im thinking in a number between 1 and 10')
sleep(1)