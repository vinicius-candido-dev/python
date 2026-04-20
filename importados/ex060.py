# com modulo
from math import factorial
num = int(input('Digite um numero para calcular o fatorial: '))
a = 0
c = factorial(num)
print('{}! ='.format(num), end=' ')
for a in range(num,0,-1):
    print(f' {a} ',end='')
    print(f'x' if a > 1 else '=',end='')
print(f' {c}',end='')

# sem modulo
n = int(input('\nDigite um numero para calcular o fatorial: '))
c = n
f = 1
print('{}! ='.format(n), end=' ')
while n > 0:
    print(f'{n} ',end='')
    print (f' x ' if c > 1 else ' = ',end='')
    f *= n
    n -= 1
print('{}'.format(f))
