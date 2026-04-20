palavras = ('Franciely','Marina','Angelo','Flamengo','jogos','Python','Programação')
for i in palavras:
    print(f'\nNa palavra {[i.upper()]} temos: ', end='' )
    for letra in i:
        if letra.lower() in 'aeiou':
            print(letra.lower(), end=' ')