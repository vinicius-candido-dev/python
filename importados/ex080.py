lista = []
for c in range(0, 5):
    lis = int(input('digite um valor:  '))
    if c == 0 or  lis > lista[-1]:
        lista.append(lis)
    else:
        pos = 0
        while pos < len(lista):
            if lis <= lista[pos]:
                lista.insert(pos, lis)
                print(f'adicionado na posição {pos} da lista...')
                break
            pos+=1

    print(lista)
