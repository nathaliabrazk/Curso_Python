#Program who read numbers. In the end show the average between all the values and show the bigger and 
#the smaller number. The program need ask if the user want continue or not
n = 0
op = 0
bigger = 0
smaller = 0
add = 0
average = 0 
count = 0

op = ''
while op != 'NO':
    n = int(input('Type a number:'))
    add += n
    count += 1
    op = str(input('Continue?\nYes or no:')).strip().upper()
  
    if count == 1:
        smaller = bigger = n
    else:
        if n > bigger:
            bigger = n
        if n < smaller:
            smaller = n
average = add / count
print('end')
print('You type {} numbers'.format(count))
print('Average of all the numbers: {}'.format(average))
print('The bigger number: {}\nThe smaller number: {}'.format(bigger,smaller))

