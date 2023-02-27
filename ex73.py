#Program will create a tuple with the top 20 of the brazilian championship table. Then show: a) Only the top five
#b) Last placed in the table c) A list with times in alphabetical order d) In wich position in the table is the
#Chapecoense 
team = ('Atlético Mineiro', 'Flamengo', 'Palmeiras', 'Fortaleza',
        'Corinthians', 'Bragantino', 'Fluminense', 'América-MG',
        'Atlético Goianiense', 'Santos', 'Ceará', 'Internacional',
        'São Paulo', 'Atlélico-PR', 'Cuiabá', 'Juventude',
        'Grêmio', 'Bahia', 'Sport Recife', 'Chapecoense')
print('=' * 145)
print('                                                             TEAMS')
print('=' * 145)
print(team)
print('=' * 145)
print('                                                             TOP 5')
print('=' * 145)
print(team[0:5])
print('=' * 145)
print('                                                           THE LAST 4')
print('=' * 145)
print(team[16:])
print('=' * 145)
print('                                                    TEAMS IN ALPHABETICAL ORDER')
print('=' * 145)
print(sorted(team))
