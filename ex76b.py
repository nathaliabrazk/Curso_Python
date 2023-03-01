##Program will have a single tuple that stores product names with their respective values. Then show 
#a list of prices, organizing the data on tabular form
p = ('Milk', 3.0, 'Bread', 0.50, 'Orange juice', 2.0, 'Strawberry pie', 4.0, 'Grape jelly', 10.0, 
            'Honey', 6.0, 'Cocunut cake', 2.50, 'Lemon cake', 2.50, 'Orange cake', 2.50, 'Party cake', 20.0)
print('-' * 40)
print(f'{"PRICE LIST":^40}')
print('-' * 40)
for pos in range(0, len(p)):
    if pos % 2 == 0:
        print(f'{p[pos]:.<30}',end='')
    else:
        print(f' R$ {p[pos]:>7.2f}')