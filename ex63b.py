#Program who read a whole number and show on the screen the first elements of a sequence of Fibonacci
n = int(input(('Type the number of terms you want see:')))
F1 = 0
F2 = 1
count = 1
while count <= n:
    print('{} -> {} '.format(F1,F2), end='')
    total = F1 + F2
    F1 = F2
    F2 = total
print(' -> end')