#Program who read the name and price of a lot products. The program will ask for the user if him want continue. In the 
#end show: What is the total expense. How many products cust more than R$1000.
#What is the product name more cheap
op = '' #will store the option (if the user want continue or not)
price = 0 #will store the price of a product
total = 0 #will calculate the total expense 
moreproduct = 0 #will store how many products cust more than R$1000
morecheapprice = 1000 #will store the price of the more expensive product
morecheapname = '' #will store the name of the more expensive product 
print('----- MARKETPLACE -----')
pn = str(input('Type the product name: '))
price = int(input(('Type the product price R$: ')))
op = str(input('Continue?: ')).strip().upper()
while op == 'YES':
    while op not in ('YESyesNOno'):
        print('invalid!')
        op = str(input('Type just yes or no: ')).strip().upper()
    print('----- MARKETPLACE -----')
    pn = str(input('Type the product name: '))
    price = int(input(('Type the product price R$: ')))
    op = str(input('Continue? ')).strip().upper()
    if price > 1000:
        moreproduct += 1
        if price > morecheapprice:
            morecheapprice = price
            morecheapname = pn
    elif op == 'NO':
        break
total += price
print('---------- END ----------')
print(f'Total expense: R${total}')
print(f'{moreproduct} products cust more than R$1000')
print(f'Product name more cheap: {morecheapname} that costs: R${morecheapprice}')