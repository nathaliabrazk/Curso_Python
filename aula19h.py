#DICIONARY
estado = dict()#dict() = dicionary
brasil = list()
#loop to fill in brasil
for c in range(0,3):
    estado['uf'] = str(input('Uf: ')) 
    estado['sigla'] = str(input('Sigla: '))
    brasil.append(estado.copy())
#loop to data output
for e in brasil:
    print(e)
    for v in e.values():
        print(v,end='')