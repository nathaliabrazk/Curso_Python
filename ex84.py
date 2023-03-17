#Program who read the name and weight from a lot of people keeping the information on a list. At the end show
#A)How many people were registered. b)A list with the heavier people. c)A list with the more skinny people
temporary = []
principal = []
while True:
    temporary.append(str(input('name:')))
    temporary.append(float(input('weight:')))
    op = str(input('Continue?')).strip().upper()
    if op in 'NO':
        break