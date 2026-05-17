from rich import print
from rich.table import Table
#existencia
def existe(arquive):
    """
    Essa função verifica a existencia de um arquivo .txt ou cria se não existir
    :param arquive: existe("arquivo.txt")
    :return: criado, existe e qual o erro
    """
    from os import path
    if path.exists(arquive):
        return "existe"
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
'''def all(): #com erro
    try:
        with open("birthdays.txt", 'r', encoding="utf-8") as f:
            for line in f:
                lin = line.strip().split(',')
                obj = {
                        "day": lin[0],
                        "month": lin[1],
                        "name": lin[2]}

                return f'A pessoa {obj["name"]} no mês {obj["month"]} no dia {obj["day"]}'

    except Exception as e:
        return f"Erro em {e}"
'''

#verificar as datas pra o dia
def aniversario_hoje():
    from datetime import date
    hoje = date.today()
    day = str(hoje.day)
    month = str(hoje.month)

    with open("birthdays.txt", "r", encoding="UTF-8") as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            partes = linha.split(',')

            if len(partes) == 3:
                dia = partes[0]
                mes = partes[1]
                nome = partes[2]

            if day == dia and mes == month:
                print(f"O aniversário de {nome} é hoje")
        if not day == dia:
            print("Ninguém faz aniversário nesse dia.")

#especificar data
def especificar(day, month):
    day = str(day)
    month = str(month)
    a = 0
    with open("birthdays.txt", "r", encoding="UTF-8") as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            partes = linha.split(',')

            if len(partes) == 3:
                dia = partes[0]
                mes = partes[1]
                nome = partes[2]

            if day == dia and mes == month:
                a += 1
                return f"O aniversário de {nome} é hoje"

    if a != 1:
        return "Ninguém faz aniversário nesse dia."


def tabl(nome,mes,dia,):
    tabela = Table(title='Lista')
    tabela.add_column('Dia')
    tabela.add_column('Mês')
    tabela.add_column("Nome")

    tabela.add_row(nome,mes,dia)

    return tabela

#tabela = tabl('11','1', 'vini')
#print(tabela)


#