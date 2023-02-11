#Program who read a phrase and say if her is a palindrome disregardin the spaces 
phrase = str(input('Type a phrase:')).strip().upper()
words = phrase.split()
together = ''.join(words)
invers = ''
for letter in range(len(together)-1, -1, -1):
    invers += together[letter]
print('The invers of: {} is {}'.format(together, invers))
if invers == together:
    print('The phrase is a palindrome!')
else:
    print('The phrase is not a palindrome!') 