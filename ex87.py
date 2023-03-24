#COMPOUND LIST
#Improve the last ex showing on the end: a)The sum of all even values typed. b)The sum of the values of the 
#third column. c)The bigger value of the second line 
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
sumeven = sumthird = bigger = 0
#loop to fill in the matriz
for l in range (0, 3):#line
    for c in range (0, 3):#column
        matriz[l][c] = int(input(f'Type a value to [{l}, {c}]:'))
print('====== MATRIZ ======')
for l in range (0,3):#line
    for c in range(0,3):#column
        print(f'|{matriz[l][c]:5^}|',end='')
        if matriz[l][c] % 2 == 0:
            sumeven += matriz[l][c]
    print()
print('+=' * 30)
print(f'The sum of even values: {sumeven}')
#loop to find the values of the third column
for l in range(0, 3 ):
    sumthird += matriz[l][2]
print(f'The sum of values of the third column: {sumthird}')
for c in range(0, 3):
    if c == 0:#means it is in the first column
        bigger == matriz[l][c]
    elif matriz[l][c] > bigger:
        bigger = matriz[l][c]
print(f'The bigger value of the second line: {bigger}')