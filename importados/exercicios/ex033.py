a = int(input('digite um numero '))
b = int(input('digite outro numero '))
c = int(input('digite outro numero '))
if a < b and a < c:
    menor = a
    print(f'o menor numero {menor} ')
if b < a and b < c:
    menor = b
    print(f'o menor numero {menor}')
if c < a and c < b:
    menor = c
    print(f'o menor numero {menor}')
if a > b and a > c:
    maior = a
    print(f'o maior numero {maior}')
if b > a and b > c:
    maior = b
    print(f'o maior numero {maior}')
if c > b and c > a:
    maior = c
    print(f'o maior numero {maior}')
