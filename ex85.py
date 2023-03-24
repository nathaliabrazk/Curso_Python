#COMPOUND LIST
#Program in wich the user can type 7 number values and regist them in a single list and separete the pair numbers 
#and the odd numbers. At the end show yhe pair and the odd numbers in ascending order
#     0    1
n = [ [], [] ]
value = 0
for c in range(1,8):
    value = int(input(f'Type the {c}º value: '))
    if value % 2 == 0:
        n[0].append(value)
    else:
        n[1].append(value)
print('+=' * 30)
print(f'Pair values: {n[0]}\nOdd values:{n[1]}')
  