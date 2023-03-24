#Program who read a phrase and show:
#*How many times does the letter "A" appears;
#*What position does it appear in the first time;
#*What position does it appear in the last time.
phrase = str(input('Type a phrase:')).strip().upper()
print('The letter "A" apears: {} times'.format(phrase.count('A')))
print('The position where "A" first appears:{}'.format(phrase.find('A')+1))
print('The position where "A" last appears:{}'.format(phrase.rfind('A')+1))