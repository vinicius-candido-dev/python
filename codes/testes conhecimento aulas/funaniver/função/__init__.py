#existencia
def existe(arquive):
    """
    Essa função verifica a existencia de um arquivo .txt ou cria se não existir
    :param arquive: existe("arquivo.txt")
    :return: criado, existe e qual o erro
    """
    from os import path
    if path.exists(arquive):
        print("existe")
        pass
    else:
        try:
            with open(arquive, "w") as arquivo:
                print('criado')
                pass
        except Exception as e:
            print(f"ERROR AO CRIAR O ARQUIVO {e}")

#se é pra adicionar
def add(day, month, person):
    try:
        with open("birthdays.txt", "a", encoding="UTF-8") as arquivo:
            arquivo.write(f"{day},{month},{person}\n")
    except Exception as a:
        print(f"ERRO AO ADICIONAR POR {a}")

#todas as datas
def all():
    try:
        with open("birthdays.txt", "r", encoding="UTF-8") as arquivo:
            conteudo = arquivo.read()
            print(conteudo)
    except Exception as e:
        print(f"Erro em {e}")

#verificar as datas pra o dia
def aniversario_hoje():




