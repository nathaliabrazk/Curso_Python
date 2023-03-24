#Program will read a number from 0 to 9999 and show on the screen each of separate digits
number = int(input('Type a number:'))
b = str(number)
print('Unit:',b[3])
print('Ten:',b[2])
print('Hundred:',b[1])
print('Thousand:',b[0])