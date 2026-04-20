grupos = list()
lista = list()
maior = menor = 0
while True:
    nome = input('Digite o nome da pessoa:  ')
    peso = float(input('digite o peso da pessoa:  '))
    grupos.append(nome)
    grupos.append(peso)
    if len(lista) == 0:
        menor = maior = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
    lista.append(grupos[:])
    grupos.clear()
    continuar = input('Quer continuar?')
    if continuar in 'Nn':
        break
print(f'Ao todo, você  cadastrou {len(lista)} pessoas.')
print(f'O maior peso foi de {maior}.0kg. Peso de ', end=', ')
for p in lista:
    if p[1] >= maior:
        print(f'{p[0]}', end=' ')
print(f'\nO menor peso foi de {menor}.0kg. Peso de ', end=',')
for p in lista:
    if p[1] == menor:
       print(f'{p[0]}', end=' ')
