lista = list()
big = small = 0
for a in range(0,5):
    lista.append(int(input(f'digite um numero para a posição {a}:  ')))
    if a == 0:
        big = small = lista[a]
    else:
        if lista[a] > big:
            big = lista[a]
        if lista[a] < small:
            small = lista[a]
for a,b in enumerate(lista):
    if b == big:
        positionbig = a
print(f'o maior número digitado foi {big} na posição {positionbig}...')
for a,b in enumerate(lista):
    if b == small:
        positionsmall = a
print(f'o menor número digitado foi {small} na posição {positionsmall}...')


'''print(lista)
lista.sort(reverse=True)

lista.sort()
'''