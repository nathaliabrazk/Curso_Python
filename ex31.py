#CONDITIONAL
#Program will ask the distace of a trip in km. Calculate the price from the ticket.
#Charging R$0,50 for km to trips from to 200 km and R$0,45 to more longers trips
distance = int(input('Type the distance of a trip in km:'))
if distance <= 200:
    print('Ticket value: R$ {}'.format(distance * 0.50))
else:
    print('Ticket value: R$ {}'.format(distance * 0.45))