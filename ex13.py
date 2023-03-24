#Program who read the salary of an empoloyee and show your new salary with 15% of increase
s = float(input( 'Type the salary:') )
inc = (15 * s / 100)
ns = float(s + inc)
print('New salary:{:.2f}'.format(ns) )