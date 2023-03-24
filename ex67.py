#BREAK
#Program who show the multiplication table of some numbers, one at a time, for each value typed for the user 
#The program will stop when the typed number is negative
while True:
    n = int(input(('Type a number to see your multiplication table(for stop the program type a negative number):')))
    if n < 0:
        break
    for l in range (1,11):
        print(f'{n} x {l} = {n*l}')
print('end')        