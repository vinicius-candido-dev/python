from ex115 import arquivo
from função import *
from tela import *
arq = 'birthdays.txt'
if not arquivoExiste(arq):
    criararg(arq)
while True:
    interface('TEM ANIVÉRSARIO?')
    escolha = menu('informe um número  ')
    if escolha == 1:
        lerArq(arq)

    break