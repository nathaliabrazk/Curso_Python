#Remake the ex 09, showing in the screen the multiplication table of a number who the user choice 
#using a loop forn 
count = 0
n = int(input('Type a number:'))
for n in range(1,101):
    sum = count + 1
    print('{} x {}'.format(n, sum))