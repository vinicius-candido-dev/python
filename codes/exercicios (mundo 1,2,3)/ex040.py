nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
noum = (nota1 + nota2)/2
print(noum)
if noum < 5.0:
    print('  \033[31m Reprovado \033[m ')
elif  5.0 >=  noum <= 6.9:
    print(' \033[34mRecuperação  \033[m' )
elif noum >= 7.0:
    print(' \033[32mAprovado \033[m ')
