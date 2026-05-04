from random import randint
from time import sleep
numeros = []
lista = []
print('-'*40)
print(f'{"JOGA NA MEGA SENA":^40}')
print('-'*40)
tot = 0
vez = int(input('quantos jogos você  quer que eu sorteie?  '))
print(f'-=-=-=   SORTEANDO {vez} JOGOS   -=-=-=')
while tot < vez:
    cont = 0
    while True:
        a = randint(1,60)
        if a not in numeros:
            numeros.append(a)
            cont += 1
        if cont >= 6:
            break

    numeros.sort()
    lista.append(numeros[:])
    numeros.clear()
    tot += 1
for i, l in enumerate(lista):
    print(f'jogo {i+1}:  {l}')
    sleep(1)
print(f' -=-=-=  < Boa Sorte! > -=-=-=')
