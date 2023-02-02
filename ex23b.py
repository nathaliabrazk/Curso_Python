#Program will read a number from 0 to 9999 and show on the screen each of separate digits
number = int(input('Type a number:'))
u = number // 1 % 10
d = number // 10 % 10
h = number // 100 % 10
t = number // 1000 % 10
print('Unit:',u)
print('Ten:',d)
print('Hundred:',h)
print('Thousand:',t)
