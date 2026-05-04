par = list()
impar = list()
numeros  = list()
while True:
    numeros.append(int(input('Digite um numero: ')))
    continuar = input('Deseja continuar? [S/N]').upper().strip()[0]
    if continuar not in 'SN':
        continuar = input('Deseja continuar? [S/N]').upper().strip()[0]
        if continuar == 'N':
            break
for i, n in enumerate(numeros):
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
print(f'Os numeros digitados foram {numeros}')
print(f'os numeros pares digitados foram {par}')
print(f'os numeros impares digitados foram {impar}')
