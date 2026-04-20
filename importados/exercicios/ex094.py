cadastrar = {}
cadastrados = list()
media = 0
while True:
    cadastrar.clear()
    cadastrar['nome'] = str(input('Nome:  '))
    while True:
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
        if sexo in 'MF':
            break
        print('ERRO: por favor, digite apenas M ou F.')
    cadastrar['sexo'] =  sexo
    cadastrar['idade'] = int(input('idade:  '))
    media += cadastrar["idade"]
    cadastrados.append(cadastrar.copy())
    while True:
        parar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if parar in 'SN':
            break
        print('ERRO! responda apenas S ou N.')
    if parar == 'N':
        break
media_final =  media / len(cadastrados)
print('-='*30)
print(f'''A) Ao todo temos {len(cadastrados)} pessoas cadastradas.
B) A média de idade é de {media_final:5.2f} anos.''')
print(f'C) As mulheres cadrastradas foram ', end='')
for c in cadastrados:
    if c["sexo"] in 'Ff':
        print(f'{c["nome"]}', end=' ')
print('\nD) Lista das pessoas que estão que estão acima da média:')
for h in cadastrados:
        if h["idade"] >= media_final:
            print('    ', end='')
            for k,v in h.items():
                print(f'{k} = {v}; ', end='')
            print()
print('<< ENCERRADO >>')
