#Program wll read 4 numbers and save them in a tuple. At the end show: a)How many times the number 9 appears. 
#b)In wich position was entered the number 3. c)What were the even numbers
values = tuple(int(input('Type a number: '))for c in range(1, 5))
print(f'The number 9 apears {values.count(9)} times')
print(f'The value 3 was typed for the first on {values.index(3)+1}º position' if 3 in values else 'The value 3 was not typed')
print('The even values entered', end=' ')
print({n for n in values if n % 2 == 0}, end=' ')