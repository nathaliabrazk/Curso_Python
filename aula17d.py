#LIST
values = list()
for count in range (0,5):
    values.append(int(input('Type the value:')))
for c, v in enumerate (values):
    print(f'On position {c} i find the value {v}!') 
print('End of the list')