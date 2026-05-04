a = c = menor = maior = nome= 0
for a in range(1, 5):
    print('------{} PESSOA------'.format(a))
    name = str(input('type the name of the person: ')).capitalize().strip()
    year = float(input('type the year of the person: '))
    sex = str(input('type the sex of the person: '))
    c += year
    if sex in 'Ff':
        if year < 20:
            menor +=1
    elif sex in 'Mm':
        if year > maior:
            maior = year
            nome = name
    else:
        print('seu sexo invalido')
d = c / 4
print(f'A média de idade do grupo é {d}')
print(f' tem {menor} mulheres  com idades inferior a 20')
print(f'o homem mais velho é {nome} com {maior:.2f} anos')





