#WHILE
#Improve the ex 28 where the computer gonna "think" in a number between 1 and 10. But now the user will try to guess
#until hit, showing in the end how many guesses were needed to get the right answer
from random import randint
from time import sleep
computer = randint(0,10)
print('HELLO, Im your computer!\nIm thinking in a number between 1 and 10')
hit = False
t = 1 #variable to count the try
while not hit:
    user = int(input('Try guess the number i thought:'))
    t += 1
    if user == computer:
        hit = True
    else:
        if user < computer:
            sleep(0.5)
            print('More...Try again.')
        elif user > computer:
            sleep(0.5)
            print('Less...Try again.')
sleep(0.8)
print('YOU WIN!\nNumber of tries you needed to win:{}'.format(t))
