#BANK LOAN
#Program to approve the bank loan for the purchase of a house. The program will ask for the HOME'S VALUE,
#THE BUYER'S SALARY and in HOW MANY YEARS HE WILL PAY. Calculate the amount of the monthly installment,
#knowing that i cannot exceed 30% of the buyer's salary or the loan will be denied.
home = float(input('Enter the value of a home:'))
salary = float(input('Enter your salary:'))
years = int(input('Enter in how many years you will pay:'))
necessary = salary / home
prc = salary * 30 / 100
if necessary > prc:
    print('Bank loan denied!')
else:
    print('Bank loan approved!')