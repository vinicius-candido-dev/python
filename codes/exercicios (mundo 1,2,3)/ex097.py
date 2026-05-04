def escreva(msg):
        tamanho = len(msg) + 4
        print('~' * tamanho)
        print(f'{msg:^{tamanho}}')
        print('~' * tamanho)


escreva('Gustavo Guanabara')
escreva('Curso de Python no YouTube')
escreva('CeV')


