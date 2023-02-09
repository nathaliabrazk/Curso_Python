#Program who read 6 whole numbers and show the sum just of even numbers. If the typed value is odd 
#disregard the 
count = 0
sum = 0
for c in range (1,6):
    n = int(input(('Type a number:')))
    if n % 2 == 1:
        print('value odd')
    elif n % 2 == 0:
        count + 1
        sum = sum + n
print('The sum of all the even numbers are:{}'.format(sum))
print('end')