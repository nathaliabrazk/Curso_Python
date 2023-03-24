#DICIONARY
#Program that manage a use of a football player. The program will read the soccer player name and 
#how much matches him played. After will read the quantidy of goals made in each matches. After
#all this will be saved on a dicionary, including the total of goals madet during a champeonship
regist = dict()#dicionary
regist['name'] = str(input('Name:'))
regist['matches'] = int(input('Quanty of matches:'))
for c in range (regist['matches']):
    regist['goal'] = int(input('Quanty of goals: '))
print('-=' * 30)
print(f'The player of soccer {regist["name"]} play {regist["matches"]} matches')