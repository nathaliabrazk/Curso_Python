#COMPOUND LIST
#Program that create a matriz 3x3 with typed values. At the end show on the screen the matriz
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range (0, 3):
    for c in range (0, 3):
        matriz[l][c] = int(input(f'Type a value to [{l}, {c}]:'))
print('====== MATRIZ ======')
for l in range (0,3):
    for c in range(0,3):
        print(f'|{matriz[l][c]:5^}|',end='')
    print()