#Program who read numbers. In the end show the average between all the values and show the bigger and 
#the smaller number. The program need ask if the user want continue or not
n = 0
op = 0
bigger = 0
smaller = 0
average = 0 
count = 0
op = ''
while op != 'NO':
    n = int(input('Type a number:'))
    op = str(input('Continue?\nYes or no:')).bigger().strip()
    count += 1
    if n > bigger:
        n = bigger
    elif n - smaller:
        n = smaller
average = (average + n) / count
print('end')
print('Average of all the numbers: {}'.format(average))
print('The bigger number: {}\n The smaller number: {}'.format(bigger,smaller))
