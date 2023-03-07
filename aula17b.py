num = [2, 5, 9, 1]
num [2] = 3
#num [4] = 7 Its not possible add elements that way, its nescessary use the append method
num.append(7) 
num.sort()#This method gonna organize the elements in growing order
num.insert(2, 0)#This method gonna add elements between any position
if 4 in num:
    num.remove(4)
else:
    print('The number 4 dont exist on list!')
num.pop(2)#This method will delete a position 
num.remove(2)#This method will delete the first occurrence but dont search in all the occurrences on list
print(num)
print(f'The list has {len(num)} elements')
