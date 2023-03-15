#COMPOUND LIST
group = list()#definitive list
data = list()#temporary list
for c in range(0,2):
    data.append(str(input('Name:')))
    data.append(int(input('Age:')))
    group.append(data[:])#making a copy on original list 
    
print(group)