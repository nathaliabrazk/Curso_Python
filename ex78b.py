#Program will read 5 numerical values and save on a list. On the end then show the bigger and the smallest value 
#and yours positions on the list
list = []
big = 0
small = 0
for c in range(0,5):
    list.append(int(input(f'Type the numerical value to position {c}:')))
    if c == 0:
        big = small = list[c]
    else:
        if list > big:
            big == list[c]
        if list < small:
            small == list[c]
print(f'The values of a list: {list}')