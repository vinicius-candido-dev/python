#meu
a = 0
while True:
    numeros = str(input('Qual tabuada você desaja ver?  '))
    n = numeros.find('-')
    if n == 0:
        print('PROGRAMA TABUADA ENCERRADO. volte semnpre')
        break
    else:
        n = int(numeros)
        for a in range(1,11):
            print(f'{n} x {a} = {n * a }')
        if a == 10:
           continue
#guanabara
while True:
    numeros = int(input('Qual tabuada você desaja ver?  '))
    if numeros < 0:
        print('PROGRAMA TABUADA ENCERRADO. volte semnpre')
        break
    for a in range(1,11):
        print(f'{numeros} x {a} = {numeros * a }')
