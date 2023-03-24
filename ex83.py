#LIST
#Program will read a expression who use parentheses. The program must to analyze the last expression and 
#inform if it has open and closed parentheses in the corect order 
expr = str(input('Digite a expressão: '))
popen = expr.count('(')
pclose = expr.count(')')
if expr.index(')') > expr.index('('):
    if popen == pclose:
        print('Invalid expression!')
    else:
        print('Invalid expression!')
else:
    print('Valid expression!')