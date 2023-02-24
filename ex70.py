#Program who read the name and price of a lot products. The program will ask for the user if him want continue. In the 
#end show: What is the total expense. How many products cust more than R$1000.
#What is the product name more cheap
op = ''
price = 0
total = 0
moreproduct = 0
morecheapprice = 1000
morecheapname = ''
pn = str(input('Type the product name: '))
price = int(input(('Type the product price: ')))
op = str(input('Continue?(Type yes or no): ')).strip().upper()
while op == 'YES':
    while op not in ('YESNO'):
        print('invalid!')
        op = str(input('Type just yes or no:')).strip().upper()
    pn = str(input('Type the product name:'))
    price = int(input(('Type the product price:')))
    total = total + price
    op = str(input('Continue? ')).strip().upper()
    if price > 1000:
        moreproduct += 1
        if price > morecheapprice:
            morecheapprice = price
            morecheapname = pn
    elif op == 'NO':
        break
print('end')
print(f'Total expense: {total}')
print(f'{moreproduct} products cust more than R$1000')
print(f'Product name more cheap: {morecheapname} that costs: {morecheapprice}')