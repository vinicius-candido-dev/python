person_idade = man = woman = 0
while True:
    print('_'*30)
    print('CADASTRE UMA PESSOA')
    print('_'*30)
    idade = int(input('Qual a sua idade? '))
    sexo = input('Qual o seu sexo? [M/F] ').upper()
    if sexo != 'M' and sexo != 'F':
        sexo = input('Qual o seu sexo? [M/F] ').upper()
    print('_'*30)
    continuar = input('Deseja continuar? [S/N] ').upper()
    if continuar != 'S' and  continuar != 'N':
        continuar = input('Deseja continuar? [S/N] ').upper()
    else:
        if idade > 18:
            person_idade +=1
        if sexo == 'F':
           if idade < 20:
                woman+=1
        if sexo == 'M':
            man+=1
        if continuar == 'N':
            break
print(f'total de  pessoas com mais de 18 anos: {person_idade} ')
print(f'Ao todo temos {man} homens cadastrados')
print(f'tem {woman} mulheres com menos de 20 anos')
