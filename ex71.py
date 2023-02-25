#Program will simulate the operation of an ATM. At first, ask to the user what it be the value to be withdrawn
#(intenger number) and the program will informate how many ballots of each value will be delivered
#OBS consider that the cashier has banknotes of R$50, R$20, R$10 and R$1
print('---------- ATM ----------')
value = int(input('Enter the amount you want to withdraw: '))
total = value
ballot = 50
while True: 