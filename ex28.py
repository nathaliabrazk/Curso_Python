#Program will make the computer "think" in a whole number between 0 and 5 and ask the user to 
#discover what the number was choiced by the computer
#The computer should write in the screen if the user won or lost
import random
number = random.randint(0,5)
print(number)
numberUser = int(input('Type a number between 0 and 5:'))
if number == numberUser:
    print('You won, congratulations!')
else:
    print('You lost!')