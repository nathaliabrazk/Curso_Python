#Program who ask the number of km traveled of a rented car and the number of days for wich it was rented. calculate the price to pay. Knowing that the car costs R$60 per day and 0,15 per km driven
km = float(input( 'Type the number of km travaled:' ))
d = int(input( 'Type the number of days:' ))
p = (60 * d) + (0.15 * km)
print( 'The price to pay to {} km traveled and {} days is: {}R$'.format(km,d,p) )