matriz = [[0,0,0], [0,0,0], [0,0,0]]
soma = i = d = soma_terceira = 0
for l in range(0,3):
    for c in range(0,3):
        i +=1
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]:  '))
print('-='* 30)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end= '')
    print()
