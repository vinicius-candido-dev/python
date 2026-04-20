def arquivoExiste(arquivo):
    try:
        a = open(arquivo, 'rt')
        a.close()
    except:
        return False
    else:
        return True


def criararg(arquivo):
    try:
        a = open(arquivo, 'wt+')
    except:
        print('Houve um Erro na criação do arquivo')

def lerArq(arquiv):
    try:
        a = open(arquiv, 'rt')
    except:
        print('Houve um Erro na lista de arquivos')
    else:
        for lin in a:
            dado = lin.split(':')
            dado[1] = dado[1].replace('\n', '')
            print(dado[2])
    finally:
        a.close()
