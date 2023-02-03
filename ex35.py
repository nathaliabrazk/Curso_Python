#Program will read a lenght of three straight lines and say to the user if they can or not form a triangle
sl1 = int(input('First straight line:'))
sl2 = int(input('Second lenght of a straight line:'))
sl3 = int(input('Third lenght of a straight line:'))
if sl1 + sl2 > sl3:
    print('Can form a triangle!')
elif sl1 + sl3 > sl2:
    print('Can form a triangle!')
elif sl2 + sl3 > sl1:
    print('Can form a triangle!')
