#DICIONARY
people = {'name': 'Nathalia', 'sex': 'f', 'age': '50'}
#        |       tuple      | |  tuple |  |   tuple  |
print(f'{people["name"]} has {people["age"]} years old')
print('=-' * 30)
print(people.items())
#usin loop
print('=-' * 30)
for k in people.keys():
    print(k)#just gonna show the "bottom" part
print('=-' * 30)
for k in people.values():
    print(k)
