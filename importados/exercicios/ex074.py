from random import randint
tupla = (randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10))
print(f'Os vaçlores sorteadoos foram: ',end='')
for c in tupla:
    print(f'{c}', end=' ')
print(f'\nmaior número foi: {max(tupla)}')
print(f'o menor número foi: {min(tupla)}')