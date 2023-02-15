#Improve the ex 61, asking for the user if him want show more terms. The program end when the user say he 
#wants show 0 terms
first = int(input('Type the first term:'))
reason = int(input('Type the reason:'))
term = first
count = 1
total = 0
more = 10
while more != 0:
    total = total + more
    while count <= total:
        print('{} -> '.format(term), end='')
        term += reason
        count += 1
    print('pause')
    more = int(input('How many terms do you want see: '))
print('end')
print('Finished with {} terms shown'.format(total))