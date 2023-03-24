#FOR
#Remake the ex 09, showing in the screen the multiplication table of a number who the user choice 
#using a loop forn 
count = 0
n = int(input('Type a number to see your multiplication table:'))
for c in range(1,11):
    print('{} x {:2} = {}'.format(n, c, n*c))