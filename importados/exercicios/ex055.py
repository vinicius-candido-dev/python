c = 0
big = 0
small = 0   #small = 1000 gustavo ensinou que tem q transformar  o peso o maior e o menor no primeiro resultado
for c in range(0, 5):
    weight = int(input('type the weight of a person: '))
    if c == 0:
        big = weight
        small = weight
    else:
        if weight > big:
            big = weight
        if weight < small:
            small = weight
print(f'the big wheight {big} and small wheight {small}   ')
