#Program will read two whole numbers and compare the two, showing in the screen a message:
#-The first value is bigger, -The second value is bigger, -Don't exist bigger value, the two are the same
from time import sleep
n1 = int(input('Type a first number:'))
n2 = int(input('Type a second number:'))
if n1 != int or n2 != int:
    print('Type just whole numbers!')
print('Comparing...')
sleep(2)
if n1 > n2:
    print('The first value is bigger!')
elif n2 > n1:
    print('The second value is bigger!')
elif n1 == n2:
    print('Dont exist bigger value, the two are the same!')
