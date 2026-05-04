def fator (n=1, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor de Fatorial de um número n.
    """
    f = 1
    for c in range(n, 0 , -1):
        if show == True:
            print(c , end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f
print(fator(5, show=True))
help(fator)