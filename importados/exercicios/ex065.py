media = big = small = n = b = c = 0
resp = 'S'
while resp in 'Ss':
    numeros = float(input('digite um número:  '))
    b += numeros
    media +=1
    if media == 1:
        small =big = numeros
    else:
        if numeros > big:
            big = numeros
        elif numeros < small:
            small = numeros
    continuar = input('quer continuar [S/N]?').upper()
    if continuar == 'N':
        break
c =  b / media
print(f'O maior numéro é de {big:.0f},e o menor numéro é de {small:.0f} e ', end='')
print(f'a media é de {c}')
