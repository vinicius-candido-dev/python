dictionary = {}
lista = []
pessoas = []
while True:
    dictionary.clear()
    lista.clear()
    dictionary['name'] = str(input('Nome do Jogador:  '))
    matches = int(input(f'Quantas partidas {dictionary["name"]} jogou?  '))
    for a in range(0,matches):
        lista.append(int(input(f'    Quantos gols na partida {a}?  ')))
    dictionary['gols'] = lista[:]
    dictionary['total'] = sum(lista)
    pessoas.append(dictionary.copy())
    while True:
        parar = input('Quer continuar? [S/N]').upper().strip()[0]
        if parar in 'NS':
            break
        print('ERRO! Responda apenas S or N.')
    if parar == 'N':
        break
print('-='*30)
print(f'cod', end='')
for i in dictionary.keys():
    print(f'{i:<15}', end='')
print()
print('-'*40)
for k, v in enumerate(pessoas):
    print(f'{k:>3}' , end=' ')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print(f'{'-'*40}')
while True:
    jogador = int(input('Mostrar os dados de qual jogador? (999 para parar)  '))
    if jogador == 999:
        break
    if jogador >= len(pessoas):
        print(f'ERRO! Não existe jogador com esse codigo {jogador}  ')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {pessoas[jogador] ["name"]}:')
        for i, g in enumerate(pessoas[jogador]["gols"]):
            print(f' fez {g} gols.')
    print('-'* 40)
print('<< VOLTE SEMPRE >>')
