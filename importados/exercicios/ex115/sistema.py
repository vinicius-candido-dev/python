from ex115.funçoes import *
from ex115.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'
if arquivoExiste(arq):
    print('Arquivo encontrado com sucesso!')
else:
    print('Arquivo não encontrado!')
    criarArquivo(arq)
while True:
    menu()
    açãoe = opc()
    if açãoe == 1:
        lerArquivo(arq)
    elif açãoe == 2:
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome:  '))
        idade = leiaInt('Idade:  ')
        cadrastrar(arq, nome, idade)
    elif açãoe == 3:
        sair()
        break
    sleep(2)