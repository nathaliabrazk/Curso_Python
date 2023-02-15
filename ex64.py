#Program who read many numbers, the program will stop when the user type 999. In the end show how many numbers
#were typed and how is the sum between them
n = 0
count = 0
add = 0
n = int(input('Type a number[999 to stop the program]:'))
while n != 999:
    count += 1 
    add += n
    n = int(input('Type a number[999 to stop the program]:'))
if n == 999:
        count - 1   
print('end')
print('Quanty of typed numbers: {}'.format(count))
print('Add of all the numbers: {}'.format(add))
