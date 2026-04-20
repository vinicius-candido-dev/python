def leiaDinheiro(msg):
    valido = False
    while not valido:
        nume = str(input(msg)).strip().replace(',', '.')
        if nume.isalpha() or nume == '':
            print(f'\033[31mERRO: \"{nume}\" é um preço inválido!\033[m')
        else:
            valido = True
    p = float(nume)
    return p
