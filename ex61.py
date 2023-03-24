#WHILE
#remake the ex 51 who read the first term and the reason of a P.A. In the end show the 10 first terms 
#of this progression using while
first = int(input('Type the first term:'))
reason = int(input('Type the reason:'))
term = first
count = 1
while count <= 10:
    print('{} -> '.format(term), end='')
    term += reason
    count += 1
print('end')