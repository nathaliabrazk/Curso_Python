#CONDITIONAL
#Program will read 3 numbers and show wich is the biggest and wich is the smallest
n1 = int(input('Type a first number:'))
n2 = int(input('Type a second number:'))
n3 = int(input('Type a third number:'))
#big
if n1 > n2 and n1 > n3:
    print('The biggest number:{}'.format(n1))
elif n2 > n1 and n2 > n3:
    print('The biggest number:{}'.format(n2))
elif n3 > n1 and n3 > n2:
    print('The biggest number:{}'.format(n3))
#small
if n1 < n2 and n1 < n3:
    print('The smalest number:{}'.format(n1))
elif n2 < n1 and n2 < n3:
    print('The smalest number:{}'.format(n2))
elif n3 < n1 and  n3 < n2:
    print('The smalest number:{}'.format(n3))