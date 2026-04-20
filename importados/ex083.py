expressão = list(input('Digite a expressão: '))
a = expressão.count('(')
b = expressão.count(')')
if a == b:
    print('Está impressão é valida')
else:
    print('Essa expressão é invalida')