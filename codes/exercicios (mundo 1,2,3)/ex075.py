tupla = (int(input('digite um numero: ')),
int(input('digite outro numero: ')),
int(input('digite outro numero: ')),
int(input('digite outro numero: ')))
#total de vezes q o 9 apareceu
print(f'O número 9 está na posição {tupla.count(9)}ª ')
#posição de 3
if 3 in tupla:
    print(f'o numéro 3 apareceu na tupla na posição {tupla.index(3)+1}')
else:
    print(f'Não existe 3 na tupla')
#pares
print(f'esses numeros são pares: ',end=' ')
for i in tupla:
    if i%2==0:
        print(i, end=' ')
