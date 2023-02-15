#remake the ex 51 who read the first term and the reason of a P.A. In the end show the 10 first terms 
#of this progression using while
term = int(input('Type the first term:'))
reason = int(input('Type the reason:'))
tenth = 0
while term < reason:
    tenth = term * reason
print('{} -> {} -> end',end= ''.format(term,tenth))
