from random import randint
from time import sleep
números = []


def sorteia():
    print(f'Sorteando 5 valores da liata: ', end='')
    for a in range(0,5):
        números.append(randint(0,10))
    for g in números:
        print(f'{g}', end=' ', flush=True)
        sleep(0.5)
    print('PRONTO!')


def somar():
    soma = 0
    for b in números:
        if b % 2 == 0:
            soma += b
    print(f'A soma de todos os valores pares é {soma}')


sorteia()
somar()
