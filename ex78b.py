#Program will read 5 numerical values and save on a list. On the end then show the bigger and the smallest value 
#and yours positions on the list
listvalues = []
big = small = 0
#repeat loop to fill the list 
for c in range(0,5):
    listvalues.append(int(input('Type a value:')))
    if c == 0:
        big = small = listvalues[0]
    else:
        if listvalues[c] > big:
            big = listvalues[c]
        if listvalues[c] < small:
            small = listvalues[c]
print(f'You type the values: {listvalues}')
print(f'The SMALLEST values: on positions:',end='')
#repeat loop to find the positions from the smallest values
for i, v in enumerate(listvalues):
    if v == small:
        print(f'{i}...', end='')

print(f'The HIGGESTS values: {big} on positions:',end='')
#repeat loop to find the positions from the higgests values
for i, v in enumerate(listvalues):
    if v == big:
        print(f'{i}...', end='')
