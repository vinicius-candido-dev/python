b = 0
one_term = int(input('type the first term: '))
reason = int(input('type the reason: '))
termo = one_term
print('-='*10)
while b!= 10:
   print(f'{termo} -> ',end='')
   termo += reason
   b += 1
print('Acabou')