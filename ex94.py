#DICIONARY
#LIST OF DICIONARYS
#The program will read the name, age, sex of a several people keeping the datas of each person on a dicionary
#and all the dicionarys on a list. Show:
#a)How much people were registered *
#b)The avarage of age from the group 
#c)A list with all the womans*
#d)A list with all the people with age above average 
galera = list()
pessoa = dict()
soma = media = 0
while True:
    pessoa['nome'] = str(input('Nome:'))
    while True:
        if pessoa['sexo'] in 'MF':
            break 
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
    print('-=' * 30)
    print(f'Ao todo temos {len(galera)} pessoas cadastradas')
    media = soma / len(galera)
    print(f'A media de idade é de {media:5.2f} anos')
    print(f'As mulheres cadastradas foram ', end='')
    for p in galera:
        if p['sexo'] in 'Ff':
            print(f'{p["nome"]}', end='')
    print()
    print('D) Listas das pessoas que estão acima da média: ', end='' )