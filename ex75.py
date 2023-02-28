#Program wll read 4 numbers and save them in a tuple. At the end show: a)How many times the number 9 appears. 
#b)In wich position was entered the number 3. c)What were the even numbers
tuple = 0
nine = 0
three = 0
for c in range(4):
    n  = int(input('Type a number: '))
if n == 9:
    nine += 1
print(f'The number 3 appears on position = {c.index(3) + 1}')
print(f'The number 9 appears = {nine} times')
for even in n:
    if n % 2 == 0:
        print('n', end='')
