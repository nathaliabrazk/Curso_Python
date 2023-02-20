#Program who read the name and price of a lot products. The program will ask for the user if him want continue. In the 
#end show: What is the total expense. How many products cust more than R$1000.
#What is the product name more cheap
op = ''
price = 0
total = 0
moreproduct = 0
morecheap = 0
pn = str(input('Type the product name:'))
price('Type the product price:')
op = str(input('Continue? ')).strip().upper()
while op == 'YES':
    pn = str(input('Type the product name:'))
    price('Type the product price:')
    op = str(input('Continue? ')).strip().upper()
    if price > 1000:
        moreproduct += 1
print('end')
print(f'Total expense: {total}')
print(f'{moreproduct} products cust more than R$1000')
print(f'Product name more cheap: {morecheap}')