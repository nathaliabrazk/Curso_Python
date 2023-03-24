#DICIONARY
#Dicionary with list
MovieRental = list()
film = {'film': 'Star Wars', 'year': 1977 ,'director': 'George Lucas'}#gonna be the first position of the list MovieRental[0]
MovieRental.append(film)

film = {'film': 'Avengers', 'year': 2012, 'director': 'Josh Whedon'}#gonna be the second position of the list MovieRental[1]
MovieRental.append(film)

film = {'film': 'Matrix', 'year': 1999, 'director': 'Wachowski'}#gonna be the third position of the list MovieRental[2]
MovieRental.append(film)
print(MovieRental)
print(MovieRental[0]['year'])

#MovieRental
#-----------------------------------------------------------------------------------------------------
#|'Star Wars', 1997, 'George Lucas'||'Avengers', 2012, 'Josh Whedon'||'Avengers', 2012, 'Josh Whedon'|
#|---------------------------------||-------------------------------||-------------------------------|
#|  film       year    director    ||  film       year    director  ||  film       year    director  |
#-----------------------------------------------------------------------------------------------------
#               0                                  1                                 2
