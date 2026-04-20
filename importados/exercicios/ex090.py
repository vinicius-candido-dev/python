mun = {}
mundo = []
mun['nome'] = str(input('Nome:  '))
mun['media'] = float(input(f'media de {mun["nome"]}:  '))
if mun["media"] >= 7:
    mun['situação'] = 'Aprovado'
elif mun["media"] < 5:
    mun['situação'] = 'Reprovado'
else:
    mun['situação'] = 'Recuperação'
mundo.append(mun.copy())
print('=-'*30)
for e in mundo:
    for l, v in e.items():
        print(f'  - {l} é igual a {v}')