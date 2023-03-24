#LIST
#Program will read 5 numerical values and save on a list. On the end then show the bigger and the smallest value 
#and yours positions on the list
n = list()
for c in range(0,5):
    n.append(int(input(f'Type a numerical value to position[{c}]:')))
print(f'The list values: {n}')
print(f'The biggest value = {max(n)} On position {c}\nThe smallest value = {min(n)} On position {c}')