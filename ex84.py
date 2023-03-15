#Program who read the name and weight from a lot of people keeping the information on a list. At the end show
#A)How many people were registered. b)A list with the heavier people. c)A list with the more skinny people
date = list()
moreweight = list()
moreskinny = list()
small = big = 0
op = ''
total = 0
while True:
    date.append(str(input('Name:')))
    date.append(float(input('Weight:')))
    total += 1
    if date[1] > big:
        moreweight.append(date[0][1])
    elif date[1] < small:
        moreskinny.append(date[1]) 
    op = str(input('Continue?')).strip().upper()
    if op == 'NO':
        break
print(f'Total of people registered: {total}')
print(f'The havier people: {moreweight}')
print(f'The more skinny people: {moreskinny}')