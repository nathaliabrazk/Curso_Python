#BREAK
#Program who read the name and price of a lot products. The program will ask for the user if him want continue. In the 
#end show: What is the total expense. How many products cust more than R$1000.
#What is the product name more cheap.
total = 0
thousand = 0
smaller = 0
count = 0
while True:
    product = str(input('Type the product name: '))
    price = float(input('Type the product price R$: '))
    count += 1
    total += 1
    if price > 1000:
        thousand += 1
    if count == 1 or price < smaller:
        smaller == price
        cheap = price
    op = ''
    while op not in 'YN':
        op = str(input('Continue? ')).strip().upper()[0]
    if op == 'NO':
        break
print('{:->40}'.format('END OF THE PROGRAM'))
print(f'Total expense:{total:.2f} ')
print('{thousand} products more than R$1000 ')
print(f'The cheapest product was {cheap} costs: R${smaller:.2f}')