#Program who read a whole number and show on the screen the first elements of a sequence of Fibonacci
n = int(input('Type how many terms do you want see:'))
t1 = 0
t2 = 1
print('{} -> {}'.format(t1,t2), end='')
count = 3
while count <= n:
    t3 = t1 + t2
    print(' -> {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    count += 1
print(' -> end')