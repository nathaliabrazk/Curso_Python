#Program who read some whole numbers. The program will stop when the user types 999. In the end show how many 
#numbers were typed and their sum
count = 0
add = 0
while True:
    n = int(input('Type a number:'))
    if n == 999:
        break
    count += 1
    add += n

print(f'Quanty of typed numbers: {count}\nSum of the numbers: {add}')