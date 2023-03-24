#FOR
#Program who read the first term and the reason of a P.A. In the end show the 10 first terms 
#of this progression
term = int(input('Type the first term:'))
reason = int(input('Type the reason:'))
tenth = term + (10 - 1) * reason
for c in range(term,tenth + reason,reason):
    print(' {} '.format(c), end=' -> ')
print('end')