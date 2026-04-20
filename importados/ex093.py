dictionary = {}
lista = []
dictionary['name'] = str(input('Nome do Jogador:  '))
matches = int(input(f'Quantas partidas {dictionary["name"]} jogou?  '))
for a in range(0,matches):
    lista.append(int(input(f'    Quantos gols na partida {a}?  ')))
dictionary['gols'] = lista[:]
dictionary['total'] = sum(lista)
print('-='*30)
print(dictionary)
print('-='*30)
for k,v in dictionary.items():
    print(f'O jogador {k} tem o valor {v}')
print('-='*30)
print(f'O jogador {dictionary["name"]} jogou {dictionary["total"]} partidas.')
for k,v in enumerate(dictionary["gols"]):
    print(f'    => Na partida {k}, fez {v} gols.')
print(f'Foi um total de {dictionary["total"]} gols.')
