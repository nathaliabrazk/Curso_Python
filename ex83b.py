#LIST
#Program will read a expression who use parentheses. The program must to analyze the last expression and 
#inform if it has open and closed parentheses in the corect order (with loop)
expression = ''
stack = []#this list gonna regist the parentheses
while True:
    expression = str(input('Type the expression:'))
    for simb in expression:
        if simb == '(':#if the symbol are a open parentheses the list gonna regist he
            stack.append('(')
        elif simb == ')':#if the second symbol are a open parentheses and the list is not empty this will mean that
            #the parentheses has your partner to close it
            if len (stack) > 0:
                stack.pop()#this method will delete the last position of a list(in this case because the index
                #was not typed)
            else:
                stack.append(')')
                break
    if len (stack) == 0:#if the list is empty this means the expression are correct because all the parentheses are 
        #closed with your partner
        print('The expression is it correct!')
    else:
        print('The expression is it incorrect!')
    op = str(input('Continue?')).strip().upper()
    if op in 'NOno':
        break
    elif op not in 'NOnoYESyes':
        op = str(input('Type just yes or no!\nContinue?'))
    