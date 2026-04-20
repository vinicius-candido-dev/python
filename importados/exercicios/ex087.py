matriz = [[0,0,0], [0,0,0], [0,0,0]]
soma = i = d = soma_terceira = 0
for l in range(0,3):
    for c in range(0,3):
        i +=1
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]:  '))
        if matriz[l][c] % 2 == 0:
            soma += matriz[l][c]
        if i == 3 or i == 6 or i ==9:
            soma_terceira += matriz[l][c]
        if i == 4:
            d = matriz[l][c]
        elif 3 > i < 7:
            if d < matriz[l][c]:
                d = matriz[l][c]
print('-='* 30)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end= '')
    print()
print(f'A soma dos valores pares é {soma}')
print(f'A soma dos valores ta coluna linha é {soma_terceira}')
print(f'O maior valor da segunda linha é {d}')
