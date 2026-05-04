'''def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela
    :param i: inicio da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    função ensinada por gustavo Guanabara
    """
    cont = i
    while cont >= f:
        print(f'{cont}', end='  ', flush=True)
        cont -= p
    print('FIM!')


#help(contador)
def somar(a=0, b=0, c=0):
    """
    Faz a soma dis três valores e mostra na tela..
    :param a: o primeiro valor
    :param b: o segundo valor
    :param c: o terceiro valor
    Função para somar criada por vini
    """
    soma = a + b + c
    print(f'A soma vale {soma}')


somar(1,2)
somar(1,2,7)
somar(c=3, a=9)

def teste(b):
    global a
    a = 8
    b += 4
    c = 3
    print(a, b ,c)


a = 5
b = 4
teste(a)
print(a)'''

def somar(a=0, b=0, c=0):
    s = a + b + c
    return s


r = somar(1, 2, 3)
r2 = somar(4, 3)
r3 = somar(5)

print(f'Os resultados foram {r}. {r2}, {r3}')