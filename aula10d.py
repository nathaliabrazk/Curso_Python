#Avarage with conditional
n1 = float(input('Type the first note:'))
n2 = float(input('Type the second note:'))
a = (n1 + n2) / 2
if a >= 6:
    print('Avarage:{:.1f} \nIts a good avarage, congratulations!'.format(a))
else:
    print('Avarage:{:.1f} \nIts not a good avarege, good luck in the next!'.format(a))