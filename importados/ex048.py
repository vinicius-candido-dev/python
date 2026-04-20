cont = 0
c = 0
for i in range(1, 501,2):
    if i % 3 == 0:
        print(i, end=' ')
        c += i
        cont += 1
print(f'\n{c} ')
print(f'{cont} ')


