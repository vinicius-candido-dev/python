l1 = int(input('informe lado do triãngulo: '))
l2 = int(input('informe outro lado do triãngulo: '))
l3 = int(input('informe outro lado do triãngulo: '))
if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:
    if l1 == l2 and l3 == l1:
        print('Equilatero: todos os lados iguais')
    elif l1 == l2 and l2 != l3 or l1 == l3 and l2 != l1 or l1 == l3 and l2 != l1:
        print('Isóceles: dois lados iguais')
    elif l2 != l1 and l3 != l2:
        print('Escaleno: todos os lados são diferentes')
else:
    print('Não é um triãgulo')