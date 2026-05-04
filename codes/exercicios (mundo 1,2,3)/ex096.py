def área(larg, comp):
    area = largura * comprimento #/ 2
    print(f'A área do terreno {largura} x {comprimento} é de {area:.1f}m².')


print('-'*25)
print('  CONTROLE DE TERRENOS')
print('-' * 25)
largura = float(input('Digite a largura (m):  '))
comprimento = float(input('Digite seu comprimento:  '))
área(largura, comprimento)
