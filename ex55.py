#FOR
#Program who read the weight of 5 people and show wich was the biggest and the smallest 
bigger = 0
smaller = 0
for c in range(1, 6):
    weight = float(input('Weight of the {}ª person:'.format(c)))
    if c == 1:
        bigger = weight
        smaller = weight
    if weight > bigger:
        bigger = weight
    if weight < smaller:
        smaller = weight 
print('The bigger weight is: {} kg'.format(bigger))
print('The smaller weight is: {} kg'.format(smaller))