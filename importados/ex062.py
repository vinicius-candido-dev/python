one_term = int(input('type the first term: '))
reason = int(input('type the reason: '))
termo = one_term
print('-='*10)
contador = 0
total = 0
mais = 10
while mais != 0:
    total = total + mais
    contador = 0
    while contador < mais:
       print(f'{termo} -> ',end='')
       termo += reason
       contador += 1
    print('PAUSA')
    mais = int(input('quantos termos deseja ver? '))
print('fim')
