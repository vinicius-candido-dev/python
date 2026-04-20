from time import sleep
cor = ('\033[m',       # 0 - sem cor
       '\033[0;97;41m', # 1 - vermelho
       '\033[0;97;42m', # 2 - verde
       '\033[0;97;43m', # 3 - amarelo
       '\033[0;97;44m', # 4 - azul
       '\033[0;97;45m', # 5 - roxo
       '\033[7;97m'     # 6 - branco
       );


def ajuda(com):
    título(f'Acessando o manual do comando \'{com}\'', 4 )
    print(cor[6], end='')
    help(com)
    print(cor[0], end='')
    sleep(2)


def título(msg, c=0):
    tam = len(msg) + 4
    print(cor[c], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(cor[0], end='')
    sleep(1)

# programa principal
while True:
    título("SISTEMA DE AJUDA PyHELP", 3)
    fun = str(input('Função ou Biblioteca > '))
    if fun.upper() == 'FIM':
        break
    else:
        ajuda(fun)
título(f'ATÉ LOGO!', 1)
