#BANK LOAN
#Program to approve the bank loan for the purchase of a house. The program will ask for the HOME'S VALUE,
#THE BUYER'S SALARY and in HOW MANY YEARS HE WILL PAY. Calculate the amount of the monthly installment,
#knowing that i cannot exceed 30% of the buyer's salary or the loan will be denied.
home = float(input('Enter the value of a home R$'))
salary = float(input('Enter your salary R$'))
years = int(input('Enter in how many years you will pay:'))
provision = home / (years * 12)
necessary = salary * 30 / 100
print('To pay a home that costs R${:.2f} in {} years'.format(home,years), end = '')
print(' its necessary: R${:.2f} monthly'.format(provision))
if provision <= necessary:
    print('Loan approved!')
else:
    print('Loan dennied!')
