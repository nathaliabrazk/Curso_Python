#Program who calculate the value to be paid out about a product considering its normal price
#and payment condition: |in cash money/10% of discount| |in cash on card/5% of discount| 
#|in until 2x on the card/normal price| |3x or more on the card 20% of fees|
price = float(input('Enter the purchase amount R$:'))
print('*=*' * 30)
print('                                     Payment menu')
print('*=*' * 30)
print('1 - In cash money\n2 - In cash on the card\n3 - In until 2x on the card\n4 - 3x or more on the card')
option = int(input('Type your choice:'))
if option == 1:
    print('You will pay in cash money, so you have 10% of discount!')
    discount = (10 * price / 100)
    print('The value of: R${} with discount is: R${}'.format (price, price - discount))
elif option == 2:
    print('You will pay in cash on card, so you have 5% of discount!')
    discount = (5 * price/ 100)
    print('The value of R${} with discount is: R${}'.format(price, price - discount))
elif option == 3:
    print('You will pay in until 2x on the card, so you go pay the normal price!')
    print('The purchase price:{}'.format(price))
elif option == 4:
    print('You will pay 3x or more on the card, so you have 20% of discount!')
    discount = (20 * price / 100)
    print('The value of R${} with discount is R${}'.format(price, price - discount))
else:
    print('Type just (1, 2, 3 or 4!)')