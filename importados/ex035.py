a = int(input('Primeiro lado do triangulo: '))
b = int(input('segundo lado do triangulo: '))
c = int(input('terceiro lado do triangulo: '))
if a + b > c and c + b > a and a + c > b:
    print('verdadeiro', end='-')
else:
    print('falso')
print('fim')