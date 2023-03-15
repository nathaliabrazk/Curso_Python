#COMPOUND LIST
group = list()#definitive list
data = list()#temporary list
for c in range(0,2):
    data.append(str(input('Name:')))
    data.append(int(input('Age:')))
    group.append(data[:])#making a copy on original list 
    data.clear()
print(group)
#looping with condition
for p in group:
    if p[1] >= 21:
        print(f'{p[0]} Is of legal age!')
    else:
        print(f'{p[0]} Is not of legal age')