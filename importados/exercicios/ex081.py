numeros = list()
while True:
    numeros.append(int(input('Digite um valor:  ')))
    continuar = input('Deseja continuar? [S/N] ').strip().upper()[0]
    if continuar not in 'SN':
        continuar = input('Deseja continuar? [S/N] ').upper().strip()[0]
    elif continuar == 'N':
        break
print(numeros)
print(f'o total números digitados foi {len(numeros)}')
numeros.sort(reverse=True)
print(f'os valores digitados em ordem decrescente foram {numeros}')
if 5 in numeros:
    print(f'o numero 5 está na lista')
else:
    print(f'O numero 5 não está na lista')