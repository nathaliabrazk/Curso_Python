#Program will simulate the operation of an ATM. At first, ask to the user what it be the value to be withdrawn
#(intenger number) and the program will informate how many ballots of each value will be delivered
#OBS consider that the cashier has banknotes of R$50, R$20, R$10 and R$1
print('=' * 30)
print('             ATM')
print('=' * 30)
value = int(input('Enter the amount you want to withdraw R$: '))
total = value
ballot = 50
totalballot = 0
while True: 
    if total >= ballot:
        total -= ballot
        totalballot += 1
    else: 
        if totalballot > 0:
            print(f'Total of {totalballot} ballots of R${ballot}')
        if ballot == 50:
            ballot = 20
        elif ballot == 20:
            ballot = 10
        elif ballot == 10:
            ballot = 1
        totalballot = 0
        if total == 0:
            break
print('=' * 30)
print('Thank you and welcome back! ')
print('=' * 30)

