#Gustavo guanabara
sexo = str(input('Sexo [M/F]: ')).upper().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Sexo invalido. Por favor, informe seu sexo:  ')).upper()[0]
print(f'Sexo {sexo} registrado com sucesso')


#meu
'''a = 0
b = 0
while a != 1:
    sex = input('Sexo [M/F]: ').upper()[0]
    while True:
        if sex == 'M' or sex == 'F':
            break
        else:
            print('Sexo invalido.', end=' ')
            sex = input('Por favor, informe seu sexo: ').upper()[0]
    if sex == 'M':
        print('sexo masculino registrado com sucesso')
        a += 1
    if sex == 'F':
        print('sexo feminino registrado com sucesso')
        a += 1'''
