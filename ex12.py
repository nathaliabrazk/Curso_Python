#program who read the price of a product and show your new price, with 5% of discount
p = float(input( 'Type a price:'))
d = float(5*p/100)/100
newp = float(p-d)
print( 'Price with discount:{:.2f}'.format(newp))
 
