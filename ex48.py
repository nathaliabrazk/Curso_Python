#FOR
#Program who calculate the sum of all the odd numbers who are multiples of three
#and wich are found in the range from 1 to 500
sum = 0
count = 0
for n in range(1, 501, 2):
    if n % 3 == 0:
        count = count + 1
        sum = sum + n
print('The sum of all the odd numbers are:{}'.format(sum))