lista = [[], []]
valores = list()
numeros = 0
for a in range(1,8):
    numeros = int(input(f'Digite o {a}o. valor:  '))
    if numeros % 2 == 0:
        lista[0].append(numeros)
    else:
        lista[1].append(numeros)
lista[0].sort()
lista[1].sort()
print('-='*40)
print(f'Os valores pares digitados foram:  {lista[0]}')
print(f'Os valores ímpares digitados foram:  {lista[1]}')