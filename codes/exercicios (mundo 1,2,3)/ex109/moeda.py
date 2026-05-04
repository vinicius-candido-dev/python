def metade(valor=0, formato=False):
    '''
    A função aumentar
    :param valor: informe um valor
    :param formato: por padrão é false em caso de True vai mostar formatada com R$ e ,00
    :return: retorna o valor formatado
    '''
    res = valor / 2
    return res if not formato is False else moeda(res)


def dobro(valor=0, formato=False):
    res = valor * 2
    return res if formato is False else moeda(res)


def aumentar(valor=0, porcentagem=0, formato=False):
     res = valor + (valor * porcentagem / 100)
     return res if formato is False else moeda(res)


def diminuir(valor=0, porcentagem=0, formato=False):
     res = valor - (valor * porcentagem / 100)
     return res if formato is False else moeda(res)


def moeda(valor=0, moeda='R$' ):
    if format == False:
        return valor
    else:
        return f'{moeda}{valor:>.2f}'.replace('.',',')