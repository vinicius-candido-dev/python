number = int(input('type the number whole: '))
total = 0
for c in range(1,number+1):
    if number % c == 0:
        print('\033[34m{}\033[m'.format(c), end=' ')
        total += 1
    else:
        print(f'\033[33m{c}\033[m', end=' ')
print(f'\n O número {number} foi dividido {total} vezes')
if total ==2:
    print(f'\033[32mE por isso ele é primo')
else:
    print('\033[31mE por isso ele não é primo')
