numeros = []
while True:
    adicionar = int(input('Digite um valor:  '))
    if adicionar in numeros:
        print('Valor duplicado! Não adicionar...')
    else:
        numeros.append(adicionar)
        print('Valor adicionado com sucesso...')
    a = input('Deseja continuar? [S/N]').upper().strip()
    if a not in 'NS':
        a = input('Deseja continuar? [S/N]').upper().strip()
    else:
        if a == 'N':
            break
numeros.sort()
print(f'você digitou os valores {numeros}')
