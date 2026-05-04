from random import randint
from time import sleep
from operator import itemgetter
dicionario = {'jogador1': randint(1,6),
              'jogador2': randint(1,6),
              'jogador3': randint(1,6),
              'jogador4': randint(1,6)}
print(' Valores sorteados:')
ranking = list()
for k, v in dicionario.items():
    print(f'     O {k} tirou {v}')
    sleep(0.7)
print(' Ranking dos jogadores:')
ranking = sorted(dicionario.items(), key=itemgetter(1), reverse=True)
for k,v in enumerate(ranking):
    print(f'    {k+1} lugar: {v[0]} com {v[1]}.  ')
    sleep(0.7)