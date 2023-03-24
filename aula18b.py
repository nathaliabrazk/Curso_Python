#COMPOUND LIST
test = list()
test.append('Maria')
test.append(32)
group = list()
group.append(test[:])
test[0] = 'Joao'
test[1] = 90
group.append(test[:])
print(group)