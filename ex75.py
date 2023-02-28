#Program wll read 4 numbers and save them in a tuple. At the end show: a)How many times the number 9 appears. 
#b)In wich position was entered the number 3. c)What were the even numbers
values = tuple(int(input('Type a number: '))for c in range(1, 5))
print(f'O numero nove aparece {values.count(9)} vezes')
print(f'Valor 3 foi digitado pela primeira vez na {values.index(3)+1}º posição' if 3 in values else 'Não foi digitado valor 3')
print('Valores pares digitados foram', end=' ')
print({n for n in values if n % 2 == 0}, end=' ')