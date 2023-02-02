#Program will read a number from 0 to 9999 and show on the screen each of separate digits
number = int(input('Type a number:'))
b = str(number)
print('unit:',b[3])
print('ten:',b[2])
print('hundred:',b[1])
print('thousand:',b[0])