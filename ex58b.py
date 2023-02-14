#Improve the ex 28 where the computer go "think" in a number between 1 and 10. But now the user go try guess
#until hit, showing in the end how many guesses were needed to get yhe right answer
from random import randint
computer = randint(0,10)
print('HELLO, Im your computer!\nIm thinking in a number between 1 and 10')
hit = False
t = 1
while not hit:
    user = int(input('Try guess the number i thought:'))
    t += 1
    if user == computer:
        hit = True
    else:
        if user < computer:
            print('More...Try again.')
        elif user > computer:
            print('Less...Try again.')
print('YOU WIN!\nNumber of try you needed to win:{}'.format(t))
