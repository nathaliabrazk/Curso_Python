#Program will read a expression who use parentheses. The program must to analyze the last expression and 
#inform if it has open and closed parentheses in the corect order 
expr = str(input('Digite a expressão: '))
pi = expr.count('(')
pf = expr.count(')')
if expr.index(')') > expr.index('('):
    if pi == pf:
        print('Expressão válida')
    else:
        print('Expressão é inválida')
else:
    print('Expressão inválida')