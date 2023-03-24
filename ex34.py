#CONDITIONAL
#Program will ask the salary of a worker and calculate the value of your increase.
#For higher salaries of R$1.250,00, calculate a increase of 10%
#For lesses or equal, the increase is of 15%
salary = float(input('Type a salary:'))
if salary > 1.250:
    print('Original salary:R${}\nSalary with increase:R${:.2f}'.format(salary,salary * 1.10))
elif salary <= 1.250:
    print('Original salary:R${}\nSalary with increase:R${:.2f}'.format(salary,salary * 1.15))