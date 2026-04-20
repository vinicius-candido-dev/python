def leiaInt(msg):
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric() == True:
            valor = int(n)
            break
        else:
            print('\033[31mErro! digite um número inteiro valido\033[m')
    return valor


n = leiaInt('Digite um número:  ')
print(f'Você acabou de digitar o númrto {n}')