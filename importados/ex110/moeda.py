def metade(valor=0, formato=False):
    res = valor / 2
    return res if formato is False else moeda(res)


def dobro(valor=0, formato=False):
    res = valor * 2
    return res if formato is False else moeda(res)


def aumentar(valor=0, porcentagem=0, formato=False):
     res = valor + (valor * porcentagem / 100)
     return res if formato is False else moeda(res)


def diminuir(valor=0, porcentagem=0, formato=False):
     res = valor - (valor * porcentagem / 100)
     return res if formato is False else moeda(res)


def moeda(valor=0, moeda='R$'):
    return f'{moeda}{valor:>.2f}'.replace('.',',')


def resumo(p, aume=10, dimu=10):
    tabela = 30
    print('-' * tabela)
    print(f'{"RESUMO DO VALOR":^{tabela}}')
    print('-' * tabela)
    print(f'{"preço analisado:"} \t{moeda(p)}')
    print(f'{"Dobro do preço:"} \t{dobro(p, True)}')
    print(f'{"Metade do preço:"} \t{metade(p, True)}')
    print(f'{aume}{"% de aumento:"} \t{aumentar(p, aume, True)}')
    print(f'{dimu}% de redução: \t{diminuir(p, dimu, True)}')
    print('-' * tabela)
